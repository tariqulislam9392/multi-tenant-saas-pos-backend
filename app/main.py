from fastapi import FastAPI

from app.database import Base
from app.database import engine

import app.models  # Ensure models are imported so that they are registered with SQLAlchemy
Base.metadata.create_all(bind=engine)

app = FastAPI(
title="Multi Tenant saas pos",
description="A multi-tenant saas point of sale application.",
version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Multi-Tenant SaaS POS Application!"} 
