from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.base import DiscoveryPlugin


class DnsDiscoveryPlugin(DiscoveryPlugin):
    name = "dns"

    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        return [
            DiscoveredAsset(ip_address=target, hostname=None, source=self.name)
            for target in targets
        ]
