"""Start the dance project's native Blender helpers in the current session."""
from pathlib import Path
import sys

directory = str(Path(__file__).resolve().parent)
if directory not in sys.path:
    sys.path.insert(0, directory)
import dance_tools
dance_tools.register()
