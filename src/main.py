import questionary
from estilos import mostrarLetrero, gamerStyle
from usuarios import registrarUsuario, inicioDeSesionDelUsuario
from rich.console import Console
from publicaciones import crear_publicacion 

consola = Console()
def LikeAndComments(nombreUser):
    while True:
        consola.print(f"\n Publcaciones\n")
        consola.print(f"publicacion de {nombreUser}")
        opc = questionary.select(
            "Elige una opción",
            choices=[
                "Comentar 💭",
                "like ❤️",
                "volver"
            ],
            style=gamerStyle
        ).ask()

        if opc == "Comentar 💭":
            pass
        elif opc == "like ❤️":
            pass
        elif opc == "volver":
            break


def subMenuDeIniciarSesion(nombreUser):
    while True:
        consola.clear()
        consola.print(f"\n[bold cyan]👾 Bienvenido al submenú, {nombreUser}![/bold cyan]\n")
        opc = questionary.select(
            "Elige una opción",
            choices=[
                "📋 Crear Publicaciónes",
                "👀 Ver Publicaciones",
                "🔓 Cerrar Sesion"
            ],
            style=gamerStyle
        ).ask()

        if opc == "📋 Crear Publicaciónes":
            crear_publicacion(nombreUser)

        elif opc == "👀 Ver Publicaciones":
            LikeAndComments(nombreUser)
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
