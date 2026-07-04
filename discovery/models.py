from pydantic import BaseModel, Field


class DiscoveredService(BaseModel):
    port: int = Field(ge=1, le=65535)
    protocol: str
    name: str | None = None


class DiscoveredAsset(BaseModel):
    ip_address: str
    hostname: str | None = None
    source: str
    services: list[DiscoveredService] = Field(default_factory=list)
    metadata: dict[str, str] = Field(default_factory=dict)
