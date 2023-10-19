import _module_finder

from micro_screen.keyboard import Keyboard, KeyboardFactory 
import asyncio

factory = KeyboardFactory()
keyboard: Keyboard = factory.create()

async def poll_keyboard():
    while True:
        result = keyboard.pending_event()
        if result != None:
            print(result)
        await asyncio.sleep(0.02)
                
loop = asyncio.new_event_loop()
loop.run_until_complete(poll_keyboard())
