from fastapi import FastAPI

from api.routers import all_routers


app = FastAPI(title='Records_Encryption_App')


for router in all_routers:
    app.include_router(router)
 
@app.on_event("startup")
async def startup():
    print('[+] APP SERVER WAS STARTED')


if __name__ == "__main__":
    import uvicorn
    from config import UVI_PORT,UVI_HOST, LOG_CONFIG
    uvicorn.run(app, log_config=LOG_CONFIG, host=UVI_HOST, port=UVI_PORT)
