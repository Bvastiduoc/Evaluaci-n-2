import requests
import json

def solicitar_ciudades():
    # Versión sin input
    origen = "santiago"
    destino = "ovalle"
    return origen, destino

def obtener_coordenadas(ciudad):
    url = f"https://nominatim.openstreetmap.org/search?q={ciudad}&format=json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos:
        lat = datos[0]['lat']
        lon = datos[0]['lon']
        return lat, lon
    else:
        raise ValueError(f"No se pudo obtener coordenadas para {ciudad}")

def consultar_ruta(origen_lat, origen_lon, destino_lat, destino_lon):
    api_key = "your_graphhopper_api_key"  # Reemplaza con tu API Key si es necesario
    url = f"https://graphhopper.com/api/1/route?point={origen_lat},{origen_lon}&point={destino_lat},{destino_lon}&vehicle=car&locale=es&key={api_key}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if 'paths' in datos and datos['paths']:
        distancia = datos['paths'][0]['distance'] / 1000  # en km
        tiempo = datos['paths'][0]['time'] / 60000        # en minutos
        return distancia, tiempo
    else:
        raise ValueError("No se pudo calcular la ruta.")

def main():
    origen, destino = solicitar_ciudades()
    print(f"Calculando ruta desde {origen} hasta {destino}...")

    try:
        origen_lat, origen_lon = obtener_coordenadas(origen)
        destino_lat, destino_lon = obtener_coordenadas(destino)
        distancia, tiempo = consultar_ruta(origen_lat, origen_lon, destino_lat, destino_lon)

        print(f"Distancia aproximada: {distancia:.2f} km")
        print(f"Tiempo estimado: {tiempo:.2f} minutos")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()

