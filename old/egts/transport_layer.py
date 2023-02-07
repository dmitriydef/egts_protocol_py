from bitstring import Bits
from crc import Calculator, Configuration

config = Configuration(
    width=8,
    polynomial=0x0131,
    init_value=0xFF,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

calculator = Calculator(config)


class TransportLayer:
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

    def __init__(self, buf):
        self.protocol_version = buf[0]
        self.security_key_id = buf[1]
        self.flags = Bits(int=buf[2], length=8).bin
        self.header_length = buf[3]
        self.header_encoding = buf[4]
        self.frame_data_length = int.from_bytes(buf[5:7], byteorder='little')
        self.package_id = int.from_bytes(buf[7:9], byteorder='little')
        self.package_type = buf[9]
        self.header_check_sum = calculator.checksum(buf[:self.header_length-1])
        self.__encoding_flags()

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
