import requests
import os
import re

readme_path = "README.md"

api_key = os.getenv("NASA_API_KEY")

def obtener_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        imagen_url = datos['url']
        title = datos['title']
        description = datos['explanation']
        return imagen_url, title, description
    else:
        return None, "No se pudo obtener la imagen."

imagen_url, title, description = obtener_apod()

if imagen_url:

    try:
        with open(readme_path, "r") as file:
            contenido = file.read()

        contenido = re.sub(
            r'<img [^>]*src="[^"]*"[^>]*>', 
            f'<img width="500" height="300" src="{imagen_url}" title="{description}"/>', 
            contenido,
            count=1  
        )

        contenido = re.sub(
            r'<p><i>[^<]*</i></p>', 
            f'<p><i>{title}</i></p>', 
            contenido,
            count=1  
             )
        with open(readme_path, "w") as file:
            file.write(contenido)

        print("README.md actualizado correctamente.")

    except Exception as e:
        print(f"Hubo un error al actualizar el README.md: {e}")


else:
    print("No se pudo obtener la imagen de la NASA.")
