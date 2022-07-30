import os
from services.iaManager import IaManager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

ia = IaManager()
app = FastAPI()

@app.get("/positive", tags=["Review"])
async def positif_review_of_inolys_company():
    review = ia.generateReview(True)
    return [{"review", review}]


@app.get("/negative", tags=["Review"])
async def negatif_review_of_inolys_company():
    review = ia.generateReview(False)
    return [{"review", review}]

@app.get("/", include_in_schema=False)
async def main():
    return RedirectResponse(url=f"/docs/", status_code=303)