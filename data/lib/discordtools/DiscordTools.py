#----------------------------------------------------------------------

    # Libraries
import discord, time, asyncio, random
from typing import Callable
#----------------------------------------------------------------------

    # Class
class DiscordTools:
    def __new__(cls) -> None:
        return None



    async def timed_embed(message: discord.Message, timeout: int, condition: Callable[[], bool], embed: Callable[[int], discord.Embed]) -> None:
        timer = time.time()

        while condition() and timeout >= 0:
            await asyncio.sleep(1)

            timeout -= time.time() - timer
            timer = time.time()

            await message.edit(embed = embed(timeout))



    def zalgo(string, addsPerChar):
        result = ''

        for char in string:
            for _ in range(0, addsPerChar):
                randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += randBytes.decode('utf-16be')

            result += char

        return result
#----------------------------------------------------------------------
