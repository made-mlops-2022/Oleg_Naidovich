import uvicorn
from fastapi import FastAPI


app = FastAPI()
model = None

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000)