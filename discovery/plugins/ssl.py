from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.base import DiscoveryPlugin


class SslDiscoveryPlugin(DiscoveryPlugin):
    name = "ssl"

    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        return [DiscoveredAsset(ip_address=target, source=self.name) for target in targets]
