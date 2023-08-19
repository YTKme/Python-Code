"""
Run With Timeout
~~~~~~~~~~~~~~~~
"""

from queue import Queue
import random
import shlex
import subprocess
import threading
import time


def fuzz(is_fuzz: bool = False):
    """Random Fuzz

    Fuzz(ing) is an automated software testing technique that involves
    providing invalid, unexpected, or random data as inputs to a
    computer program.

    Fuzz(ing) is also a technique for amplifying race condition errors
    to make them more visible.

    :param is_fuzz: (bool) Whether or not to enable fuzzing (sleep for a
        random amount of time), defaults to `False`
    """
    if is_fuzz:
        time.sleep(random.random())


def queue_line(data, print_queue):
    """Queue line.

    Iterate over the `data` and enqueue each item into the `print_queue`
    for printing.
    """
    for line in iter(data.readline, ''):
        print_queue.put(line)
    data.close()


def print_manager(print_queue):
    """Print manager.

    The print manager have 'exclusive' right to call print

    :param print_queue: (Queue) queue of line(s) to print
    """
    while True:
        line = print_queue.get()
        print(line)
        # Inform `print_queue` that the job is done
        print_queue.task_done()


def run_with_timeout(
    command: str | list,
    timeout: int | float,
    ):
    """Run a `command` with a `timeout` defined.

    :param command: (str | list) command passed to subprocess
    :param timeout: (int | float) seconds after which the process is
        killed and values returned
    """

    # Print the `full_command` for copy and paste reproducibility
    full_command = shlex.join(command) if isinstance(command, list) else command
    print(f'Full Command: {full_command}')

    # Convert command to `list` if needed
    if not isinstance(command, list):
        command = shlex.split(command)

    # Create the process
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        text=True,
        )
    
    process.timed_out = False
    process.output_buffer = ''

    print_queue = Queue()
    print_thread = threading.Thread(target=print_manager, args=(print_queue,))
    print_thread.daemon = True
    print_thread.start()
    del print_thread

    worker_thread = threading.Thread(target=queue_line, args=(process.stdout, print_queue,))
    worker_thread.start()

    try:
        print_queue.put('In Try')
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        print_queue.put('In Except')
        process.timed_out = True
        process.kill()
    finally:
        worker_thread.join()
        print_queue.put('In Finally')
        print_queue.join()
