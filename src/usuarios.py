import json
import os
import questionary
from rich.console import Console
from rich.prompt import Prompt

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


