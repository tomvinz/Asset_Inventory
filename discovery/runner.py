from collections.abc import Iterable

from discovery.models import DiscoveredAsset
from discovery.plugins.dns import DnsDiscoveryPlugin
from discovery.plugins.nmap import NmapDiscoveryPlugin
from discovery.plugins.smb import SmbDiscoveryPlugin
from discovery.plugins.snmp import SnmpDiscoveryPlugin
from discovery.plugins.ssl import SslDiscoveryPlugin

PLUGINS = {
    "nmap": NmapDiscoveryPlugin(),
    "dns": DnsDiscoveryPlugin(),
    "snmp": SnmpDiscoveryPlugin(),
    "smb": SmbDiscoveryPlugin(),
    "ssl": SslDiscoveryPlugin(),
}


def run_plugins(plugin_names: Iterable[str], targets: Iterable[str]) -> list[DiscoveredAsset]:
    discovered: list[DiscoveredAsset] = []
    target_list = list(targets)
    for plugin_name in plugin_names:
        plugin = PLUGINS[plugin_name]
        discovered.extend(plugin.collect(target_list))
    return discovered
