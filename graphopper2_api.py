import requests

API_KEY = "53920fda-c85e-4ed1-a438-2c08aaf90065"
URL = "https://graphhopper.com/api/1/route"

ciudades_coords = {
    "santiago": "-33.4489,-70.6693",
    "ovalle": "-30.6039,-71.1995"
}

def solicitar_ciudades():
    origen = input("Ciudad de origen (santiago/ovalle, q para salir): ").lower()
    if origen == 'q':
        exit()
    destino = input("Ciudad de destino (santiago/ovalle, q para salir): ").lower()
    if destino == 'q':
        exit()

    if origen not in ciudades_coords or destino not in ciudades_coords:
        print("❌ Ciudad no válida. Usa solo: santiago u ovalle.")
        return solicitar_ciudades()

    return ciudades_coords[origen], ciudades_coords[destino]

def seleccionar_vehiculo():
    print("Vehículos disponibles: car, bike, foot")
    vehiculo = input("Tipo de vehículo: ").lower()
    if vehiculo not in ["car", "bike", "foot"]:
        print("Tipo inválido. Usando 'car'.")
        vehiculo = "car"
    return vehiculo

def consultar_ruta(origen, destino, vehiculo):
    params = {
        "point": [origen, destino],
        "vehicle": vehiculo,
        "locale": "es",
        "key": API_KEY
    }
    response = requests.get(URL, params=params)
    return response.json()

def mostrar_resultado(data):
    if "paths" not in data:
        print("\n❌ Error en la respuesta de la API:")
        print(data)
        return

    ruta = data["paths"][0]
    distancia_km = round(ruta["distance"] / 1000, 2)
    duracion_seg = ruta["time"] / 1000
    horas = int(duracion_seg // 3600)
    minutos = int((duracion_seg % 3600) // 60)
    segundos = int(duracion_seg % 60)

    print(f"\n✅ Distancia: {distancia_km:.2f} km")
    print(f"⏱️ Duración: {horas}h {minutos}m {segundos}s")
    print("\n📍Narrativa del viaje:")
    for i, step in enumerate(ruta["instructions"]):
        print(f"{i+1}. {step['text']}")

def main():
    while True:
        origen, destino = solicitar_ciudades()
        vehiculo = seleccionar_vehiculo()
        datos = consultar_ruta(origen, destino, vehiculo)
        mostrar_resultado(datos)
        cont = input("\nPresiona 'q' para salir o Enter para otra consulta: ")
        if cont.lower() == "q":
            break

if __name__ == "__main__":
    main()
