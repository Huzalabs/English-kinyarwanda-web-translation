from fastapi import FastAPI, Request, Response, UploadFile, Form, File
from docx import Document
from translator import *

#Initiate the api
api = FastAPI()



#Gov
@api.post('/translate')
async def translate(request : Request, text : str = Form(...), source_lang : str = Form(...), target_lang : str = Form(...)):
    paragraphs = text.split('\n')
    texts = []
    for text in paragraphs:
        trans_text = translate_row(text, target_lang=f'{target_lang}', source_lang=f'{target_lang}')
        texts.append(trans_text)
    
    return "\n".join(texts)
