import json 
import uuid 
from datetime import datetime
import questionary
from rich.console import Console
from rich.panel import Panel 
import os

# Consola Rich
console = Console()

ARCHIVO = os.path.join("data", "publicaciones.json")
# Ruta del archivo JSON


def cargar_contenido():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        try:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
        except json.JSONDecodeError:
            return []

def guardar_contenido(publicaciones):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(publicaciones, archivo, indent=4, ensure_ascii=False)


# Crear una nueva publicación
def crear_publicacion(usuario):
    console.rule("[bold cyan]🎮 Publicar Contenido Gamer")

    tipo = questionary.select(
        "🖥️ ¿Qué tipo de contenido vas a publicar?",
        choices=["logro", "noticia", "captura", "recomendación"]
    ).ask()

    contenido = questionary.text("📸 Escribe tu publicación:").ask()

    if not contenido.strip():
        console.print("[bold red]❌ No se puede publicar contenido vacío.[/bold red]")
        return
    
    publicaciones = cargar_contenido()
    nuevo_id = len(publicaciones) + 1
    

    nueva_publicacion = {
        "id": nuevo_id,
        "autor": usuario,
        "tipo": tipo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    publicaciones.append(nueva_publicacion)
    guardar_contenido(publicaciones)
    
    texto = (
        f"🎲 ID: [bold magenta]{nuevo_id}[/bold magenta]\n"
        f"[bold magenta]{tipo.upper()}[/bold magenta]: {contenido}\n\n"
        f"🧙‍♀️ Autor: [cyan]{usuario}[/cyan]\n"
        f"🗓️ Fecha: [green]{nueva_publicacion['fecha']}[/green]"
    )

    console.print(Panel(texto, title=f"🕹️ ¡{tipo.capitalize()} publicada!", border_style="green"))

# Ejecutar
crear_publicacion("DayanaGamer")