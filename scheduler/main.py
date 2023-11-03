import time, asyncio
import uvicorn
from fastapi import FastAPI
import aiohttp



app = FastAPI(title='Scheduler Service')
http = 'http://app:8000'

# Every Minute
async def update_records(session) -> None:
    await asyncio.sleep(60)
    await session.get(http + "/update_records/")
    


async def main():
    async with aiohttp.ClientSession() as session:
        while time.gmtime().tm_sec != 0:
            while True:
                await update_records(session)

 
@app.on_event("startup")
async def startup():
    print('[+] SCHEDULER STARTED')
    await main()     


if __name__ == "__main__":
    import uvicorn
    from config import SCHEDULER_PORT,SCHEDULER_HOST, LOG_CONFIG
    uvicorn.run(app, log_config=LOG_CONFIG, host=SCHEDULER_HOST, port=SCHEDULER_PORT)


