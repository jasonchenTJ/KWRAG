import uvicorn
import uuid
from langchain_core.documents import Document
from Service.KwRag import KwRag
from fastapi import FastAPI , File, UploadFile
from pydantic import BaseModel
from fastapi import Form
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
kw = KwRag()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class User(BaseModel):
    username: str
    password: str

class Message(BaseModel):
    content: str


@app.post("/userLogon/")
def userLogon(user:User):
    result = kw.userLogon(user.username,user.password)
    return JSONResponse(content={"result":result})

@app.post("/LLMTalk/")
def LLMTalk(message:Message):
    comment = kw.LLMTalk(message.content)
    return JSONResponse(content={"comment":comment})

@app.post("/embeddingTalk/")
def embeddingTalk(message:Message):
    comment = kw.embeddingTalk(message.content)
    return JSONResponse(content={"comment":comment})

@app.post("/RAGTalk/")
def RAGTalk(message:Message):
    comment = kw.RAGTalk(message.content)
    return JSONResponse(content={"comment":comment})

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    docs = [
        Document(
            page_content=contents,
     metadata={"id": str(uuid.uuid4()), "catalog": "DB", "topic": "DBA knowledge"})]
    comment = kw.embeddingLoad(docs)
    #return {"filename": file.filename, "content_type": file.content_type, "file_size": len(contents)}
    return JSONResponse(content={"comment": comment})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8866)
