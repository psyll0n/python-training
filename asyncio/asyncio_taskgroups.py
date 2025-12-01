# Asynchronous task execution by using coroutines with `asyncio` and Task Groups
import asyncio


async def fetch_data(id, sleep_time):
    """Fetch data asynchronously after a delay.

    Args:
        id (int): Identifier for the coroutine.
        sleep_time (int): Time in seconds to simulate data fetching delay.
    Returns:
        dict: A dictionary containing the id and fetched data.
    """
    print(f"Coroutine {id} starting to fetch data...")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Data from coroutine {id}"}


async def main():
    """
    Main coroutine to run multiple fetch_data coroutines concurrently using TaskGroup.
    
    Note: TaskGroup provides built-in error handling compared to `fetch_data` and `gather`.
    
    The `async with` is known as a context manager that ensures proper setup and teardown of resources.
    """
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 3, 1], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    
    # After the TaskGroup context, all tasks are complete.
    results = [task.result() for task in tasks]
    
    for result in results:
        print(f"Received result: {result}")
    
    
asyncio.run(main())