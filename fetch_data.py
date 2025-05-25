import pandas as pd
import requests

def fetch_all_launches():
    url = "https://api.spacexdata.com/v5/launches/query"
    query = {"query": {}, "options": {"pagination": False}}

    res = requests.post(url, json=query)
    data = res.json()["docs"]

    df = pd.json_normalize(data)
    df.to_csv("spacex_data.csv", index=False)
    print("✅ All SpaceX launch data saved to spacex_data.csv")

if __name__ == "__main__":
    fetch_all_launches()


