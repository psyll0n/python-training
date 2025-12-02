# Use of semaphores in asyncio
import asyncio
import time


async def access_resource(semaphore, resource_id):
    """
    Sample function that accesses a shared, limited resource using an asyncio Semaphore.
    """
    print(f"[{time.strftime('%H:%M:%S')}] Task {resource_id}: Waiting for resource...")
    
    # Acquire the semaphore (blocks if limit reached)
    async with semaphore:
        print(f"[{time.strftime('%H:%M:%S')}] Task {resource_id}: Acquired resource, working...")
        await asyncio.sleep(2)  # Simulate some I/O operation
        print(f"[{time.strftime('%H:%M:%S')}] Task {resource_id}: Releasing resource")
    
    print(f"[{time.strftime('%H:%M:%S')}] Task {resource_id}: Done")


async def access_resource_manual(semaphore, resource_id):
    """
    Alternative approach using manual acquire/release (useful when async with isn't suitable).
    """
    print(f"Task {resource_id}: Requesting access...")
    
    await semaphore.acquire()
    try:
        print(f"Task {resource_id}: Got access, processing...")
        await asyncio.sleep(2)
    finally:
        semaphore.release()
        print(f"Task {resource_id}: Released")


async def main():
    """
    Main coroutine to demonstrate synchronization using an asyncio Semaphore.
    """
    print("=== Semaphore Example (limit: 2 concurrent tasks) ===\n")
    
    # Create a semaphore that allows 2 concurrent accesses
    semaphore = asyncio.Semaphore(2)
    
    # Launch 5 tasks - only 2 will run concurrently
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))
    
    print("\n=== Alternative: Manual acquire/release ===\n")
    semaphore2 = asyncio.Semaphore(3)
    await asyncio.gather(*(access_resource_manual(semaphore2, i) for i in range(6)))


if __name__ == "__main__":
    asyncio.run(main())
