from pydantic import BaseModel, Field


class Service(BaseModel):
    port: int = Field(ge=1, le=65535)
    protocol: str
    name: str | None = None


class Asset(BaseModel):
    hostname: str | None = None
    ip_address: str
    source: str
    services: list[Service] = Field(default_factory=list)
