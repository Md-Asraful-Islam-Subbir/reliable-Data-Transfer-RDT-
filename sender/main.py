# sender/main.py
import socket
import struct
import random
from common import create_packet, extract_packet, is_corrupt

def send_packet(sock, packet, addr):
    if random.random() < 0.2:  # Simulate 20% packet loss
        print(f"Packet lost: {extract_packet(packet)[0]}")
    else:
        sock.sendto(packet, addr)
        print(f"Sent packet: {extract_packet(packet)[0]}")

def main():
    sender_port = 12345
    receiver_port = 12346
    receiver_addr = ('localhost', receiver_port)

    sender_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender_sock.bind(('localhost', sender_port))

    seq_num = 0

    while True:
        data = input("Enter data to send (or 'exit' to quit): ")
        if data.lower() == 'exit':
            break

        packet = create_packet(seq_num, data)
        send_packet(sender_sock, packet, receiver_addr)
        seq_num = 1 - seq_num  # Toggle sequence number

    sender_sock.close()

if __name__ == "__main__":
    main()
