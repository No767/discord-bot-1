from pkgutil import iter_modules
from typing import Literal, NamedTuple


# This system comes from Discord.py directly
class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "final"]

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.micro}-{self.releaselevel}"


EXTENSIONS = [
    module.name
    for module in iter_modules(__path__, f"{__package__}.")
    if module.name != "cogs.utils"
]
VERSION: VersionInfo = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha")
