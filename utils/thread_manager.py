import threading


def thread_manager(threads, flooder, ip, port, packets):
    for i in range(threads):
        th = threading.Thread(target=flooder, daemon=True, args=(i, ip, port, packets))
        th.start()
