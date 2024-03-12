from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(tags=["healthcheck"])

@router.get("/healthcheck", response_class=JSONResponse, include_in_schema=False)
async def healthcheck() -> JSONResponse:
    """
    Returns the healthcheck response
    """
    return JSONResponse(status_code=200, content={"status": "ok"})