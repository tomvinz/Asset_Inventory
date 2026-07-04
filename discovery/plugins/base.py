from abc import ABC, abstractmethod
from collections.abc import Iterable

from discovery.models import DiscoveredAsset


class DiscoveryPlugin(ABC):
    name: str

    @abstractmethod
    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        """Collect assets from the supplied target list."""
