echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/BikashTG/UniqueMovie-Bot.git /UniqueMovie-Bot
cd /UniqueMovie-Bot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot Please Wait..."
python3 bot.py
