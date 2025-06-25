#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24515547"))
API_HASH = environ.get("API_HASH", "0809699a061f02fbbcc1a6c4443547ee")
BOT_TOKEN = environ.get("BOT_TOKEN", "7745629635:AAHigiLaGaAAXw6sfus_9vkKV3kBbavqbZU")
OWNER = int(environ.get("OWNER", "7503180362"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '7503180362').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
