"""
Asynchronous Queue Delta
~~~~~~~~~~~~~~~~~~~~~~~~

The AsynchronousDelta module provide example(s) for the `asyncio.Queue`
module with class. It uses `async with TaskGroup()` for task creation,
along with `asyncio.BoundedSemaphore` as limiter for concurrent task(s).
"""

import asyncio
from asyncio import BoundedSemaphore, Queue, Semaphore, TaskGroup

import tealogger


tealogger.set_level(tealogger.DEBUG)


class AsynchronousDelta:
    """Asynchronous Delta Class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        ...

    def __new__(cls, *args, **kwargs):
        """New"""
        return super().__new__(cls)

    async def fetch_recursive(
        self,
        source_list: list[str],
        # destination_list: list[str],
        maximum_task: int = 10,
    ):
        """Fetch Recursive

        :param source: The source (Remote) path
        :type source_list: list[str]
        :param destination: The destination (Local) path
        :type destination: list[str]
        :param maximum_task: The `maximum_task` to fetch concurrently,
            defaults to 10
        :type maximum_task: int
        """
        tealogger.info('Fetch Recursive')

        limiter = BoundedSemaphore(maximum_task)

        # Create a `result_queue` to store the result(s) of the fetch
        result_queue = Queue()

        async with TaskGroup() as group:
            # Create `maximum_task` of `fetch_query` worker task(s)
            # Store them in a `task_list`
            task_list = [
                group.create_task(
                    self.fetch_query(
                        name=f'Worker-{index + 1}',
                        source=source,
                        result_queue=result_queue,
                        limiter=limiter,
                    )
                ) for index, source in enumerate(source_list)
            ]


    async def fetch_query(
        self,
        name: str,
        source: str,
        result_queue: Queue,
        limiter: Semaphore,
    ):
        """Fetch Query

        :param name: The `name` of the worker
        :type name: str
        :param source: The `source` to fetch
        :type source: str
        :param result_queue: The `result_queue` to store the result
        :type result_queue: Queue
        """
        async with limiter:
            tealogger.debug(f'{name} Source: {source}')

            # Simulate the work
            await asyncio.sleep(3)

            # Store the result
            result = f'{name} Result: {source}'
            await result_queue.put(result)
            tealogger.debug(f'Finished Task: {name}')
