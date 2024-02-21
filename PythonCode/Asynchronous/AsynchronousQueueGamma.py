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
        maximum_connection: int = 10,
    ):
        """Fetch Recursive"""
        print('Fetch Recursive')
        query_queue = Queue()

        for source in source_list:
            query_queue.put_nowait(source)

        task_list = []
        for _ in range(maximum_connection):
            task = asyncio.create_task(self.fetch_query(queue=query_queue))
            task_list.append(task)
            task.add_done_callback(task_list.remove)

        await query_queue.join()

        for task in task_list:
            task.cancel()

        await asyncio.gather(*task_list, return_exceptions=True)

    async def fetch_query(
        self,
        queue: Queue,
    ):
        """Fetch Query"""
        while True:
            query = await queue.get()
            print(f'Query: {query}')
            queue.task_done()
