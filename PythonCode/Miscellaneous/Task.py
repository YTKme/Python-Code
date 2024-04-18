import time

from rich.progress import Progress

with Progress() as progress:
    task = progress.add_task(
        description='Test',
        start=False,
    )
    print(f'A: {progress.finished}')
