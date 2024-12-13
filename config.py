import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23159366")
    API_HASH  = os.environ.get("API_HASH", "4623dd30dd1303bddb729eb0862262d9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AutoRenamer")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://testbot:testbot@cluster0.7rzwxwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/7687f4eb79b81db106765.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5222155765').split()]
    # -- FORCE_SUB_CHANNELS = ["Warrior_Units","WarriorUnitsBots","WarriorUnits"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'WarriorUnitsBots,Warrior_Units').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002164129051"))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @WarriorUnitsBots</b>

<b><a href='https://t.me/WarriorUnitsBots'>WarriorUnitsBots</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @WarriorUnitsBots</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/WarriorUnitsBots'>WarriorUnitsBots</a>
    
<b>♻️ Bot Made By :</b> @WarriorUnitsBots"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @WarriorUnitsBots
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - 007jatji@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @WarriorUnitsBots To Help """





