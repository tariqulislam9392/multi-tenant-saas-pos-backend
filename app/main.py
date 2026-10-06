from fastapi import FastAPI

app = FastAPI(
title="Multi Tenant saas pos",
description="A multi-tenant saas point of sale application.",
version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Multi-Tenant SaaS POS Application!"} 
