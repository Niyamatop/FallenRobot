class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 6390608832
    API_HASH = "9647ab7fc03a8a93f701a5528b2f206e"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://avnadmin:AVNS_gwvtPgMcQ7IX0qwaCG9@freedb-mayrice01.i.aivencloud.com:14358/defaultdb?sslmode=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002239117016)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Dark123:Dark123@cluster0.jsapbqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7346455769:AAG4S9buEgIlCfwT-Vk80PaODeILZ_hLWlw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5536168611  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
