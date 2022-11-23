import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

IMDB_CAPTION = environ.get("IMDB_CAPTION", "# Imdb Caption 🗯️\n<b>☊ 𝐅𝐢𝐥𝐦 :</b> 
📅 𝐘𝐞𝐚𝐫 : 
🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 
💿 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 :
🕐 𝐓𝐢𝐦𝐞 : 
🌟 𝐌𝐨𝐯𝐢𝐞 𝐑𝐚𝐭𝐢𝐧𝐠 : 
🏙 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : 


🔘𝐉𝐨𝐢𝐧
