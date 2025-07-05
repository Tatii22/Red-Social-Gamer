from questionary import Style
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# 🎨 Estilo tipo gamer para Questionary
gamer_style = Style([
    ("qmark", "fg:#ff00ff bold"),
    ("question", "fg:#00ffff bold"),
    ("answer", "fg:#39ff14 bold"),
    ("pointer", "fg:#ff00ff bold"),
    ("highlighted", "fg:#00ffff bold"),
    ("selected", "fg:#ff00ff bold"),
    ("separator", "fg:#6C6C6C"),
    ("instruction", "fg:#808080 italic"),
])

# 🎮 ASCII Art estilo gamer
gamer_ascii = """
   _____           _       ____                  _       
  |  __ \         | |     / __ \                (_)      
  | |  | | ___  __| | ___| |  | |_   _  ___  ___ _  __ _ 
  | |  | |/ _ \/ _` |/ _ \ |  | | | | |/ _ \/ __| |/ _` |
  | |__| |  __/ (_| |  __/ |__| | |_| |  __/\__ \ | (_| |
  |_____/ \___|\__,_|\___|\___\_\\__,_|\___||___/_|\__,_|

           [bold cyan]¡Bienvenido a Red Social Gamer![/bold cyan]
       [green]Conecta. Comparte. Juega. 🔥 [/green]
"""

# 🚀 Mostrar intro bonito
def mostrar_intro():
    consola = Console()
    consola.print(Panel.fit(Text(gamer_ascii, justify="center"), border_style="bold magenta", title="👾 G4M3R 👾"))
