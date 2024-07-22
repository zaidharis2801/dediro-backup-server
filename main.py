from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/print")
async def print_data(request: Request):
    data = await request.json()
    print(data)
    return {"message": "Data received and printed."}
