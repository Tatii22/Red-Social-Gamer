import questionary
from estilos import mostrarLetrero, gamerStyle
from usuarios import registrarUsuario, inicioDeSesionDelUsuario
from rich.console import Console
from publicaciones import crear_publicacion, ver_publicaciones
from usuarios import ver_jugadores_registrados


consola = Console()

def subMenuDeIniciarSesion(nombreUser):
    while True:
        consola.clear()
        consola.print(f"\n[bold cyan]👾 Bienvenido al submenú, {nombreUser}![/bold cyan]\n")
        
        opc = questionary.select(
            "Elige una opción",
            choices=[
                "📋 Crear Publicaciónes",
                "👀 Ver Publicaciones",
                "👤 Ver Jugadores Registrados",
                "🔓 Cerrar Sesion"
            ],
            style=gamerStyle
        ).ask()

        if opc == "📋 Crear Publicaciónes":
            crear_publicacion(nombreUser)

        elif opc == "👀 Ver Publicaciones":
            ver_publicaciones(nombreUser)
            
        elif opc == "👤 Ver Jugadores Registrados":
            ver_jugadores_registrados()
            
        elif opc == "🔓 Cerrar Sesion":
            consola.print("\n Sesión cerrada. ¡Hasta pronto! \n")
            break

def menuPrincipal():
    while True:
        opc = questionary.select(
            "\n🎮 ¿Qué deseas hacer?",
            choices=[
                "📝 Registrarse",
                "🕹️  Iniciar Sesión",
                "❌ Salir"
            ],
            style=gamerStyle
        ).ask()

        if opc == "📝 Registrarse":
            registrarUsuario()
        elif opc == "🕹️  Iniciar Sesión":
            usuario = inicioDeSesionDelUsuario()
            if usuario:
                subMenuDeIniciarSesion(usuario)
        elif opc == "❌ Salir":
            consola.print("\n👋 [bold magenta]¡Hasta luego, gamer![/bold magenta]\n")
            break

if __name__ == "__main__":
    mostrarLetrero()
    menuPrincipal()
