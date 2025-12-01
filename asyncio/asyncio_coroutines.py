# Asynchronous execution by using coroutines with `asyncio`
import asyncio


# Define a coroutine that simulates an asynchronous, time-consuming task
async def fetch_data(delay, id):
    """Simulate fetching data asynchronously with a delay.

    Args:
        delay (int): The number of seconds to wait before returning data.

    Returns:
        dict: A dictionary containing the fetched data.
    """
    print(f"Fetching data for task with id: {id}...")
    await asyncio.sleep(delay)  # Simulate a network or I/O operation with a delay.
    print("Data fetched, id:", id)
    
    return {"data": "Sample data", "id": id } # Return some sample data


# Define a another coroutine function that calls the first coroutine.
async def main():
    """
    Main coroutine that demonstrates running multiple asynchronous tasks concurrently.
    """
    print("Start of the main coroutine")
    task1 = fetch_data(2, 1)  # Call the fetch_data coroutine with id 1 with a 2-second delay
    task2 = fetch_data(3, 2)  # Call the fetch_data coroutine with id 2 with a 3-second delay
    print("End of the main coroutine")
    
    # Await the result of the fetch_data coroutine for task1
    result1 = await task1
    print(f"Received result: {result1}")
    
    # Await the result of the fetch_data coroutine for task2
    result2 = await task2
    print(f"Received result: {result2}")

# Run the main coroutine
asyncio.run(main())
