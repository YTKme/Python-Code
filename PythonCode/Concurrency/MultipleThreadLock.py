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
        old_counter = counter
        fuzz()
        counter = old_counter + 1
        fuzz()
        with printer_lock:
            print(f'The count is {counter}', end='')
            fuzz()
            print()
            fuzz()
            print(f'---------------', end='')
            fuzz()
            print()
        fuzz()


with printer_lock:
    print('Starting Up', end='')
    fuzz()
    print()
fuzz()


worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
    fuzz()

for t in worker_threads:
    t.join()
    fuzz()


with printer_lock:
    print('Finishing Up', end='')
    fuzz()
    print()


fuzz()


if __name__ == '__main__':
    pass
