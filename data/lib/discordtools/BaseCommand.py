#----------------------------------------------------------------------

    # Libraries
from data.lib.debug import Console
import discord, sys, os, traceback
#----------------------------------------------------------------------

    # Class
class BaseCommand: pass

class BaseCommand:
    name: str = 'command'
    aliases: list[str] = []
    category: str = 'None'
    utilisation: str = '{prefix}command'
    allowed_users: list[str] = []
    admin_users: list[str] = []
    required_permissions: list[str] = []
    __path__: str = ''

    def __init__(self) -> None:
        self.subcommands: list[BaseCommand] = []

    async def execute(self, client: discord.Client, message: discord.Message, args: list[str]) -> None: pass

    def load_commands(self, path: str = '') -> None:
        Console.log(f'Chargement des sous-commandes de {self.name}...')
        sys.path.insert(0, f'{path}')
        for file in os.listdir(f'{path}'):
            if file.endswith('.py'):
                extension = file[:-3]
                try:
                    imported_module = __import__(f'{extension}')
                    self.subcommands.append(imported_module.Command())
                    self.subcommands[-1].path = f'{path}'
                    sys.modules.pop(imported_module.__name__)
                    Console.success(f'-> Sous-commande de {self.name} chargée: {extension}')
                except Exception as e:
                    Console.error(f'-> Echec du chargement de la sous-commande de {self.name} {extension}\n{traceback.format_exc()}')
        sys.path.pop(0)

    async def exec_sub_command(self, client: discord.Client, message: discord.Message, args: list[str]):
        for subcommand in self.subcommands:
            if subcommand.name == args[0] or args[0] in subcommand.aliases:
                if client.can_exec_command(message, subcommand):
                    args.pop(0)
                    await subcommand.execute(client, message, args)
                return

    def find_command(self, name: str) -> BaseCommand:
        for cmd in self.subcommands:
            if (cmd.name == name) or (name in cmd.aliases):
                return cmd
#----------------------------------------------------------------------
