from decouple import config


# --------------------- OAUTH2 ---------------------
SECRET_KEY = config('SECRET_KEY')
HASH_ALGORITHM = config('HASH_ALGORITHM')
ACCESS_TOKEN_EXPIRE_SECONDS = int(config('ACCESS_TOKEN_EXPIRE_SECONDS'))
REFRESH_TOKEN_EXPIRE_SECONDS = int(config('REFRESH_TOKEN_EXPIRE_SECONDS'))
CODE_EXPIRE_SECONDS = int(config('CODE_EXPIRE_SECONDS'))
# --------------------------------------------------

# ------------------- DATABASE ---------------------
DATABASE_URL = config('DATABASE_URL')
# --------------------------------------------------

# --------------- OPENAI CALLBACK ------------------
CALLBACK_URL = config('CALLBACK_URL')
# --------------------------------------------------
