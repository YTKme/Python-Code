"""
Multiple Thread Alpha
~~~~~~~~~~~~~~~~~~~~~
"""

import threading


counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print(f'The count is {counter}')
    print(f'---------------')


print('Starting Up')

for i in range(10):
    threading.Thread(target=worker).start()

print('Finishing Up')


if __name__ == '__main__':
    pass
