klk_data_string_dict = {
    "0": "01010106A2500BCB0000FFFF1101",
    "1": "0101010569170B7F000438803FDC"
}

def decode_klk_data(klk_data):
    uint8_t = 2
    uint16_t = 4

    klk_data_structure_dict = {
        "protocol_type": uint8_t,
        "device_type": uint8_t,
        "software_version": uint16_t,
        "param_crc": uint16_t,
        "vbat_mv": uint16_t,
        "nb_entry": uint16_t,
        "oldest_entry": uint16_t,
        "cur_time": uint16_t
    }

    decoded_klk_data = []
    start = 0
    end = 0
    for x in klk_data_structure_dict:
        end += klk_data_structure_dict[x]
        hexbytes = klk_data[start:end]
        
        if x == "param_crc":
            if hexbytes == "A250":
                value = "STORAGE"
            elif hexbytes == "CFEC":
                value = "NOMINAL"
            else:
                value = hexbytes
        elif x == "software_version":
            value = "{}.{}".format(hexbytes[0:2], hexbytes[2:4])
        else:
            value = str(int(hexbytes, 16))

        decoded_klk_data.append("{}:{}".format(x, value))
        start = end

    return '\n'.join(decoded_klk_data)

for y in klk_data_string_dict:
	print(decode_klk_data(klk_data_string_dict[y]))