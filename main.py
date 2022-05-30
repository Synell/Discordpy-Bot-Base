#----------------------------------------------------------------------

    # Libraries
import discord, os, sys, json, traceback
from discord_components import DiscordComponents
from data.lib import *
#----------------------------------------------------------------------

    # Config Class
class Config:
    def __init__(self) -> None:
        with open('./config/data.json', encoding = 'utf8') as infile:
            data = json.load(infile)
            self.prefix = data['client']['prefix']
            self.token = data['client']['token']
#----------------------------------------------------------------------

    # Set Up
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

client = discord.Client(intents = intents)
client.commands = []
client.config = Config()
#----------------------------------------------------------------------

    # Events & Utils
@client.event
async def on_ready():
    load_commands()
    load_ready()
    DiscordComponents(client)

def load_ready() -> None:
    Console.log('Connecté en tant que ' + client.user.display_name + '#' + client.user.discriminator)

    count = 0
    for guild in client.guilds:
        count += guild.member_count - 1

    Console.log(f'Prêt sur {len(client.guilds)} serveurs pour un total de {count} utilisateurs')

def load_commands() -> None:
    Console.log('Chargement des commandes...')
    for folder in os.listdir(f'./commands/'):
        if not os.path.isdir(f'./commands/{folder}/'): continue
        sys.path.insert(0, f'./commands/{folder}/')
        for file in os.listdir(f'./commands/{folder}/'):
            if file.endswith('.py'):
                extension = file[:-3]
                try:
                    imported_module = __import__(f'{extension}')
                    client.commands.append(imported_module.Command())
                    client.commands[-1].path = f'./commands/{folder}/'
                    Console.success(f'-> Commande chargée: {extension}')
                except Exception as e:
                    Console.error(f'-> Echec du chargement de la commande {extension}\n{traceback.format_exc()}')
        sys.path.pop(0)

@client.event
async def on_message(message: discord.Message):
    if str(message.content).startswith(client.config.prefix) and (not message.author.bot):
        args = str(message.content).split(' ')
        command = args.pop(0)[1:]
        cmd = find_command(command)
        if cmd:
            if can_exec_command(message, cmd):
                try:
                    await cmd.execute(client, message, args)
                except Exception as e:
                    Console.error(f'-> Echec de l\'execution de la commande {cmd.name}\n{traceback.format_exc()}')

def find_command(name: str) -> BaseCommand:
    for cmd in client.commands:
        if (cmd.name == name) or (name in cmd.aliases):
            return cmd

def can_exec_command(message: discord.Message, cmd: BaseCommand):
    if isinstance(message.channel, discord.channel.DMChannel):
        #return ((not cmd.requiredPermissions) and ((not cmd.allowed_users) or (message.author.id in cmd.allowed_users))) or (message.author.id in cmd.admin_users)
        return False
    return (has_command_permissions(message, cmd) and has_command_allowed(message, cmd)) or has_command_admin(message, cmd)

def has_command_permissions(message: discord.Message, cmd: BaseCommand):
    if Permissions.has_required(message.author.guild_permissions, cmd.required_permissions): return True

def has_command_admin(message: discord.Message, cmd: BaseCommand):
    return message.author.id in cmd.admin_users

def has_command_allowed(message: discord.Message, cmd: BaseCommand):
    if len(cmd.allowed_users) == 0: return True
    return message.author.id in cmd.allowed_users



def get_server_users(server: discord.Guild, allow_bots = False) -> list[discord.User]:
    return [member for member in server.members if allow_bots or not member.bot]

def get_channel_users(channel: discord.TextChannel, allow_bots = False) -> list[discord.User]:
    return [member for member in channel.members if allow_bots or not member.bot]
#----------------------------------------------------------------------

    # Bind
client.find_command = find_command
client.has_command_permissions = has_command_permissions
client.has_command_admin = has_command_admin
client.has_command_allowed = has_command_allowed
client.can_exec_command = can_exec_command

client.get_server_users = get_server_users
client.get_channel_users = get_channel_users
#----------------------------------------------------------------------

    # Run
client.run(client.config.token)
#----------------------------------------------------------------------
