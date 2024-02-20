"""
Asynchronous Queue
~~~~~~~~~~~~~~~~~~

The AsynchronousQueue module provide example(s) for the `asyncio.Queue`
module.
"""

import asyncio
import time


async def worker(
    name: str,
    queue: asyncio.Queue
) -> None:
    """Worker

    :param name: The name for the worker
    :type name: str
    :param queue: The input queue to execute
    :type queue: asyncio.Queue
    """
    while True:
        # Get a work item out of the queue.
        sleep_time = await queue.get()

        # Execute the work item.
        await asyncio.sleep(sleep_time)

        # Notify the queue that the work item has been completed.
        queue.task_done()

        # Display the worker name and sleep time.
        print(f'Worker {name} has executed for {sleep_time} second(s).')


async def main():
    """Main"""
    # Create an (asynchronous) queue to store the work item(s).
    queue_size = 10
    queue = asyncio.Queue(queue_size)

    # Create sleep timer and put them into the queue.
    sleep_time = 5.0
    for i in range(queue_size):
        queue.put_nowait(sleep_time)

    # Create a task list to process the queue concurrently.
    task_size = 5
    task_list = []
    for i in range(task_size):
        task = asyncio.create_task(worker(f'Worker-{i}', queue))
        task_list.append(task)

    # Wait until the queue is fully processed.
    start_time = time.monotonic()
    await queue.join()
    total_execute_time = time.monotonic() - start_time

    # Cancel the worker task(s).
    for task in task_list:
        task.cancel()
    # Wait until the worker task(s) are cancelled.
    await asyncio.gather(*task_list, return_exceptions=True)

    # Display the total execute time.
    print(f'------')
    print(f'Task Size: {task_size}, Execute Time: {total_execute_time:.2f} second(s).')
    print(f'Expect Time: {((sleep_time * queue_size) / task_size):.2f} second(s).')


if __name__ == '__main__':
    asyncio.run(main())
