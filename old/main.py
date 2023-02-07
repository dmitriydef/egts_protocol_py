from egts.egts import EGTSProtocol

# from crc import Calculator, Configuration
# from bitstring import BitArray, Bits
#
from egts.transport_layer import TransportLayer

#
# config = Configuration(
#     width=8,
#     polynomial=0x0131,
#     init_value=0xFF,
#     final_xor_value=0x00,
#     reverse_input=False,
#     reverse_output=False,
# )
#
# calculator = Calculator(config)

auth = b'\x01\x00\x00\x0b\x00(\x00\x01\x00\x01\xa5\x19\x00:\t\x85\x00\x00\x00\x00\xc7\x97\x9f\x18\x01\x01\x01\x16\x00' \
       b'\x00\x00\x00\x00\x03\x00\x008687280351376597\xcc'

auth2 = b'\x01\x00\x00\x0b\x00(\x00\x02\x00\x01o\x19\x00;\t\x85\x00\x00\x00\x00\xd1\x97\x9f\x18\x01\x01\x01\x16\x00' \
        b'\x00\x00\x00\x00\x03\x00\x00868728035137659\xa1_ '

auth3 = b'\x01\x00\x00\x0b\x00(\x00\x03\x00\x01)\x19\x00<\t\x85\x00\x00\x00\x00\xdb\x97\x9f\x18\x01\x01\x01\x16\x00' \
        b'\x00\x00\x00\x00\x03\x00\x00868728035137659\x9d\xfd '
auth4 = b'\x01\x00\x00\x0b\x00(\x00\x04\x00\x01\xca\x19\x00=\t\x85\x00\x00\x00\x00\xe5\x97\x9f\x18\x01\x01\x01\x16' \
        b'\x00\x00\x00\x00\x00\x03\x00\x00868728035137659\xf7\x98 '

z = b"\x01\x00\x00\x0b\x00#\x00\x00\x00\x01\x99\x18\x00\x00\x00\x01\xef\x00\x00\x00\x02\x02\x10\x15\x00\xd21+\x10O\xba:\x9e\xd2'\xbc5\x03\x00\x00\xb2\x00\x00\x00\x00\x00j\x8d"

nav_packet2 = b"\x01\x00\x03\x0b\x00\x23\x00\x00\x00\x01\x42\x18\x00\x00\x00\x01\xef\x00\x00\x00\x02\x02\x10\x15\x00" \
              b"\xd2\x31\x2b\x10\x4f\xba\x3a\x9e\xd2\x27\xbc\x35\x03\x00\x00\xb2\x00\x00\x00\x00\x00\x6a\x8d"

test = "0100000b002300000001991800000001ef0000000202101500d2312b104fba3a9ed227bc35030000b200000000006a8d"

test2 = "0100020B0067000100019360000200000202101800EE66681848E2BE7B52F80A3E8100805DED94050005C201001102000" \
        "80F140500027F002A00170200400617020050061702006006170200700617020080061702009006170200A006170200B0061D0D" \
        "0000000001080000000000000000FCEC"

egts = EGTSProtocol(buff=nav_packet2)

# print(nav_packet2.hex())
# egts_old_2.print_transport_layer()

# egts_old_2 = TransportLayer(buf=nav_packet2)
#
# egts_old_2.print_transport_layer()
# egts_old_2 = EGTSProtocol(buf=nav_packet2)
#
# print(egts_old_2.hell())

# transport_layer = TransportLayer(bytes.fromhex(test))
#
# transport_layer.print_transport_layer()
#
# print(int.from_bytes(b'\x8D6A', byteorder='little'))


# def transport_layer(buff):
#     protocol_version = buff[0]
#     security_key_id = buff[1]
#     flags = buff[2]
#     header_length = buff[3]
#     header_encoding = buff[4]
#     frame_data_length = int.from_bytes(buff[5:7], byteorder='little')
#     package_id = int.from_bytes(buff[7:9], byteorder='little')
#     package_type = buff[9]
#
#     header = buff[:header_length]
#     header_crc = header[-1]
#
#     header_check_sum = calculator.checksum(header[:-1])
#
#     print('Protocol Version', protocol_version)
#     print('Security Key ID', security_key_id)
#     print('Flags', flags)
#     print('Header Length ', header_length)
#     print('Header Encoding ', header_encoding)
#     print('Frame Data Length ', frame_data_length)
#     print('Package Id ', package_id)
#     print('Package Type ', package_type)
#     print('Head Check Sum', header_check_sum)
#
#     c = Bits(int=flags, length=8)
#     print(c.bin)
#     # z = b"\x03"
#     # print(int.from_bytes(z, byteorder='little'))
#     # input_str = flags.__str__()
#     # print(flags)
#     # print(input_str)
#     # z = [bin(byte) for byte in bytes(input_str, "utf-8")]
#     # print(z)
#     # val = (int.from_bytes(b"\x03", byteorder='little') >> 6) & 3
#     # print(val)
#     # print((flags >> 6) & 1)
#     # z = "0x03"
#     # c = BitArray(hex=z)
#     # print(c.bin)
#
#
# transport_layer(nav_packet2)
# print(nav_packet2.hex())
# print(auth.hex())
# print(ord(b'\xA5'))
# # transport_layer(auth4)
# # print(int.from_bytes(b'\xCA', byteorder='little'))
# print(ord(b'\xCA'))
# r = auth4.hex()
# c = crc.crc8(r[1:9])
# print(c)
# # print(auth4.hex())
