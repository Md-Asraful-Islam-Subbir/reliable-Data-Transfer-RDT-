# receiver/main.py
import socket
import struct
from common import extract_packet, is_corrupt

def receive_packet(sock):
    packet, addr = sock.recvfrom(1024)
    print(f"Received packet: {extract_packet(packet)[0]}")
    return packet, addr

def send_ack(sock, seq_num, addr):
    ack_packet = struct.pack('!HH', seq_num, 0)
    sock.sendto(ack_packet, addr)
    print(f"Sent ACK: {seq_num}")

def main():
    sender_port = 12345
    receiver_port = 12346

    receiver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_sock.bind(('localhost', receiver_port))

    seq_num = 0

    while True:
        packet, addr = receive_packet(receiver_sock)

        if not is_corrupt(packet):
            seq_num, _, data = extract_packet(packet)
            print(f"Sender's message: {data}")
            send_ack(receiver_sock, seq_num, addr)
        else:
            print("Received corrupt packet. Ignoring.")

    receiver_sock.close()

if __name__ == "__main__":
    main()
