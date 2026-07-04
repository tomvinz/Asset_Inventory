import argparse
import json

from discovery.runner import run_plugins


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run discovery plugins.")
    parser.add_argument("--targets", required=True, help="Comma-separated targets.")
    parser.add_argument("--plugins", required=True, help="Comma-separated plugin names.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    targets = [target.strip() for target in args.targets.split(",") if target.strip()]
    plugins = [plugin.strip() for plugin in args.plugins.split(",") if plugin.strip()]
    assets = run_plugins(plugins, targets)
    print(json.dumps([asset.model_dump() for asset in assets], indent=2))


if __name__ == "__main__":
    main()
