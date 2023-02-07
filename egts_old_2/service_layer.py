class ServiceLayer:
    record_length: int
    record_number: int
    source_service_type: int
    recipient_service_type: int
    record_data: int

    def __init__(self, buff):
        print(buff)
        self.record_length = int.from_bytes(buff[:2], byteorder='little')
        self.record_number = int.from_bytes(buff[2:4], byteorder='little')
        self.record_number = int.from_bytes(buff[2:4], byteorder='little')

        tmfe = buff[4] >> 2 & 1
        evfe = buff[4] >> 1 & 1
        obfe = buff[4] & 1

        opt_len = (tmfe + evfe + obfe) * 4

        self.source_service_type = buff[5 + opt_len]
        self.recipient_service_type = buff[6 + opt_len]

    def print_service_layer(self):
        print('Record Length - ', self.record_length)
        print('Record Number - ', self.record_number)
        print('Source Service Type - ', self.source_service_type)
        print('Recipient Service Type', self.recipient_service_type)