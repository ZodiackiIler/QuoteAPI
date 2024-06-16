# main.py
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import os
import init_db  # Импорт функций из init_db.py

# Загрузка переменных среды из .env файла
load_dotenv()
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

app = FastAPI()

class QuoteResponse(BaseModel):
    id: int = Field(..., example=1)
    text: str = Field(..., example="В жизни есть мгновения, которые меняют нас раз и навсегда.")
    author: Optional[str] = Field(None, example="Джеффри Дивер")
    theme: Optional[str] = Field(None, example="жизнь")

class QuoteRequest(BaseModel):
    text: str
    author: Optional[str] = None
    theme: Optional[str] = None

def get_token_header(x_token: str = Header(...)):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/random_quote", response_model=QuoteResponse, summary="Get a random quote", description="Fetch a random quote from the database")
def get_random_quote():
    quote = init_db.get_random_quote()
    if quote:
        return quote
    else:
        raise HTTPException(status_code=404, detail="Quote not found")

@app.post("/add_quote", summary="Add a new quote", description="Add a new quote to the database", dependencies=[Depends(get_token_header)])
def add_quote(quote: QuoteRequest):
    result = init_db.add_quote_to_db(quote.text, quote.author, quote.theme)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.put("/update_quote/{quote_id}", summary="Update an existing quote", description="Update an existing quote in the database", dependencies=[Depends(get_token_header)])
def update_quote(quote_id: int, quote: QuoteRequest):
    result = init_db.update_quote_in_db(quote_id, quote.text, quote.author, quote.theme)
    if "error" in result:
        if result["error"] == "Quote not found":
            raise HTTPException(status_code=404, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.delete("/delete_quote/{quote_id}", summary="Delete an existing quote", description="Delete an existing quote from the database", dependencies=[Depends(get_token_header)])
def delete_quote(quote_id: int):
    result = init_db.delete_quote_from_db(quote_id)
    if "error" in result:
        if result["error"] == "Quote not found":
            raise HTTPException(status_code=404, detail=result["error"])
        else:
            raise HTTPException(status_code=500, detail=result["error"])
    return result

# Для запуска сервера используйте команду ниже
# uvicorn main:app --reload
