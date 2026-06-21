import pandas as pd

def scaling_table(max_channels=100):
    rows = []
    for n in range(1, max_channels + 1):
        rows.append({
            "channels": n,
            "devices_architecture_sources": n,
            "devices_architecture_detectors": n,
            "mode_architecture_resonators": 1,
            "mode_architecture_modes": n,
        })
    return pd.DataFrame(rows)
