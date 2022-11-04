from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    html_content = "<h1>Welcome to my site</h1>"
    return HTMLResponse(content=html_content, status_code=200)