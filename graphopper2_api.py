import requests

def solicitar_ciudades():
    # Jenkins no permite input(), así que usamos valores fijos
    return "santiago", "ovalle"

def obtener_datos(ciudad_origen, ciudad_destino):
    # Reemplaza esto con tu propia API key válida de Graphhopper
    api_key = "53920fda-c85e-4ed1-a438-2c08aaf90065"

    url = f"https://graphhopper.com/api/1/route?point={ciudad_origen},Chile&point={ciudad_destino},Chile&vehicle=car&locale=es&key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        distancia_metros = datos["paths"][0]["distance"]
        tiempo_ms = datos["paths"][0]["time"]
        return distancia_metros, tiempo_ms
    else:
        print(f"Error al consultar la API: {response.status_code}")
        return None, None

def main():
    origen, destino = solicitar_ciudades()
    print(f"Calculando ruta desde {origen} hasta {destino}...")
    distancia, tiempo = obtener_datos(origen, destino)
    
    if distancia and tiempo:
        print(f"Distancia aproximada: {distancia / 1000:.2f} km")
        print(f"Tiempo estimado: {tiempo / 60000:.2f} minutos")

if __name__ == "__main__":
    main()
