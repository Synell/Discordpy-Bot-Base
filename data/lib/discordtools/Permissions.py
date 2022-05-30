#----------------------------------------------------------------------

    # Libraries
import discord
from enum import Enum
#----------------------------------------------------------------------

    # Class
class Permissions(Enum): pass

class Permissions(Enum):
    AddReactions = 'add_reactions'
    Administrator = 'administrator'
    AttachFiles = 'attach_files'
    BanMembers = 'ban_members'
    ChangeNickname = 'change_nickname'
    Connect = 'connect'
    CreateInstantInvite = 'create_instant_invite'
    CreatePrivateThreads = 'create_private_threads'
    Create_public_threads = 'create_public_threads'
    DeafenMembers = 'deafen_members'
    EmbedLinks = 'embed_links'
    ExternalEmojis = 'external_emojis'
    ExternalStickers = 'external_stickers'
    KickMembers = 'kick_members'
    ManageChannels = 'manage_channels'
    ManageEmojis = 'manage_emojis'
    ManageEmojisAndStickers = 'manage_emojis_and_stickers'
    ManageEvents = 'manage_events'
    ManageGuild = 'manage_guild'
    ManageMessages = 'manage_messages'
    ManageNicknames = 'manage_nicknames'
    ManagePermissions = 'manage_permissions'
    ManageRoles = 'manage_roles'
    ManageThreads = 'manage_threads'
    ManageWebhooks = 'manage_webhooks'
    MentionEveryone = 'mention_everyone'
    ModerateMembers = 'moderate_members'
    MoveMembers = 'move_members'
    MuteMembers = 'mute_members'
    PrioritySpeaker = 'priority_speaker'
    ReadMessageHistory = 'read_message_history'
    ReadMessages = 'read_messages'
    RequestToSpeak = 'request_to_speak'
    SendMessages = 'send_messages'
    SendMessagesInThreads = 'send_messages_in_threads'
    SendTTSMessages = 'send_tts_messages'
    Speak = 'speak'
    Stream = 'stream'
    UseEmbeddedActivities = 'use_embedded_activities'
    UseExternalEmojis = 'use_external_emojis'
    UseExternalStickers = 'use_external_stickers'
    UseSlashCommands = 'use_slash_commands'
    UseVoiceActivation = 'use_voice_activation'
    Value = 'value'
    ViewAuditLog = 'view_audit_log'
    ViewChannel = 'view_channel'
    ViewGuildInsights = 'view_guild_insights'



    def __convert_perm_list__(perm_list: list[Permissions]) -> list[int]:
        if type(perm_list) == list:
            if perm_list:
                if type(perm_list[0]) is Permissions: perm_list = [perm.value for perm in perm_list]

                elif type(perm_list[0]) is str: pass

                else: raise TypeError('Permissions must be discord.Permissions, a list of Permissions or a list of strings')

        elif type(perm_list) == discord.Permissions: perm_list = [perm[0] for perm in perm_list if perm[1]]

        elif type(perm_list) == discord.PermissionOverwrite: perm_list = [perm[0] for perm in perm_list if perm[1]]

        else: raise TypeError('Permissions must be discord.Permissions, discord.PermissionOverwrite, a list of Permissions or a list of strings')

        return perm_list



    def create(*permissions: Permissions, overwrite: bool = False) -> discord.PermissionOverwrite:
        if overwrite:
            perms = discord.PermissionOverwrite()
        else:
            perms = discord.Permissions()

        permDict = {}

        permissions = Permissions.__convert_perm_list__(list(permissions))

        for perm in permissions:
            permDict[perm] = True

        perms.update(**permDict)

        return perms



    def has_required(permissions: discord.Permissions|discord.PermissionOverwrite|list[Permissions]|list[str], required_permissions: discord.Permissions|discord.PermissionOverwrite|list[Permissions]|list[str]) -> bool:
        permissions = Permissions.__convert_perm_list__(permissions)
        required_permissions = Permissions.__convert_perm_list__(required_permissions)

        for perm in required_permissions:
            if perm not in permissions:
                return False
        return True
#----------------------------------------------------------------------
