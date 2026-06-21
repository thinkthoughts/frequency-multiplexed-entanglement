from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)
    return path

ensure_dir(FIGURES_DIR)
ensure_dir(RESULTS_DIR)
