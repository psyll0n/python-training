# Future primer for asyncio
import asyncio


async def set_future_result(future, value):
    """
    Sample function that sets the result of a given Future after a delay.
    When using this function, ensure that the Future results are awaited for retrieval.
    """
    
    await asyncio.sleep(2)  # Simulate some asynchronous operation
    future.set_result(value)
    print(f"Set the future result to: {value}")
    
    
async def main():
    """
    Main coroutine to demonstrate the use of Future objects in asyncio.
    """
    # Create a Future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    # Schedule the set_future_result coroutine to run concurrently
    asyncio.create_task(set_future_result(future, "Future result is ready!"))
    
    print("Waiting for the future result...")
    
    # Await for the future's result
    result = await future
    print(f"Received future result: {result}")