from fastapi import FastAPI
from ollama import ChatResponse, Client
from fastapi import Body
app = FastAPI()

client = Client(
    host='http://localhost:11434/'
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat( message: str = Body(..., example="Hello, how are you?")):
    response: ChatResponse = client.chat(model='gemma:2b', messages=[
    {
        'role': 'user',
        'content':message,
    },
    ])
    print(response.message.content)
    return {"response": response.message.content}