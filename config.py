import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28574839"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a844a3066fb7e5f61f049dee592ae024")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://xeroxbayzid12:xeroxbayzid12@cluster0.dcapc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
