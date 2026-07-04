from discovery.runner import run_plugins


def test_run_plugins_returns_discovered_assets() -> None:
    assets = run_plugins(["nmap", "dns"], ["127.0.0.1"])

    assert len(assets) == 2
    assert {asset.source for asset in assets} == {"nmap", "dns"}
