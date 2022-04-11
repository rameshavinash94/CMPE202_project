from fastapi import FastAPI
from api.routers import Customer, Rewards, Booking, Hotel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(openapi_url='/api/v1/hotelbooking/tasks/openapi.json',
              docs_url='/api/v1/hotelbooking/tasks/docs')

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"],allow_credentials=True)

@app.get("/")
async def root():
    return "Entry Page Testing"

app.include_router(Customer.router,prefix='/api/v1/hotelbooking/tasks')
app.include_router(Rewards.router,prefix='/api/v1/hotelbooking/tasks')
app.include_router(Booking.router,prefix='/api/v1/hotelbooking/tasks')
app.include_router(Hotel.router,prefix='/api/v1/hotelbooking/tasks')
