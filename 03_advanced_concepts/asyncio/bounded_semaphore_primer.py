# Comprehensive BoundedSemaphore primer for asyncio
import asyncio
import time
from typing import Optional


async def worker_task(semaphore: asyncio.BoundedSemaphore, worker_id: int, work_duration: float = 1.0):
    """
    Simulates a worker accessing a limited resource with a BoundedSemaphore.
    
    Args:
        semaphore: The BoundedSemaphore controlling access
        worker_id: Unique identifier for this worker
        work_duration: Time to simulate work (seconds)
    """
    timestamp = time.strftime('%H:%M:%S')
    print(f"[{timestamp}] Worker {worker_id}: Requesting access...")
    
    async with semaphore:
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] Worker {worker_id}: ✓ Acquired semaphore, working for {work_duration}s")
        await asyncio.sleep(work_duration)
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] Worker {worker_id}: Completed, releasing semaphore")
    
    timestamp = time.strftime('%H:%M:%S')
    print(f"[{timestamp}] Worker {worker_id}: Done")


async def basic_bounded_semaphore():
    """
    Demonstrates basic BoundedSemaphore usage limiting concurrent access.
    """
    print("=" * 70)
    print("EXAMPLE 1: Basic BoundedSemaphore Usage")
    print("=" * 70)
    print("Limiting 6 workers to 2 concurrent executions\n")
    
    semaphore = asyncio.BoundedSemaphore(2)
    
    # Create 6 workers, but only 2 can run concurrently
    tasks = [worker_task(semaphore, i, work_duration=1.5) for i in range(6)]
    await asyncio.gather(*tasks)
    
    print("\n✓ All workers completed\n")


async def bounded_vs_regular_semaphore():
    """
    Demonstrates the key difference between BoundedSemaphore and regular Semaphore.
    """
    print("=" * 70)
    print("EXAMPLE 2: BoundedSemaphore vs Regular Semaphore")
    print("=" * 70)
    
    # Regular Semaphore allows release() beyond initial value
    regular_sem = asyncio.Semaphore(2)
    print(f"Regular Semaphore initial value: 2")
    
    # You can release without acquiring (dangerous!)
    regular_sem.release()
    regular_sem.release()
    print(f"After 2 extra releases (no acquire): internal counter = 4 (allows 4 concurrent)")
    
    # BoundedSemaphore prevents this
    print(f"\nBoundedSemaphore initial value: 2")
    bounded_sem = asyncio.BoundedSemaphore(2)
    
    try:
        bounded_sem.release()  # This will raise ValueError
        print("Release succeeded (unexpected!)")
    except ValueError as e:
        print(f"✓ Trying to release without acquire raised: {e}")
    
    print("\n✓ BoundedSemaphore protects against accidental over-release\n")


async def database_connection_pool():
    """
    Real-world example: Simulating a database connection pool with limited connections.
    """
    print("=" * 70)
    print("EXAMPLE 3: Database Connection Pool Simulation")
    print("=" * 70)
    print("Pool size: 3 connections | Active queries: 8\n")
    
    # Simulate a DB connection pool with 3 available connections
    connection_pool = asyncio.BoundedSemaphore(3)
    
    async def execute_query(query_id: int, complexity: str = "simple"):
        """Simulates executing a database query."""
        work_time = 1.0 if complexity == "simple" else 2.5
        
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] Query {query_id} ({complexity}): Waiting for DB connection...")
        
        async with connection_pool:
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Query {query_id}: Connected, executing ({work_time}s)...")
            await asyncio.sleep(work_time)
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Query {query_id}: Complete, connection released")
        
        return f"Result_{query_id}"
    
    # Mix of simple and complex queries
    queries = [
        execute_query(0, "simple"),
        execute_query(1, "complex"),
        execute_query(2, "simple"),
        execute_query(3, "simple"),
        execute_query(4, "complex"),
        execute_query(5, "simple"),
        execute_query(6, "simple"),
        execute_query(7, "simple"),
    ]
    
    results = await asyncio.gather(*queries)
    print(f"\n✓ All queries completed: {len(results)} results\n")


