from fastapi import APIRouter

from api.app.schemas import Asset

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("", response_model=list[Asset])
def list_assets() -> list[Asset]:
    return [
        Asset(
            hostname="localhost",
            ip_address="127.0.0.1",
            source="seed",
            services=[],
        )
    ]
