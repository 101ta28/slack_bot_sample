from fastapi import FastAPI

from router import kintai

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

v1 = FastAPI()

@v1.get("/")
def read_root():
    return {"message": "You get test message!!"}

v1.include_router(kintai.router)

app.mount("/api/v1", v1)
