# chatbot_api.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(chat_message: ChatMessage):
    # Check if the incoming message is "hello" (case-insensitive)
    if chat_message.message.lower() == "hello":
        return {"reply": "hi"}
    else:
        return {"reply": "Sorry, I didn't understand that."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Main:app", host="127.20.1.0", port=8000, reload=True)
