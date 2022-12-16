from fastapi import FastAPI
from routes.user import user 

app = FastAPI(
    title="API Creditos",
    description="API que abrueba o rechaza un credito a un usuario, construido en python con fastAPI y SQLAlchemy"
)

app.include_router(user)
