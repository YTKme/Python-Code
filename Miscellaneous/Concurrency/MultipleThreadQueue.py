"""
Multiple Thread Base
~~~~~~~~~~~~~~~~~~~~
"""

import queue
import threading

from Concurrency import fuzz

counter = 0

counter_queue = queue.Queue()


def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get()
        fuzz()
        old_counter = counter
        fuzz()
        counter = old_counter + increment
        fuzz()
        print_queue.put([
            f'The counter is {counter}',
            f'-----------------'
            ])
        fuzz()
        counter_queue.task_done()


t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t


print_queue = queue.Queue()


def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()
        fuzz()
        for line in job:
            print(line, end='')
            fuzz()
            print()
            fuzz()
        print_queue.task_done()
        fuzz()


t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t


def worker():
    'My job is to increment the counter and print the current counter'
    counter_queue.put(1)
    fuzz()


print_queue.put(['Starting Up'])
fuzz()

worker_threads = []

for i in range(10):
    t = threading.Thread(target=worker)
    worker_threads.append(t)
    t.start()
    fuzz()

for t in worker_threads:
    fuzz()
    t.join()


counter_queue.join()
fuzz()
print_queue.put(['Finishing Up'])
fuzz()
print_queue.join()
fuzz()


if __name__ == '__main__':
    pass
