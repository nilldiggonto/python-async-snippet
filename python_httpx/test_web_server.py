from fastapi import FastAPI,Request
import uvicorn

app = FastAPI()

@app.get('/hi')
async def index():
    return {'status':'ok'}

@app.post('/write')
async def writeIndex(request:Request):
    data = await request.json()
    return data


if __name__ == '__main__':
    uvicorn.run("test_web_server:app", port=8005, host='127.0.0.1',workers=1)