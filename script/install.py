"""
Installations for the necessary packages.
"""

import os
from dataclasses import dataclass

# we use the rich progress bar to show the progress of the installation

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
        HostDependency(
            "rustc",
            "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
        ),
        HostDependency("rysk", "poetry install"),
    ]
    logger.info(f"Installing {len(dependencies)} dependencies")
    for dependency in track(dependencies):
        if not dependency.is_present():
            logger.info(f"Installing {dependency.name}")
            dependency.install()
    logger.info("Done!")


if __name__ == "__main__":
    install_dependencies()
