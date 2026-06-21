import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_paper():
    with open(ROOT / "paper.yaml", "r") as f:
        return yaml.safe_load(f)
