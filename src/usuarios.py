import json
import os
import questionary
from rich.console import Console
from rich.prompt import Prompt
from estilos import gamerStyle

console = Console()
RUTA_USUARIOS = os.path.join("data", "usuarios.json")

def cargarUsuarios():
    if not os.path.exists(RUTA_USUARIOS):
        return []
    
    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        try:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
        except json.JSONDecodeError:
            return []

def guardarUsuarios(usuarios):
    with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

def registrarUsuario():
    usuarios = cargarUsuarios()

    console.print("\n[bold cyan]🎮 Registro de nuevo jugador[/bold cyan]\n")
    nombreUser = questionary.text("👤 Nombre de usuario:", style=gamerStyle).ask().strip().lower()
    if any(user["nombreUser"] == nombreUser for user in usuarios):
        console.print("❌ [bold red]El nombre de usuario ya existe.[/bold red]")
        return

    password = questionary.password("🔒 Contraseña:", style=gamerStyle).ask().strip()

    nuevo_usuario = {
        "nombreUser": nombreUser,
        "password": password
    }

    usuarios.append(nuevo_usuario)
    guardarUsuarios(usuarios)

    console.print(f"\n✅ [bold green]Usuario '{nombreUser}' registrado con éxito.[/bold green]")

def inicioDeSesionDelUsuario():
    from main import subMenuDeIniciarSesion
    usuarios = cargarUsuarios()
    console.print("\n[bold cyan]🔒 Iniciar Sesión[/bold cyan]\n")

    nombreUser = questionary.text("👤 Nombre de usuario:", style=gamerStyle).ask().strip().lower()
    password = questionary.password("🔒 Contraseña:", style=gamerStyle).ask().strip()

    usuario_encontrado = next((user for user in usuarios if user["nombreUser"] == nombreUser and user["password"] == password), None)

    if usuario_encontrado:
        console.print(f"\n [bold green] Inicio de sesión exitoso. Bienvenido {nombreUser} [/bold green]\n")
        return nombreUser  
    else:
        console.print(f"\n [bold red] Usuario o Contraseña incorrectos. [/bold red]\n")
        return None


        