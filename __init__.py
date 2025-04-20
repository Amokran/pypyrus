import os

# Read version from VERSION file
_version_file = os.path.join(os.path.dirname(__file__), "VERSION")
with open(_version_file) as f:
    __version__ = f.read().strip()

from .translation_manager import TranslationManager
from .metadata import Metadata

__all__ = ["TranslationManager", "Metadata"]