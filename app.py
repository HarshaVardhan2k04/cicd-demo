from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/version")
def version():
    import sys
    match sys.version_info.minor:
        case 12:
            return {"python": "3.12", "support": "full"}
        case _:
            return {"python": f"3.{sys.version_info.minor}", "support": "partial"}