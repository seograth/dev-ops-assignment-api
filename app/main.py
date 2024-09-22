from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()
REQUEST_COUNT = Counter('request_count', 'Number of requests')

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
def health_check():
    # comment out the following line to simulate a failing health check
    # raise HTTPException(status_code=500, detail="Internal Server Error")
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    registry = CollectorRegistry()
    REQUEST_COUNT.collect(registry)
    data = generate_latest(registry)
    return Response(data, media_type=CONTENT_TYPE_LATEST)