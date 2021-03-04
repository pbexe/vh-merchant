from fastapi import FastAPI, File, UploadFile
import uvicorn
from struct import unpack, calcsize
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Please post to /upload"}


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    merchant = get_entity_location(file.file.read(), b"Vendor_BlackForest")
    return {"locations": {
        "merchant": (int(merchant[0]), int(merchant[2])),
        "eikthyrnir": (420, 69)
    }}

@app.post("/upload_alt/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"locations": {
        "merchant": (10,-1000),
        "boss_1": (100, 1234)
    }}

def get_entity_location(db, name):
    root =  db.find(name) + len(name)
    coords = unpack("fff", db[root:root + calcsize("fff")])
    return coords


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
