import requests
import os

readme_path = "README.md"

api_key = os.getenv("NASA_API_KEY")

def obtener_apod():
    url = "https://api.nasa.gov/planetary/apod?api_key={api_key}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        imagen_url = datos['url']
        title = datos['title']
        return imagen_url, title
    else:
        return None, "No se pudo obtener la imagen."

imagen_url, title = obtener_apod()

if imagen_url:
    with open(readme_path, "r") as file:
        contenido = file.read()

    contenido = contenido.replace(
        '<img width="500" height="300" src="https://apod.nasa.gov/apod/image/2411/Ngc6888Hoo_Aro_960.jpg" />',
        f'<img width="500" height="300" src="{imagen_url}" />'
    )

    contenido = contenido.replace(
        '<p><i>Title: NGC 6888 - The Crescent Nebula</i></p>',
        f'<p><i>Title: {title}</i></p>'
    )


    with open(readme_path, "w") as file:
        file.write(contenido)

    print("README.md actualizado correctamente.")
else:
    print("No se pudo obtener la imagen de la NASA.")
