#----------------------------------------------------------------------

    # Libraries
import discord
import sys
from data.lib.discordtools import BaseCommand
from data.lib.debug import Console
#----------------------------------------------------------------------

    # Class
class Command(BaseCommand):
    name = 'help'
    aliases = ['h']
    category = 'Info'
    utilisation = '{prefix}help [command]'

    async def execute(self, client: discord.Client, message: discord.Message, args: list[str]) -> None:
        if args:
            if args[0] == 'syntax':
                embed = discord.Embed(
                    title = 'Aide - Syntaxe',
                    description = '',
                    color = client.config.embed.color
                )
                embed.set_footer(text = client.config.embed.footer)

                syntax_dict = {
                    'texte': '**Entrer littéralement le texte**, exactement comme indiqué',
                    '<argument>': 'Un **argument** qui doit être remplacé par la valeur appropriée',
                    '[argument]': 'Un argument facultatif',
                    '(argument|argument)': '(Requis) **Choisir** un des arguments proposés',
                    '[argument|argument]': '(Facultatif) **Choisir** un des arguments proposés',
                    'commande ...': 'Une autre **sous-commande** est requise'
                }
                syntax_keys = list(syntax_dict.keys())

                embed.add_field(
                    name = 'Syntaxe',
                    value = f'`{syntax_keys[0]}`',
                    inline = True
                )
                embed.add_field(
                    name = 'Signification',
                    value = f'{syntax_dict[syntax_keys.pop(0)]}',
                    inline = True
                )
                embed.add_field(
                    name = '\u200b',
                    value = '\u200b',
                    inline = True
                )

                while syntax_keys:
                    embed.add_field(
                        name = '\u200b',
                        value = f'`{syntax_keys[0]}`',
                        inline = True
                    )
                    embed.add_field(
                        name = '\u200b',
                        value = syntax_dict[syntax_keys.pop(0)],
                        inline = True
                    )
                    embed.add_field(
                        name = '\u200b',
                        value = '\u200b',
                        inline = True
                    )

                return await message.channel.send(embed = embed)

            cmdPath = args[0]
            cmd = client.find_command(args.pop(0))
            if cmd:
                while args and cmd:
                    cmdPath += f' -> {args[0]}'
                    cmd = cmd.find_command(args.pop(0))

                if cmd:
                    embed = discord.Embed(
                        title = f'Aide - {cmdPath}',
                        description = '',
                        color = client.config.embed.color
                    )
                    embed.set_footer(text = client.config.embed.footer)
                    embed.add_field(
                        name = 'Nom',
                        value = cmd.name,
                        inline = True
                    )
                    embed.add_field(
                        name = 'Aliases',
                        value = self.stringAliases(cmd),
                        inline = True
                    )
                    embed.add_field(
                        name = 'Catégorie',
                        value = cmd.category,
                        inline = True
                    )
                    embed.add_field(
                        name = 'Utilisation',
                        value = cmd.utilisation.replace('{prefix}', client.config.prefix),
                        inline = False
                    )
                    embed.add_field(
                        name = 'Accès',
                        value = self.stringAccess(cmd),
                        inline = True
                    )
                    embed.add_field(
                        name = 'Permissions requises',
                        value = self.stringPermissions(cmd),
                        inline = True
                    )

                    return await message.channel.send(embed = embed)
            return await message.channel.send(f'Cette commande n\'est pas reconnue: {cmdPath}')


        command_list = {}
        for cmd in client.commands:
            if cmd.category not in command_list:
                command_list[cmd.category] = []
            command_list[cmd.category].append(cmd)

        embed = discord.Embed(
            title = 'Aide - Liste des commandes',
            description = f'`{client.config.prefix}help [command]` pour plus d\'informations\n`{client.config.prefix}help syntax` pour la syntaxe des commandes',
            color = client.config.embed.color
        )
        embed.set_footer(text = client.config.embed.footer)

        for category in command_list:
            embed.add_field(
                name = category,
                value = '\n'.join(f'{cmd.name}' for cmd in command_list[category]),
                inline = True
            )

        return await message.channel.send(embed = embed)
    
    def find_command(self, client: discord.Client, name: str) -> BaseCommand:
        for cmd in client.commands:
            if (cmd.name == name) or (name in cmd.aliases):
                return cmd

    def stringAliases(self, cmd: BaseCommand) -> str:
        if not cmd.aliases:
            return '-'
        return '\n'.join(cmd.aliases)

    def stringAccess(self, cmd: BaseCommand) -> str:
        if not cmd.allowed_users:
            if not cmd.admin_users:
                return 'Tout le monde'
            return 'Utilisateurs administrateurs'
        if not cmd.admin_users:
            return 'Utilisateurs autorisés'
        return 'Utilisateurs autorisés et administrateurs'

    def stringPermissions(self, cmd: BaseCommand) -> str:
        if not cmd.required_permissions:
            return 'Aucune'
        return '\n'.join(cmd.required_permissions)
#----------------------------------------------------------------------
