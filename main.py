from pyscript import document

# Dictionary storing the predetermined weather instruments dataset
weather_instruments = {
    "thermometer": {
        "name": "Thermometer",
        "measures": "Air Temperature",
        "unit": "Degrees Celsius (°C)",
        "purpose": "Measures how hot or cold the air is."
    },
    "barometer": {
        "name": "Barometer",
        "measures": "Atmospheric Pressure",
        "unit": "Hectopascals (hPa)",
        "purpose": "Measures air pressure to help monitor weather changes."
    },
    "anemometer": {
        "name": "Anemometer",
        "measures": "Wind Speed",
        "unit": "Kilometers per hour (km/h)",
        "purpose": "Measures how fast the wind is blowing."
    },
    "hygrometer": {
        "name": "Hygrometer",
        "measures": "Relative Humidity",
        "unit": "Percent (%)",
        "purpose": "Measures the amount of moisture in the air."
    },
    "rain gauge": {
        "name": "Rain Gauge",
        "measures": "Rainfall",
        "unit": "Millimeters (mm)",
        "purpose": "Measures the amount of rainfall in an area."
    },
    "wind vane": {
        "name": "Wind Vane",
        "measures": "Wind Direction",
        "unit": "Cardinal Directions",
        "purpose": "Identifies the direction from which the wind is blowing."
    },
    "weather balloon": {
        "name": "Weather Balloon",
        "measures": "Atmospheric Conditions",
        "unit": "Varies",
        "purpose": "Collects atmospheric data at different altitudes."
    },
    "pyranometer": {
        "name": "Pyranometer",
        "measures": "Solar Radiation",
        "unit": "Watts per square meter (W/m²)",
        "purpose": "Measures incoming solar radiation."
    }
}

# Default fallback dictionary for instruments not found
not_found_data = {
    "name": "Not Found",
    "measures": "N/A",
    "unit": "N/A",
    "purpose": "The entered weather instrument is not included in the dataset."
}

def search_instrument(event):
    # Get user input, strip extra spaces, and convert to lowercase for case-insensitive matching
    raw_input = document.querySelector("#instrument-input").value
    query = raw_input.strip().lower()
    
    # Retrieve the instrument dictionary using .get() with the default fallback
    result = weather_instruments.get(query, not_found_data)
    
    # Format and display the output in the HTML result area
    output_html = (
        f"<strong>Weather Instrument:</strong> {result.get('name')}<br>"
        f"<strong>What It Measures:</strong> {result.get('measures')}<br>"
        f"<strong>Unit of Measurement:</strong> {result.get('unit')}<br>"
        f"<strong>Purpose:</strong> {result.get('purpose')}"
    )
    
    document.querySelector("#result-area").innerHTML = output_html