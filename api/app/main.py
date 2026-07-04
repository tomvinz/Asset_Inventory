from fastapi import FastAPI

from api.app.routes.assets import router as assets_router

app = FastAPI(
    title="Asset Discovery Platform API",
    version="0.1.0",
    description="API for cyber asset inventory, discovery status, and integrations.",
)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(assets_router)
