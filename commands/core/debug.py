#----------------------------------------------------------------------

    # Libraries
import discord
from data.lib.discordtools import BaseCommand
#----------------------------------------------------------------------

    # Class
class Command(BaseCommand):
    name = 'debug'
    aliases = ['dbg']
    category = 'Core'
    utilisation = '{prefix}debug <python command>'
    admin_users = ['399266992236003358', '690181493880127745', '422102938622885891']

    async def execute(self, client: discord.Client, message: discord.Message, args: list[str]) -> None:
        command_args = ' '.join(args)
        await message.channel.send(f'**Console:**\n\\>\\>\\> `{command_args}`\n~~--------------------------------------------------~~')

        for msg in self.split_message(str(eval(' '.join(args)))):
            await message.channel.send(f'```py\n{msg}\n```')
    
    def split_message(self, msg: str) -> list[str]:
        msg_lst = msg.split(' ')
        new_msg_lst = []
        s = msg_lst.pop(0)
        while msg_lst:
            if len(s + ' ' + msg_lst[0]) < 1950:
                s += ' ' + msg_lst.pop(0)
            else:
                new_msg_lst.append(s)
                s = msg_lst.pop(0)
        if s:
            new_msg_lst.append(s)
        
        return new_msg_lst
#----------------------------------------------------------------------
