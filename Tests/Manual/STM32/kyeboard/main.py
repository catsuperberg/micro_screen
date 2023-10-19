from micro_screen.keyboard import KeyboardFactory 
from micro_screen.keyboard import Keyboard
import uasyncio

factory = KeyboardFactory()
keyboard: Keyboard = factory.create()

async def poll_keyboard():
    while True:
        result = keyboard.pending_event()
        if result != None:
            print(result)
        await uasyncio.sleep(0.02)
                
loop = uasyncio.new_event_loop()
loop.run_until_complete(poll_keyboard())
