# common.py
import struct

def checksum(data):
    return sum(map(ord, data))

def create_packet(seq_num, data):
    chk = checksum(data)
    return struct.pack('!HH{}s'.format(len(data)), seq_num, chk, data.encode())

def extract_packet(packet):
    seq_num, chk, data = struct.unpack('!HH{}s'.format(len(packet) - 4), packet)
    return seq_num, chk, data.decode()

def is_corrupt(packet):
    seq_num, chk, data = extract_packet(packet)
    return chk != checksum(data)
