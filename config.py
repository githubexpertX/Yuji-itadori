from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",'28731705'))
API_HASH = getenv("API_HASH",'7ed8bb45ea845bef652aa0606584f413')

BOT_TOKEN = getenv("BOT_TOKEN",'6338221023:AAF7XDPQv6p6ebWdunT1tcCLDdsY1mBy_KA')
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",'6647321265'))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2a457256aed0ca9a4fcd5.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/16c5ea4390fcb09ac5a20.jpg")

SESSION = getenv("SESSION","AQG2aTkAS47gsetpjbftb2GfcPSr-Si_hRtz_-8KWCaLzQrMsrh4Y71PvFB2c-BpI35Fnno1ZeLANaAmXxgyV4x1QTaCoo-BW4EO405VAXojWJoNKmLGeGUwSanAkm-4i55yXP74XzV3t330tVtuuXqx4m7Btsf5DWhW9SNBFiyjX5LZesYFCo0vAiKOK7YT9K_qReTBRHtAF27t92M43b8r6Yn38WKSp4a_VkUQwyewKlCE4DLTjrADA3wXJrvgDezjcXJij3u3rwK8ReVknyjKMeGPFtSnSfAyKOLD40KQxKLhjk-hISNVYpUTlykgO5pmu8U3T6r1LVsXXcakcBZxZ9pTzAAAAAGFN2o4AA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/fuck_uff_XD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fuck_uff_XD")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6647321265").split()))


FAILED = "https://telegra.ph/file/24981f7943d702af1851a.jpg"
