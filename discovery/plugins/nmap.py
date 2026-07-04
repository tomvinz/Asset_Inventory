from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.base import DiscoveryPlugin


class NmapDiscoveryPlugin(DiscoveryPlugin):
    name = "nmap"

    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        return [
            DiscoveredAsset(ip_address=target, source=self.name, metadata={"status": "stub"})
            for target in targets
        ]
