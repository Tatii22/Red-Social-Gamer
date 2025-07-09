import json 
import os
from datetime import datetime
import questionary
from rich.console import Console
from rich.panel import Panel 
from estilos import gamerStyle  # Estilo personalizado

# Consola Rich
console = Console()

# Ruta del archivo JSON
ARCHIVO = os.path.join("data", "publicaciones.json")

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
        choices=["logro", "noticia", "captura", "recomendación"],
        style=gamerStyle
    ).ask()

    while True: 
        contenido = questionary.text("🖋️ Escribe tu publicación:", style=gamerStyle).ask()
    
        if  contenido and contenido.strip():
            break 
        console.clear()
        console.rule("[bold red]📭 Publicacion vacia", style="red")
        console.print("[bold red]🫡 Intenta escribir tu publicacion nuevamente.[/bold red]")
    
    publicaciones = cargar_contenido()
    nuevo_id = len(publicaciones) + 1
    print("\n ")
    
    nueva_publicacion = {
        "id": nuevo_id,
        "autor": usuario,
        "tipo": tipo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%d-%m-%Y %H:%M"),
        "like": [],
        "comentarios": []
    }

    publicaciones.append(nueva_publicacion)
    guardar_contenido(publicaciones)
    
    texto = (
        f"🎲 ID: [bold magenta]{nuevo_id}[/bold magenta]\n"
        f"[bold magenta]{tipo.upper()}[/bold magenta]: {contenido}\n\n"
        f"🧙‍♀️ Autor: [cyan]{usuario}[/cyan]\n"
        f"🗓️ Fecha: [green]{nueva_publicacion['fecha']}[/green]"
    )

    console.print(Panel(texto, title=f"🕹️ ¡{tipo.capitalize()} publicado/a!", border_style="green"))
    input("\nPresiona Enter para volver al submenú...")

def ver_publicaciones(usuario_actual):
    publicaciones = cargar_contenido()

    if not publicaciones:
        console.print(Panel("😔 No hay publicaciones aún.", title="AFKNet", style="bold red"))
        return

    opciones = []
    for idx, pub in enumerate(publicaciones, start=1):
        # Validar que existan los campos necesarios
        likes = pub.get("likes", [])
        comentarios = pub.get("comentarios", [])
        opciones.append(
            f"{idx}. [{pub['autor']}] {pub['contenido']}\n   👍 Likes: {len(likes)}   💬 Comentarios: {len(comentarios)}"
        )
    opciones.append("❌ Volver al menú principal")

    seleccion = questionary.select(
        "📰 Publicaciones Disponibles:",
        choices=opciones,
        style=gamerStyle
    ).ask()

    if seleccion == "❌ Volver al menú principal":
        return

    indice = int(seleccion.split(".")[0]) - 1
    mostrar_detalle_publicacion(publicaciones, indice, usuario_actual)



def mostrar_detalle_publicacion(publicaciones, indice, usuario_actual):
    pub = publicaciones[indice]
    pub.setdefault("likes", [])
    pub.setdefault("comentarios", [])

    texto = (
        f"[bold cyan]{pub['autor']}[/bold cyan]: {pub['contenido']}\n\n"
        f"👍 Likes: {len(pub['likes'])}   💬 Comentarios: {len(pub['comentarios'])}\n\n"
        "[dim]No hay comentarios aún.[/dim]\n"
    )

    console.print(Panel.fit(texto, title="📝 Publicación"))

    accion = questionary.select(
        "¿Qué deseas hacer?",
        choices=["👉 Dar like", "⬅️ Volver"],
        style=gamerStyle
    ).ask()

    if accion == "👉 Dar like":
        if usuario_actual.lower() in [u.lower() for u in pub["likes"]]:
            console.print("[yellow]⚠️ Ya le diste like a esta publicación.[/yellow]")
        else:
            pub["likes"].append(usuario_actual)
            guardar_contenido(publicaciones)
            console.print("[green]✅ ¡Le diste like a esta publicación![/green]")
        mostrar_detalle_publicacion(publicaciones, indice, usuario_actual)

    else:
        ver_publicaciones(usuario_actual)