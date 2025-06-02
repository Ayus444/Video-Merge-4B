import os

class Config(object):
    API_HASH = os.environ.get("API_HASH", "1db7bdcf908100cc641c6a5276765c3d")  # Default value added for safety
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7483308323:AAHKI83Opq3xdY590DuoIwLrxh_ft_awg44")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "22581733")
    OWNER = os.environ.get("OWNER", "6530997270")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Slayerxcorp")
    PASSWORD = os.environ.get("PASSWORD", "mypass")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    LOGCHANNEL = int(os.environ.get("LOGCHANNEL", "-1002294532244"))  # Convert to integer for Telegram compatibility
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = os.environ.get("IS_PREMIUM", "False").lower() == "true"  # Convert string to boolean
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
