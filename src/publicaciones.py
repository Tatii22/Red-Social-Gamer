import json 
import uuid 
from datetime import datetime
import questionary
from rich.console import Console
from rich.panel import Panel 

# Consola Rich
console = Console()

# Ruta del archivo JSON
ARCHIVO = "publicaciones.json" 


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
    
