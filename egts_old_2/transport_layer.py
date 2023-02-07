from crc import Calculator, Configuration

crc8_config = Configuration(
    width=8,
    polynomial=0x0131,
    init_value=0xFF,
    final_xor_value=0x00,
    reverse_input=False,
    reverse_output=False,
)

crc8_calculator = Calculator(crc8_config)


class TransportLayer:
    protocol_version: int
    security_key_id: int
    header_length: int
    header_encoding: int
    frame_data_length: int
    package_id: int
    package_type: int
    header_check_sum: int

    def __init__(self, buff):
        self.protocol_version = buff[0]
        self.security_key_id = buff[1]
        self.header_length = buff[3]
        self.header_encoding = buff[4]
        self.frame_data_length = int.from_bytes(buff[5:7], byteorder='little')
        self.package_id = int.from_bytes(buff[7:9], byteorder='little')
        self.package_type = buff[9]
        self.header_check_sum = crc8_calculator.checksum(buff[:self.header_length - 1])

    def print_transport_layer(self):
        print('EGTS Transport Layer:')
        print('_____________________')
        print('\n')
        print('Protocol Version - ', self.protocol_version)
        print('Security Key ID - ', self.security_key_id)
        print('Header Length - ', self.header_length)
        print('Header Encoding - ', self.header_encoding)
        print('Frame Data Length - ', self.frame_data_length)
        print('Packet ID - ', self.package_id)
        print('Package Type - ', self.package_type)
        print('Header Check Sum - ', self.header_check_sum)
