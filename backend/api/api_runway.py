from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import httpx

load_dotenv()

RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY")

router = APIRouter()

class RunwayGenerateRequest(BaseModel):
    prompt: str
    image_url: str | None = None

@router.post("/generate", response_model=dict)
async def generate(req: RunwayGenerateRequest):
    """Proxy endpoint to RunwayML (example).
    Returns the Runway API response or raises HTTPException on error.
    """
    if not RUNWAY_API_KEY:
        raise HTTPException(status_code=500, detail="Runway API key not configured")

    url = "https://api.runwayml.com/v1/generate"
    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": req.prompt}
    if req.image_url:
        payload["image_url"] = req.image_url

    timeout = httpx.Timeout(30.0, connect=5.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.post(url, headers=headers, json=payload)

    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Runway error: {resp.text}")

    return resp.json()