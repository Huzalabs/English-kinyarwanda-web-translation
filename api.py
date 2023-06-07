from fastapi import FastAPI, Request, Response, UploadFile, Form, File
from docx import Document
from translator import *
import nest_asyncio
from pyngrok import ngrok
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ngrok_tunnel = ngrok.connect(3000)

# Gov
@api.post('/translate')
async def translate(request: Request, payload: dict):
    text = payload.get('text')
    source_lang = payload.get('source_lang')
    target_lang = payload.get('target_lang')

    paragraphs = text.split('\n')
    texts = []
    for text in paragraphs:
        trans_text = translate_row(text, target_lang=f'{target_lang}', source_lang=f'{source_lang}')
        texts.append(trans_text)

    # Update the API response with the ngrok URL
    response = "\n".join(texts)

    # Set CORS headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
        #"Location": f"{ngrok_tunnel.public_url}/translate"
    }
    return Response(content=response, headers=headers)


# if __name__ == "__main__":
#     print('Please use the following link to access your app:', ngrok_tunnel.public_url)
#     nest_asyncio.apply()
#     uvicorn.run(api, port=3000)
