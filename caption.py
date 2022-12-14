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

IMDB_CAPTION = environ.get("IMDB_CAPTION", """# Imdb Caption šÆļø\n<b>ā šš¢š„š¦ :</b> {title}\n<b>š šššš« :</b> {release_date}\n<b>š ššš§š š®šš š :</b> {languages}\n<b>š šš¢š¦š :</b> <code>{runtime} minutes</code>\n<b>š ššØšÆš¢š ššš­š¢š§š  :</b> {rating} / 10\n<b>š ššØš®š§š­š«š² :</b> {countries}\n\n<b>šššØš¢š§</b>\nš <a href="https://t.me/Its_unique_movies_adda">Unique Movies</a>\nš <a href="https://t.me/+BixProBUQBo4MWM9">Unique Movies Updates</a>""")

