"""
Multiple Thread Base
~~~~~~~~~~~~~~~~~~~~
"""

import threading

from Concurrency import fuzz

counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter

    fuzz()
    old_counter = counter
    fuzz()
    counter = old_counter + 1
    fuzz()
    print(f'The count is {counter}', end='')
    fuzz()
    print()
    print(f'---------------', end='')
    fuzz()
    print()
    fuzz()


print('Starting Up')

for i in range(10):
    threading.Thread(target=worker).start()
    fuzz()

print('Finishing Up')


if __name__ == '__main__':
    pass
