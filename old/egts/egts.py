from bitstring import Bits
from crc import Calculator, Configuration
import crcmod

from . import egts_constants

crc16_func = crcmod.mkCrcFun(0x011021, initCrc=0xFFFF, rev=False)

crc8_config = Configuration(
    width=8,
    polynomial=0x0131,
    init_value=0xFF,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

crc16_config = Configuration(
    width=16,
    polynomial=0x011021,
    init_value=0xFFFF,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

crc8_calculator = Calculator(crc8_config)
crc16_calculator = Calculator(crc16_config)


class EGTSProtocol:
    buff: bytes
    protocol_version: int
    security_key_id: int
    flags: str
    prefix: str
    route: str
    encryption_alg: str
    compression: str
    priority: str
    header_length: int
    header_encoding: int
    frame_data_length: int
    package_id: int
    package_type: int
    header_check_sum: int
    service_layer: bytes

    def __init__(self, buff):
        self.buff = buff
        self.__parse_transport_layer()
        self.__parse_service_layer()

    def __parse_transport_layer(self):
        self.protocol_version = self.buff[0]
        self.security_key_id = self.buff[1]
        self.flags = Bits(int=self.buff[2], length=8).bin
        self.header_length = self.buff[3]
        self.header_encoding = self.buff[4]
        self.frame_data_length = int.from_bytes(self.buff[5:7], byteorder='little')
        self.package_id = int.from_bytes(self.buff[7:9], byteorder='little')
        self.package_type = self.buff[9]
        self.header_check_sum = crc8_calculator.checksum(self.buff[:self.header_length - 1])
        self.__encoding_flags()

    def __parse_service_layer(self):
        self.service_layer = self.buff[self.header_length:]

        body = self.service_layer[:self.frame_data_length]
        crc16_check_sum = crc16_calculator.checksum(self.service_layer)

        if self.package_type == egts_constants.EGTS_PT_APPDATA:
            self.__parse_egts_appdata()

        # print(crc16_check_sum)

        # crc16 = crc16_func(body)
        # body_crc = int.from_bytes(self.service_layer[self.frame_data_length:self.frame_data_length + 2], byteorder='little')
        #
        # print(crc16)
        # print(body_crc)
        # crc16 = crc16_calculator.checksum(body)
        # print(crc16)
        # print(self.service_layer)

    def __parse_egts_appdata(self):
        EgtsRecord.parse(buffer=self.service_layer)

        # record_length = int.from_bytes(self.service_layer[0:3], byteorder='little')
        # record_number = int.from_bytes(self.service_layer[2:4], byteorder='little')
        # record_flags = Bits(int=self.service_layer[4], length=8).bin
        #
        # tmfe = self.service_layer[4] >> 2 & 1
        # evfe = self.service_layer[4] >> 1 & 1
        # obfe = self.service_layer[4] & 1
        #
        # opt_len = (tmfe + evfe + obfe) * 4
        #
        # source_service_type = self.service_layer[5 + opt_len]
        # recipient_service_type = self.service_layer[6 + opt_len]
        # print(recipient_service_type)

        # header_len = egts_constants.EGTS_SERVICE_LAYER_MIN_RECORD_HEADER_LEN + opt_len
        #
        # source_service_type = self.service_layer[5 + opt_len]
        # recipient_service_type = self.service_layer[6 + opt_len]
        # print(recipient_service_type)

    def __encoding_flags(self):
        self.prefix = self.flags[:3]
        self.route = self.flags[2]
        self.encryption_alg = self.flags[3:5]
        self.compression = self.flags[5]
        self.priority = self.flags[6:]

    def print_transport_layer(self):
        print('EGTS Transport Layer:')
        print('_____________________')
        print('\n')
        print('Protocol Version - ', self.protocol_version)
        print('Security Key ID - ', self.security_key_id)
        print('Flags - ', self.flags)
        print('\t Prefix - ', self.prefix)
        print('\t Route - ', self.route)
        print('\t Encryption Alg - ', self.encryption_alg)
        print('\t Compression - ', self.compression)
        print('\t Priority - ', self.priority)
        print('Header Length - ', self.header_length)
        print('Header Encoding - ', self.header_encoding)
        print('Frame Data Length - ', self.frame_data_length)
        print('Packet ID - ', self.package_id)
        print('Package Type - ', self.package_type)
        print('Header Check Sum - ', self.header_check_sum)


class EgtsRecord:

    @staticmethod
    def parse(buffer):
        record_length = int.from_bytes(buffer[0:3], byteorder='little')
        record_number = int.from_bytes(buffer[2:4], byteorder='little')

        tmfe = buffer[4] >> 2 & 1
        evfe = buffer[4] >> 1 & 1
        obfe = buffer[4] & 1

        opt_len = (tmfe + evfe + obfe) * 4

        source_service_type = buffer[5 + opt_len]
        recipient_service_type = buffer[6 + opt_len]
