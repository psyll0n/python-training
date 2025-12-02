# Synchronization primer with asyncio 
import asyncio


async def waiter(event):
    """
    Waits for an event to be set.
    """
    print("Waiting for event to be set...")
    await event.wait()
    print("Event has been set!")
    

async def setter(event):
    """
    Sets the event after a delay.
    """
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("Event has been set!")
    
    
async def main():
    """
    Main coroutine to demonstrate synchronization using an asyncio Event.
    """
    event = asyncio.Event()
    
    await asyncio.gather(
        waiter(event),
        setter(event)
    )
    
asyncio.run(main())