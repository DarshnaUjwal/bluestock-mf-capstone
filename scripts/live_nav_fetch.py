import requests
import pandas as pd
from pathlib import Path

save_path = Path("data/raw")

scheme_codes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{fund_name}_live_nav.csv"

        nav_df.to_csv(
            save_path / file_name,
            index=False
        )

        print(f"Saved {file_name}")

    else:

        print(f"Failed for {fund_name}")