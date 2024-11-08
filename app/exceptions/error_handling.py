from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Union


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            # Call the next middleware or the actual route handler
            response = await call_next(request)
            return response
        except HTTPException as exc:
            # Handle known HTTPExceptions (like 404, 500)
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail}
            )
        except Exception as exc:
            # Handle all other exceptions (e.g., unexpected errors)
            return JSONResponse(
                status_code=500,
                content={"detail": f"An internal error occurred: {str(exc)}"}
            )
