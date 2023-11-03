from os import environ as env
import uvicorn

# DATABASES CONFIG
ASYNC_POSTGRES_URL = f"postgresql+asyncpg://{env['POSTGRES_USER']}:{env['POSTGRES_PASSWORD']}@postgres_db/"
MONGO_URL = f"mongodb://{env['MONGO_USER']}:{env['MONGO_PASSWORD']}@mongo_db/"
MONGO_DATABASE_NAME='records'

# UVI CONFIG
UVI_HOST = env['UVI_HOST']
UVI_PORT = int(env['UVI_PORT'])
LOG_CONFIG = uvicorn.config.LOGGING_CONFIG
LOG_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"

# REMOVING INTERVALS IN SECONDS
REMOVE_INTERVALS = 3600

# PYDANTIC SCHEMAS SETTINGS
TextSchemaCreateMaxLength = 1000