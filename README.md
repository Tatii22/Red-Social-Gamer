# 🎮 Red Social Gamer - Mini-Sprint Python + Scrum 

Proyecto académico desarrollado durante un mini Sprint aplicando la metodologia Scrum. Consiste en una red social en consola donde los usuarios pueden interactuar, compartir publicaciones, comentar y dar "me gusta". 🫶

---

## 📌 Objetivo 

El objetivo de este proyecto es desarrollar una red social en consola utilizando Python, dirigida a una comunidad de gamers. A través de esta aplicación, los usuarios podrán registrarse, iniciar sesión, crear publicaciones sobre videojuegos, ver publicaciones de otros y dar “me gusta”, todo con persistencia de datos en archivos JSON. Además, este proyecto busca aplicar la metodología Scrum en un entorno académico, promoviendo el trabajo colaborativo, la planificación por etapas (sprint) y la entrega de un producto funcional. De esta manera, se fortalecen las habilidades de programación, lógica, organización y comunicación dentro de un equipo de desarrollo. 

---

## 👥 Equipo Proyecto Scrum

| Nombre       | Rol            |
|--------------|----------------|
| Tatiana      | Product Owner  | 
| Diego Díaz   | Scrum Master   | 
| Dayana       | Programadora   | 
| Cirstian     | Programador    | 

---

## Funcionalidades Principales 

📝 **Gestión de usuarios**
-  Registro de nuevos usuarios  
-  Inicio y cierre de sesión  
-  Ver lista de usuarios registrados  

📝 **Publicaciones**
-  Crear publicaciones  
-  Ver publicaciones de otros usuarios
-  Dar "Me gusta" a publicaciones
-  Comentar publicaciones 

🦾 **Tecnología y experiencia**
-  Interfaz en consola con librerías **Rich** y **Questionary**  
-  Almacenamiento persistente en archivos **.json** 

---

## 📥 Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/Tatii22/Red-Social-Gamer.git 

```
2. Ingresa a la carpeta del proyecto:

```bash
cd Red-Social-Gamer
```

3. Instala las dependencias necesarias:

```bash
pip install rich questionary
```

4. Ejecuta el programa principal:

```bash
python main.py
```

---

## 🌐 Tecnologías utilizadas

| Tecnología    | Descripción                                         |
|---------------|-----------------------------------------------------|
|  Python       | Lenguaje principal para desarrollar la red social   |
|  Rich         | Librería para dar estilo y color a la consola       |
|  Questionary  | Librería para crear menús interactivos en consola   |
|  JSON         | Formato usado para almacenar los datos              |
|  Git & GitHub | Control de versiones y almacenamiento del proyecto  |

---

## 🗂️ Estructura del proyecto

```
RED-SOCIAL-GAMER/
├── data/
│   ├── publicaciones.json         # Almacena las publicaciones de los usuarios
│   └── usuarios.json              # Almacena los datos de los usuarios
│
├── docs/
│   ├── presentacion.pdf           
│   └── proceso.md                 # Documentación del proceso Scrum (planificación, sprint, etc.)
│
├── src/
│   ├── __pycache__/               
│   ├── comentarios.py             # comentar publicaciones
│   ├── estilos.py                 # Estilo visual con Rich o Questionary
│   ├── main.py                    # Archivo principal para ejecutar el programa
│   ├── publicaciones.py           # Funciones para crear/ver publicaciones
│   └── usuarios.py                # Registro, inicio de sesión, listar usuarios
│
├── .gitignore                     
└── README.md                      # Documentación principal del proyecto
```

---

## 🔎 Sprint Review

- Producto funcional y probado por el equipo.
- Todas las funcionalidades clave entregadas.
- Feedback positivo del Product Owner.

---
## 🗣️ Sprint Retrospective

- **Fortalezas:** buena organización, roles claros, uso correcto de Git.
- **Mejoras:** más tiempo para pruebas, reuniones más breves.
- **Aprendizajes:** Scrum real, trabajo colaborativo, manejo de consola avanzada.

---
## ✉︎ Contacto del equipo

- Tatiana Villamizar – https://github.com/Tatii22 
- Diego Díaz – https://github.com/Twidied
- Dayana Barbosa – https://github.com/Dayana196
- Cristian Mayorga – https://github.com/yorga1317


---

## ✨ Agradecimientos :3

Queremos agradecer al docente por su guía y apoyo durante el desarrollo de este mini-sprint.  
También agradecemos a cada integrante del equipo por su compromiso, colaboración y dedicación en cada fase del proyecto.  
Este trabajo en equipo nos permitió aplicar Scrum de forma práctica y reforzar nuestras habilidades en programación con Python.