#----------------------------------------------------------------------

    # Libraries
import discord
import sys
from data.lib.discordtools import BaseCommand
from data.lib.debug import Console
#----------------------------------------------------------------------

    # Class
class Command(BaseCommand):
    name = 'reload'
    aliases = ['rl']
    category = 'Core'
    utilisation = '{prefix}reload <bot command>'
    admin_users = ['399266992236003358', '690181493880127745', '422102938622885891']

    async def execute(self, client: discord.Client, message: discord.Message, args: list[str]) -> None:
        for arg in args:
            cmd = self.find_command(client, arg)
            if cmd:
                try:
                    sys.path.insert(0, cmd.__path__)
                    importedModule = __import__(f'{cmd.name}')
                    client.commands.append(importedModule.Command())
                    client.commands[-1].path = cmd.__path__
                    sys.path.remove(cmd.__path__)

                    client.commands.remove(cmd)

                    Console.success(f'-> Commande rechargée avec succès: {cmd.name}')
                    await message.channel.send(f'Commande rechargée avec succès: {cmd.name}')

                except Exception as e:
                    exception = f'{type(e).__name__}: {e}'
                    Console.error(f'-> Echec du rechargement de la commande {cmd.name}\n{exception}')
                    await message.channel.send(f'Echec du rechargement de la commande: {cmd.name}\n{exception}')

            else:
                Console.error(f'-> Cette commande n\'est pas reconnue: {cmd.name}')
                await message.channel.send(f'Cette commande n\'est pas reconnue: {cmd.name}')
    
    def find_command(self, client: discord.Client, name: str) -> BaseCommand:
        for cmd in client.commands:
            if (cmd.name == name) or (name in cmd.aliases):
                return cmd
#----------------------------------------------------------------------
