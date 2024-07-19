import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "
6605759587:AAHLY42NBlfSSUhRJCGyk0ZYOcc47VsTXb8
")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28530298"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c042ac8604791a187b90be6684993e2b
")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://fowardbot:fowardbot@cluster0.qjwunlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
