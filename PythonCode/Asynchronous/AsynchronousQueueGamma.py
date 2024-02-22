"""
Asynchronous Queue Gamma
~~~~~~~~~~~~~~~~~~~~~~~~

The AsynchronousQueueGamma module provide example(s) for the
`asyncio.Queue` module with class.
"""

import asyncio
from asyncio import (
    Queue,
    TaskGroup
)


class AsynchronousQueueGamma:
    """Asynchronous Queue Gamma Class"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        ...

    def __new__(cls, *args, **kwargs):
        """New"""
        return super().__new__(cls)

    async def fetch_recursive(
        self,
        source_list: list[str],
        maximum_task: int = 10,
    ):
        """Fetch Recursive

        :param source_list: The input `source_list` to fetch
        :type source_list: list[str]
        :param maximum_task: The `maximum_task` to fetch concurrently,
            defaults to 10
        :type maximum_task: int
        """
        print('Fetch Recursive')

        # Create a `query_queue` to store the `source_list` to fetch
        query_queue = Queue()
        # Create a `result_queue` to store the result(s) of the fetch
        result_queue = Queue()

        async with TaskGroup() as group:
            # Create `maximum_task` of `fetch_query` worker task(s)
            # Store them in a `task_list`
            task_list = [
                group.create_task(
                    self.fetch_query(
                        name=f'Worker-{index + 1}',
                        query_queue=query_queue,
                        result_queue=result_queue,
                    )
                ) for index in range(maximum_task)
            ]

            # Enqueue the `source` to the `query_queue`
            for source in source_list:
                await query_queue.put(source)

            # Enqueue a `None` signal for worker(s) to exit
            for _ in range(maximum_task):
                await query_queue.put(None)

        # Consolidate the result(s) from the `result_queue`
        result_list = []
        while not result_queue.empty():
            result = await result_queue.get()
            result_list.append(result)

        # Display the result(s)
        for result in result_list:
            print(f'Result: {result}')

    async def fetch_query(
        self,
        name: str,
        query_queue: Queue,
        result_queue: Queue,
    ):
        """Fetch Query

        :param name: The `name` of the worker
        :type name: str
        :param query_queue: The `query_queue` to fetch
        :type query_queue: Queue
        :param result_queue: The `result_queue` to store the result
        :type result_queue: Queue
        """
        while True:
            query = await query_queue.get()

            # The signal to exit
            if query is None:
                break

            print(f'{name} Fetch Query: {query}')

            # Simulate the work
            await asyncio.sleep(1)

            # Store the result
            result = f'{name} Result: {query}'
            await result_queue.put(result)
