"""
Multiple Thread Base
~~~~~~~~~~~~~~~~~~~~
"""

import queue
import threading

from Concurrency import fuzz

counter = 0

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


print_queue.put(['Starting Up'])

for i in range(10):
    print_queue.put([f'Printing: {i}'])
    fuzz()


print_queue.put(['Finishing Up'])
print_queue.join()


if __name__ == '__main__':
    pass
