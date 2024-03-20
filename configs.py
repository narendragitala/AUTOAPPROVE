from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "SHAYRIGALIBKI")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO", "5473771943").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
