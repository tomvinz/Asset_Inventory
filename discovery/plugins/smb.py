from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.base import DiscoveryPlugin


class SmbDiscoveryPlugin(DiscoveryPlugin):
    name = "smb"

    def collect(self, targets: Iterable[str]) -> list[DiscoveredAsset]:
        return [DiscoveredAsset(ip_address=target, source=self.name) for target in targets]
