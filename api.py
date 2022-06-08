from fastapi import FastAPI, Path

app = FastAPI()

gstDict = {
    "AU": {
        "gstRate": 0.1
    },
    "NZ": {
        "gstRate": 0.15
    },
    "CA": {
        "gstRate": 0.05
    }
}

@app.get("/v1/tax/{country_code}")
async def get_tax_rate(country_code: str = Path(None, description="ISO 3166-1 alpha-2 country code")):
    if country_code in gstDict:
        return gstDict[country_code]
    else:
        return {"error": "Country code not found"}