"""
Installations for the necessary packages.
"""

import os
from dataclasses import dataclass

from rich.progress import track

from rysk_client.src.utils import get_logger

logger = get_logger()


@dataclass
class HostDependency:
    """
    represents a host dependency
    """

    name: str
    install_cmd: str

    def is_present(self) -> bool:
        """
        silently check if the dependency is present on the host
        """
        return os.popen(f"which {self.name}").read() != ""

    def install(self) -> None:
        """
        install the dependency
        """
        os.system(self.install_cmd)


def install_dependencies() -> None:
    """
    install the dependencies
    """
    dependencies = [
        (
            "rustc",
            "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
        ),
        (
            "anvil",
            "git clone https://github.com/foundry-rs/foundry && "
            + "cd foundry && "
            + "cargo install --path ./anvil --bins --locked --force && "
            + "rm -rf ../foundry",
        ),
    ]
    logger.info(f"Installing {len(dependencies)} dependencies")
    for dependency in track(dependencies):
        dep = HostDependency(*dependency)
        if not dep.is_present():
            logger.info(f"Installing {dep.name}")
            # dep.install()
    logger.info("Done!")


if __name__ == "__main__":
    install_dependencies()
