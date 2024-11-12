from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.login import router as LoginRouter
from routes.ml_model import router as ModelRouter

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(LoginRouter, tags=["Login"], prefix="")
app.include_router(ModelRouter, tags=["Model"], prefix="/model")


