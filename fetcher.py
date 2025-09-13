import pandas as pd
import requests
import json
from urllib.parse import quote

# Leer token desde .secrets
def get_token():
    with open(".secrets") as f:
        secrets = json.load(f)
    return secrets["token"]

token = get_token()

# Construcción URL
url = f"  https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/910424/es/0700/false/BIE/2.0/{token}?type=json"

print(f"Consulta generada: {url}")

# Obtener datos
res = requests.get(url)
if res.status_code != 200:
    print(f"Error al obtener datos del INEGI: {res.status_code}")
else:
    try:
        content = res.json()
        series = content.get("Series", [])
        if series and isinstance(series, list):
            observations = series[0].get("OBSERVATIONS", [])
        else:
            observations = []
    except Exception as e:
        print(f"No se pudo procesar la respuesta: {e}")
        observations = []

    if observations:
        df = pd.DataFrame(observations)
        print("Datos obtenidos exitosamente:")
        print(df)

        # Guardar los datos como CSV
        df.to_csv("observaciones.csv", index=False, encoding="utf-8")
        print("Datos guardados como 'observaciones.csv'.")
    else:
        print("No se encontraron observaciones")
