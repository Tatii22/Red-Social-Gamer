from questionary import Style
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text


gamerStyle = Style([
    ("qmark", "fg:#ff00ff bold"),
    ("question", "fg:#00ffff bold"),
    ("answer", "fg:#39ff14 bold"),
    ("pointer", "fg:#ff00ff bold"),
    ("highlighted", "fg:#00ffff bold"),
    ("selected", "fg:#ff00ff bold"),
    ("separator", "fg:#6C6C6C"),
    ("instruction", "fg:#808080 italic"),
])


letrero = r"""
 █████╗ ███████╗██╗  ██╗███╗   ██╗███████╗████████╗
██╔══██╗██╔════╝██║ ██╔╝████╗  ██║██╔════╝╚══██╔══╝
███████║█████╗  █████╔╝ ██╔██╗ ██║█████╗     ██║   
██╔══██║██╔══╝  ██╔═██╗ ██║╚██╗██║██╔══╝     ██║   
██║  ██║██║     ██║  ██╗██║ ╚████║███████╗   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   
"""

# 🚀 Mostrar intro bonito
def mostrarLetrero():
    consola = Console()

    mensaje = Text()
    mensaje.append(letrero.strip() + "\n", style="bold magenta")
    mensaje.append("\n", style="")
    mensaje.append("Bienvenido a AFKNet — La Red Social Gamer definitiva.\n")
    mensaje.append("Publica tus logros, comenta y da like. ¡Que empiece la partida!")

    panel = Panel(
        Align.center(mensaje, vertical="middle"),
        title="👾 AFKNet 👾",
        border_style="bold magenta",
        padding=(1, 4)
    )

    consola.print(panel)
