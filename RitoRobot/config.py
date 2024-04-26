class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29418676
    API_HASH = "0d522e02f8ea68339661fc9146479c15"

    CASH_API_KEY = "BQO2E9CQOR2P"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    EVENT_LOGS = (-1001969246312)  # Event logs channel to note down important bot level events

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph//file/5f47ba158a30ce7d161ea.jpg"
    
    DONATE_LINK = "https://link.dana.id/qr/6l85aa18"

    SUPPORT_CHAT = "musik_supportdan"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6647010165:AAEkpnjD2-X54hXZmI7SwO0RFXSi89Uw6cU"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "OMHHBGMFANR1RP76"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5779185981  # User id of your telegram account (Must be integer)
    
    MUST_JOIN = "Disney_storeDan"
    
    #TAMBAHAN
    DATABASE_URL = "postgres://wscpccsiinunst:f6f399e7919187bdab4e43193d49c974ef3dbf81a70b8f308a044d2277be8c04@ec2-34-232-92-61.compute-1.amazonaws.com:5432/dane27hmja8n37"
    MONGO_DB_URI = "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.pom3ops.mongodb.net/?retryWrites=true&w=majority"
    ARQ_API_KEY = "VFYULS-ASTLSK-BRVUAU-ZEGDFV-ARQ"
    ARQ_API_URL = "http://arq.hamker.dev"
    
    # Optional fields
    BL_CHATS = [5779185981]  # List of groups that you want blacklisted.
    DRAGONS = [5779185981]  # User id of sudo users
    DEV_USERS = [5779185981]  # User id of dev users
    DEMONS = [5779185981]  # User id of support users
    TIGERS = [5779185981]  # User id of tiger users
    WOLVES = [5779185981]  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "mhmdwldnnnn"
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./download/"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
