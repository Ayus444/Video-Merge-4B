import os


class Config(object):
    API_HASH = os.environ.get("1db7bdcf908100cc641c6a5276765c3d")
    BOT_TOKEN = os.environ.get("7483308323:AAHKI83Opq3xdY590DuoIwLrxh_ft_awg44")
    TELEGRAM_API = os.environ.get("22581733")
    OWNER = os.environ.get("6530997270")
    OWNER_USERNAME = os.environ.get("Slayerxcorp")
    PASSWORD = os.environ.get("mypass")
    DATABASE_URL = os.environ.get("mongodb+srv://neoayush444:3kuwGf9jKicbDxvT@cluster0.f9vq7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002294532244")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
