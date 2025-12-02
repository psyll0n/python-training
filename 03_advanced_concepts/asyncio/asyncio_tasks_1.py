# Asynchronous task execution by using coroutines with `asyncio`
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
    Main coroutine to run multiple fetch_data coroutines concurrently.
    """
    # Create multiple tasks to run coroutines concurrently.
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, "\n", result2, "\n", result3)
    
    
asyncio.run(main())