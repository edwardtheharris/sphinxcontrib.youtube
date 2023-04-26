"""Test configuration package."""
from pathlib import Path
import sys

repo_root=Path(__file__).parent

sys.path.append(str(repo_root))

print(sys.path)
