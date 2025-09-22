from fastapi import FastAPI, HTTPException
import asyncio
import time

app = FastAPI(title="Timeout API", description="A simple API that responds after a specified timeout")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "FastAPI Timeout Application is running!"}

@app.post("/")
async def timeout_endpoint(req : dict[str, int]):
    """
    Endpoint that waits for the specified number of seconds before responding
    
    Args:
        seconds: Number of seconds to wait (must be between 1 and 60)
    
    Returns:
        JSON response with success message and timing info
    """
    seconds = req.get("seconds", 1)
    # Validate input
    if seconds < 1:
        raise HTTPException(status_code=400, detail="Timeout must be at least 1 second")
    if seconds > 60:
        raise HTTPException(status_code=400, detail="Timeout cannot exceed 60 seconds")
    
    start_time = time.time()
    
    # Wait for the specified number of seconds
    await asyncio.sleep(seconds)
    
    end_time = time.time()
    actual_wait_time = round(end_time - start_time, 2)
    
    return {
        "success": True,
        "message": f"Successfully waited for {seconds} seconds",
        "requested_timeout": seconds,
        "actual_wait_time": actual_wait_time,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
