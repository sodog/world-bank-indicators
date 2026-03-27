import pandas as pd
from .api import get_indicator_page


def fetch_indicator_catalog():
    first = get_indicator_page(1)
    pages = int(first["metadata"]["pages"])

    rows = []

    for page in range(1, pages + 1):
        data = first if page == 1 else get_indicator_page(page)

        for item in data["indicators"]:
            rows.append({
                "indicator_code": item.get("id"),
                "indicator_name": item.get("name"),
                "source": (item.get("source") or {}).get("value"),
                "description": item.get("sourceNote"),
                "topics": [t["value"] for t in item.get("topics", [])]
            })

    return pd.DataFrame(rows)


def build_indicator_dict(df):
    df = df.dropna(subset=["indicator_code"]).drop_duplicates("indicator_code")
    return df.set_index("indicator_code").to_dict("index")
