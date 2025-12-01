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
    Run coroutines concurrently and gather their return values by using a `gather` function 
    and `fetch_data`. The `gather` function allows multiple coroutines to be created and run. The
    results are stored in the `results` list
    """
    results = await asyncio.gather(
        # Note that the `gather` function is not so good for error handling.
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )
    
    for result in results:
        print(f"Received result: {result}")
    
    
asyncio.run(main())