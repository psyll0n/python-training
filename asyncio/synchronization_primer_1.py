# Synchronization primer for asyncio
import asyncio

# A shared variable
SHARED_RESOURCE = 0

# An asyncio Lock to synchronize access to a shared resource used by multiple coroutines
lock = asyncio.Lock()


async def modify_shared_resources():
    """
    Sample function that modifies a shared resource safely using an asyncio Lock.
    """
    # Use the lock to ensure exclusive access to the shared resource
    global SHARED_RESOURCE
    async with lock:
        # Critical section starts
        print(f"Current shared resource value: {SHARED_RESOURCE}")
        SHARED_RESOURCE += 1
        await asyncio.sleep(1)  # Simulate some I/O delay
        print(f"Modified shared resource value: {SHARED_RESOURCE}")
        # Critical section ends


async def main():
    """
    Main coroutine to demonstrate synchronization using an asyncio Lock.
    """
    await asyncio.gather(*[modify_shared_resources() for _ in range(5)])


asyncio.run(main())

