from fastapi import FastAPI
from bus.routes import router as bus_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.include_router(bus_router)
