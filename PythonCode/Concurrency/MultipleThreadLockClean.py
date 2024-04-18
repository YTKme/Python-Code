"""
Multiple Thread Base
~~~~~~~~~~~~~~~~~~~~
"""

import queue
import threading

from Concurrency import fuzz


counter_lock = threading.Lock()
printer_lock = threading.Lock()

counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter
    with counter_lock:
        counter += 1
        with printer_lock:
            print(f'The count is {counter}')
            print(f'---------------')


with printer_lock:
    print('Starting Up')


worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()

for t in worker_threads:
    t.join()


with printer_lock:
    print('Finishing Up')


if __name__ == '__main__':
    pass