async def api_rate_limiting():
    """
    Real-world example: Rate limiting API calls to respect service limits.
    """
    print("=" * 70)
    print("EXAMPLE 4: API Rate Limiting")
    print("=" * 70)
    print("API limit: 5 concurrent requests | Total requests: 10\n")
    
    # Limit to 5 concurrent API calls
    api_semaphore = asyncio.BoundedSemaphore(5)
    
    async def call_api(request_id: int, endpoint: str):
        """Simulates calling an external API."""
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] Request {request_id} to {endpoint}: Queued")
        
        async with api_semaphore:
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Request {request_id} to {endpoint}: Calling API...")
            await asyncio.sleep(1.2)  # Simulate network delay
            timestamp = time.strftime('%H:%M:%S')
            print(f"[{timestamp}] Request {request_id} to {endpoint}: Success")
            return {"request_id": request_id, "status": "success"}
    
    # Create 10 API requests
    endpoints = ["/users", "/posts", "/comments", "/likes", "/shares"]
    requests = [
        call_api(i, endpoints[i % len(endpoints)]) 
        for i in range(10)
    ]
    
    responses = await asyncio.gather(*requests)
    print(f"\n✓ All API calls completed: {len(responses)} responses\n")


async def manual_acquire_release_with_error():
    """
    Demonstrates manual acquire/release with proper error handling.
    """
    print("=" * 70)
    print("EXAMPLE 5: Manual Acquire/Release with Error Handling")
    print("=" * 70)
    
    semaphore = asyncio.BoundedSemaphore(2)
    
    async def risky_operation(task_id: int, should_fail: bool = False):
        """Operation that might fail, demonstrating proper cleanup."""
        print(f"Task {task_id}: Attempting to acquire semaphore...")
        await semaphore.acquire()
        
        try:
            print(f"Task {task_id}: Acquired! Processing...")
            await asyncio.sleep(1)
            
            if should_fail:
                raise Exception(f"Task {task_id} encountered an error!")
            
            print(f"Task {task_id}: Success")
        except Exception as e:
            print(f"Task {task_id}: Error - {e}")
        finally:
            semaphore.release()
            print(f"Task {task_id}: Semaphore released in finally block")
    
    # Run tasks where one will fail
    tasks = [
        risky_operation(0, should_fail=False),
        risky_operation(1, should_fail=True),
        risky_operation(2, should_fail=False),
    ]
    
    await asyncio.gather(*tasks, return_exceptions=True)
    print("\n✓ Even with errors, semaphore was properly released\n")


async def checking_semaphore_state():
    """
    Demonstrates how to check semaphore state and available slots.
    """
    print("=" * 70)
    print("EXAMPLE 6: Monitoring Semaphore State")
    print("=" * 70)
    
    semaphore = asyncio.BoundedSemaphore(3)
    
    print(f"Initial state: {semaphore._value} slots available (max: 3)")
    
    # Acquire some slots
    await semaphore.acquire()
    print(f"After 1 acquire: {semaphore._value} slots available")
    
    await semaphore.acquire()
    print(f"After 2 acquires: {semaphore._value} slots available")
    
    # Check if locked (all slots taken)
    print(f"Is locked? {semaphore.locked()}")
    
    await semaphore.acquire()
    print(f"After 3 acquires: {semaphore._value} slots available")
    print(f"Is locked? {semaphore.locked()}")
    
    # Release one
    semaphore.release()
    print(f"After 1 release: {semaphore._value} slots available")
    print(f"Is locked? {semaphore.locked()}")
    
    # Clean up remaining
    semaphore.release()
    semaphore.release()
    print(f"After all releases: {semaphore._value} slots available\n")


async def main():
    """
    Main function to run all BoundedSemaphore examples.
    """
    examples = [
        basic_bounded_semaphore,
        bounded_vs_regular_semaphore,
        database_connection_pool,
        api_rate_limiting,
        manual_acquire_release_with_error,
        checking_semaphore_state,
    ]
    
    for i, example in enumerate(examples, 1):
        await example()
        if i < len(examples):
            await asyncio.sleep(0.5)  # Brief pause between examples
    
    print("=" * 70)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
