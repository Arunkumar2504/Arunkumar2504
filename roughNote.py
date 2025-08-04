import threading


def task():
    print("Running in thread")


t = threading.Thread(target=task)
t.start()
t.join()
