from os import environ as env
import uvicorn


# UVI CONFIG
SCHEDULER_HOST = env['SCHEDULER_HOST']
SCHEDULER_PORT = int(env['SCHEDULER_PORT'])
LOG_CONFIG = uvicorn.config.LOGGING_CONFIG
LOG_CONFIG["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
LOG_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
