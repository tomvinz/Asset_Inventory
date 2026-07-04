from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.base import DiscoveryPlugin


class SnmpDiscoveryPlugin(DiscoveryPlugin):
    name = "snmp"

    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        return [DiscoveredAsset(ip_address=target, source=self.name) for target in targets]
