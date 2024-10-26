from fastapi import FastAPI
from bus.routes import router as bus_router
from route.routes import router as route_router
from auth.routes import router as auth_router
from booking.routes import router as booking_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.include_router(bus_router)
app.include_router(route_router)
app.include_router(auth_router)
app.include_router(booking_router)
