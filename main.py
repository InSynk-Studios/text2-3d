from gradio_client import Client
import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

client = Client("https://1fecaa770204d8b7be.gradio.live")




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


photos = []

@app.get("/")
async def home(request: Request):
    return {"message": "hello world"}

@app.post("/getobjfile/")
async def upload_video(seed: str):
    obj_file_path =  seed
    x = seed.split("/")[-1]
    headers = {'Content-Disposition': f'attachment; filename="{x}" '}
    print(obj_file_path)
    return FileResponse(obj_file_path, headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)