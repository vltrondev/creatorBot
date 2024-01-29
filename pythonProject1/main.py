import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents = intents)
client = discord.Client(intents=intents)


#channel and category of text
@bot.event
async def on_guild_join(guild: discord.Guild):
    # verifing for category WORLD__
    welcome_name = "__WORLD__"
    welcome_info = discord.utils.get(guild.categories, name=welcome_name)
    if not welcome_info:
        welcome_info = await guild.create_category_channel(welcome_name)


    # verifing for category __information__
    information_name = "__INFORMATION__"
    information_info = discord.utils.get(guild.categories, name=information_name)
    if not information_info:
        information_info = await guild.create_category_channel(information_name)

    # verifing for category TEXT__
    text_name = "__TEXT__"
    text_info = discord.utils.get(guild.categories, name=text_name)
    if not text_info:
        text_info = await guild.create_category_channel(text_name)


    # verifing for category __GAMING VOICE__
    gaming_voice_name = "__GAMING VOICE__"
    gaming_voice_info = discord.utils.get(guild.categories, name=gaming_voice_name)
    if not gaming_voice_info:
        gaming_voice_info = await guild.create_category_channel(gaming_voice_name)


    #verifing private category

    private_consulting = "__CONSULTING__"
    consulting_info = discord.utils.get(guild.categories, name=private_consulting)

    if not consulting_info:
        consulting_info = await guild.create_category_channel(private_consulting)



    # create channel for world (WELCOME, GOODBYE, ALL, MUSIC1, MUSIC2)
    if welcome_info:
        welcome_name = '😎WELCOME😎'
        channel_welcome = discord.utils.get(guild.channels, name=welcome_name)
        if not channel_welcome:
            channel_welcome = await guild.create_text_channel(welcome_name, category=welcome_info)

        # goodbye channel verifing and create is not exist
        goodbye_name = '🥹GOODBYE🥹'
        channel_goodbye = discord.utils.get(guild.channels, name=goodbye_name)
        if not channel_goodbye:
            channel_goodbye = await guild.create_text_channel(goodbye_name, category=welcome_info)
        # all channels verifing and create is not exist
        world_name = '🥸ALL🤪 '
        channel_world = discord.utils.get(guild.channels, name=world_name)
        if not channel_world:
            channel_world = await guild.create_voice_channel(world_name, category=welcome_info)

        # MUSIC-1 channels verifing and create is not exist
        music_name = 'MUSIC-1 🎶'
        channel_music1 = discord.utils.get(guild.channels, name=music_name)
        if not channel_music1:
            channel_music1 = await guild.create_voice_channel(music_name, category=welcome_info)

        # MUISIC-2 channels verifing and create is not exist
        music2_name = 'MUSIC-2🔊'
        channel_music2 = discord.utils.get(guild.channels, name=music2_name)
        if not channel_music2:
            channel_music2 = await guild.create_voice_channel(music2_name, category=welcome_info)


    # create channel for information (RULES, DIRECT TWITCH, DIRECT ONLINE)
    if information_info:
        rules_name = 'RULES📜'
        channel_rules = discord.utils.get(guild.channels, name=rules_name)
        if not channel_rules:
            channel_rules = await guild.create_text_channel(rules_name, category=information_info)

        # TWICHT channels verifing and create is not exist
        twitch_name = 'DIRECT TWITCH🟪🟣'
        channel_twitch = discord.utils.get(guild.channels,name=twitch_name )
        if not channel_twitch:
            channel_twitch = await guild.create_text_channel(twitch_name, category=information_info)

        # DIRECT ONLINE channels verifing and create is not exist
        directo_name = 'DIRECT ONLINE 🟪🟣'
        channel_directo_online = discord.utils.get(guild.channels, name=directo_name)
        if not channel_directo_online:
            channel_directo_online = await guild.create_text_channel(directo_name, category=information_info)
        # VOICE-INFO channels verifing and create is not exist
        voice_info_name = 'VOICE INFO 📢📢'
        channel_voice_info = discord.utils.get(guild.channels, name=voice_info_name)
        if not channel_directo_online:
            channel_voice_info = await guild.create_voice_channel(voice_info_name, category=information_info)

    # create channel for text (GENERAL, JOKES AND MEME, MUSIC and LINK, ONLY DATA, EXTRA'S)
    if text_info:

        # GENERAL channels verifing and create is not exist
        general_name = "GENERAL 🌍🗺"
        channel_general = discord.utils.get(guild.channels, name=general_name)
        if not channel_general:
            channel_general = await guild.create_text_channel(general_name, category=text_info)

        # JOKES AND MEME channels verifing and create is not exist
        memes_name = 'JOKES AND MEME 🤡🤡'
        channel_meme = discord.utils.get(guild.channels, name=memes_name)
        if not channel_meme:
            channel_memes = await guild.create_text_channel(memes_name, category=text_info)

        # MUSIC and LINK channels verifing and create is not exist
        music_link_name = 'MUSIC and LINK 🔊'
        channel_music = discord.utils.get(guild.channels, name = music_link_name)
        if not channel_music:
            channel_music = await guild.create_text_channel(music_link_name,category=text_info)

        # ONLY DATA channels verifing and create is not exist
        only_data_name = 'ONLY DATA 🤖📜👏🏻'
        channel_only_data = discord.utils.get(guild.channels, name = only_data_name)
        if not channel_only_data:
            channel_only_data = await guild.create_text_channel(only_data_name, category=text_info)

        # EXTRA channels verifing and create is not exist
        extra_name = "EXTRA :) "
        channel_extra = discord.utils.get(guild.channels,name = extra_name )
        if not channel_extra:
            channel_extra = await guild.create_text_channel(extra_name, category=text_info)

    # create channel for gaming (SOLO*2 , DUO*3, THREE*3, SQUAD*4)
    if gaming_voice_info:

        #only me channels verifing and create is not exist
        only_name = 'ONLY ME 🎮 '
        channel_only = discord.utils.get(guild.channels, name = only_name)
        if not channel_only:
            channel_only = await guild.create_voice_channel(only_name, category=gaming_voice_info)

        # only me 2 channels verifing and create is not exist
        only2_name = 'ONLY ME-2 🎮'
        channel_only2 = discord.utils.get(guild.channels, name = only2_name)
        if not channel_only2:
            channel_only2 = await guild.create_voice_channel(only2_name, category=gaming_voice_info)

        #duo channels

        # DUO 1 channels verifing and create is not exist
        duo_name = 'DUO 🏁🎯🎮'
        channel_duo = discord.utils.get(guild.channels, name =duo_name)
        if not channel_duo:
            channel_duo = await guild.create_voice_channel(duo_name, category=gaming_voice_info)

        # DUO 2 channels verifing and create is not exist
        duo2_name = 'DUO-2🏁🎯🎮'
        channel_duo2 = discord.utils.get(guild.channels, name = duo2_name)
        if not channel_duo2:
            channel_duo2 = await guild.create_voice_channel(duo2_name, category=gaming_voice_info)

        # DUO 3 channels verifing and create is not exist
        duo3_name = 'DUO-3 🏁🎯🎮'
        channel_duo3 = discord.utils.get(guild.channels, name = duo3_name )
        if not channel_duo3:
            channel_duo3 = await  guild.create_voice_channel(duo3_name, category=gaming_voice_info)

        # three channels

        # 'TRHEE channels verifing and create is not exist
        trhee_name_channel = 'TRHEE 🎲👾🎮'
        channel_three = discord.utils.get(guild.channels, name = trhee_name_channel)
        if not channel_three:
            channel_three = await guild.create_voice_channel(trhee_name_channel, category=gaming_voice_info)

        # 'TRHEE 2 channels verifing and create is not exist
        trhee2_name_channel = 'THREE-2🎲👾🎮'
        channel_three2 = discord.utils.get(guild.channels, name=trhee2_name_channel)
        if not channel_three2:
            channel_three2 = await guild.create_voice_channel(trhee2_name_channel, category=gaming_voice_info)

        # 'TRHEE 3 channels verifing and create is not exist
        trhee3_name_channel = 'THREE-3🎲👾🎮'
        channel_three3 = discord.utils.get(guild.channels, name=trhee3_name_channel)
        if not channel_three3:
            channel_three3 = await guild.create_voice_channel(trhee3_name_channel, category=gaming_voice_info)

        # SQUAD CHANNELS

        # SQUAD channels verifing and create is not exist
        squad_name_channel = 'SQUAD 🔫🎮🏁'
        channel_squad = discord.utils.get(guild.channels, name=squad_name_channel)
        if not channel_squad:
            channel_squad = await guild.create_voice_channel(squad_name_channel, category=gaming_voice_info)

        # SQUAD2 channels verifing and create is not exist
        squad_name_channel2 = 'SQUAD-2 🔫🎮🏁'
        channel_squad2 = discord.utils.get(guild.channels, name=squad_name_channel2)
        if not channel_squad2:
            channel_squad2 = await guild.create_voice_channel(squad_name_channel2, category=gaming_voice_info)

        # SQUAD3 channels verifing and create is not exist
        squad_name_channel3 = 'SQUAD-3🔫🎮🏁 '
        channel_squad3 = discord.utils.get(guild.channels, name = squad_name_channel3 )
        if not channel_squad3:
            channel_squad3 = await guild.create_voice_channel(squad_name_channel3, category=gaming_voice_info)

        # SQUAD4 channels verifing and create is not exist
        squad_name_channel4 = 'SQUAD-4 🔫🎮🏁'
        channel_squad4 = discord.utils.get(guild.channels, name=squad_name_channel4)
        if not channel_squad4:
            channel_squad4 = await guild.create_voice_channel(squad_name_channel4, category=gaming_voice_info)


    #private category
    if consulting_info:
        #private channels

        # PRIVATE channels verifing and create is not exist
        work_channel_name = 'PRIVATE 🔒🔒'
        channel_work = discord.utils.get(guild.channels, name=work_channel_name)
        if not channel_work:
            channel_work = await guild.create_voice_channel(work_channel_name, category=consulting_info)

        # CONSULTORING channels verifing and create is not exist
        consultoring_name = 'CONSULTORING 🔒🔒'
        channel_consultoring = discord.utils.get(guild.channels, name=consultoring_name)
        if not channel_consultoring:
            channel_consultoring = await guild.create_voice_channel(consultoring_name, category=consulting_info)

        # CONSULTORING channels verifing and create is not exist
        channel_remember_name = 'REMEMBER THE TEAM 🔒🔒'
        channel_only_rol = discord.utils.get(guild.channels, name=channel_remember_name)
        if not channel_only_rol:
            channel_only_rol = await guild.create_voice_channel(channel_remember_name, category=consulting_info)

        # NEED PERMISSION FOR JOIN THIS CHANNELS
        await channel_work.set_permissions(guild.default_role , connect = False )
        await channel_consultoring.set_permissions(guild.default_role, connect = False)
        await  channel_only_rol.set_permissions(guild.default_role, connect = False)








token = 'MTE5OTA0NDAxNjE5NzYxOTc5Mg.G-1k5R.OX7LyOPryRsw96GVi4U6Ddsdmq6aia7uMy24Zk'
bot.run(token)
