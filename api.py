from fastapi import FastAPI, Path

app = FastAPI()

gstDict = {
    "AU": {
        "countryName": "Australia",
        "gstRate": 0.1,
        "currency": "AUD",
        "currencySymbol": "$"
    },
    "NZ": {
        "countryName": "New Zealand",
        "gstRate": 0.15,
        "currency": "NZD",
        "currencySymbol": "$"
    }
}

@app.get("/v1/tax/{country_code}")
async def get_tax_rate(country_code: str = Path(None, description="ISO 3166-1 alpha-2 country code")):
    if country_code in gstDict:
        return gstDict[country_code]
    else:
        return {"error": "Country code not found"}