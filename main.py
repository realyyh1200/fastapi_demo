import uvicorn
from fastapi import FastAPI
from routers import router


app = FastAPI(
    title="yyh_backend",
    description="个人项目",
    version="0.1.0"
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
