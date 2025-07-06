import questionary
from estilos import mostrarLetrero, gamerStyle
from usuarios import registrarUsuario, inicioDeSesionDelUsuario
from rich.console import Console

consola = Console()

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
            inicioDeSesionDelUsuario()
        elif opc == "❌ Salir":
            consola.print("\n👋 [bold magenta]¡Hasta luego, gamer![/bold magenta]\n")
            break

if __name__ == "__main__":
    mostrarLetrero()
    menuPrincipal()
