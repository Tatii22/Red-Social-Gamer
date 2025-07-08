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

def mirar_publicaciones():
    console.rule("[bold cyan]🌟 Publicaciones de la Comunidad Gamer")

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        console.print("[bold red]🚫 No hay publicaciones todavía.[/bold red]")
        input("\nPresiona Enter para volver al submenú...")
        return

    total = len(data)
    page_size = 10
    page = 0

    while True:
        console.clear()
        console.rule("[bold cyan]🌟 Publicaciones de la Comunidad Gamer")

        start = page * page_size
        end = start + page_size
        publicaciones_pagina = data[start:end]

        for pub in publicaciones_pagina:
            texto = (
                f"🎲 ID: [bold magenta]{pub['id']}[/bold magenta]\n"
                f"[bold magenta]{pub['tipo'].upper()}[/bold magenta]: {pub['contenido']}\n\n"
                f"🧙‍♀️ Autor: [cyan]{pub['autor']}[/cyan]\n"
                f"🗓️ Fecha: [green]{pub['fecha']}[/green]"
            )
            console.print(Panel(texto, border_style="green"))

        console.print(f"[bold yellow]Página {page + 1} de {(total - 1) // page_size + 1}[/bold yellow]\n")

        opciones = []

        if start + page_size < total:
            opciones.append("➡️ Siguiente")
        if page > 0:
            opciones.append("⬅️ Anterior")
        opciones.append("🏠 Volver al menú")

        opcion = questionary.select(
            "¿Qué quieres hacer?",
            choices=opciones,
            style=gamerStyle
        ).ask()

        if opcion == "➡️ Siguiente":
            page += 1
        elif opcion == "⬅️ Anterior":
            page -= 1
        else:  # Volver al menú
            break


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
    pass