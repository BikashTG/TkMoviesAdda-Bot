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

IMDB_CAPTION = environ.get("IMDB_CAPTION", "# Imdb Caption 🗯️\n<b>☊ 𝐅𝐢𝐥𝐦 :</b> {title}\n<b>📅 𝐘𝐞𝐚𝐫 :</b> {release_date}\n<b>🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :</b> {languages}\n<b>🕐 𝐓𝐢𝐦𝐞 :</b> <code>{runtime} minutes</code>\n<b>🌟 𝐌𝐨𝐯𝐢𝐞 𝐑𝐚𝐭𝐢𝐧𝐠 :</b> {rating} / 10\n<b>🏙 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 :</b> {countries}\n\n<b>🔘𝐉𝐨𝐢𝐧</b>\n👉 \n👉")

