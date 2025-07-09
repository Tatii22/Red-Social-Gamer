# PROYECTO RED SOCIAL GAMER

## Integrantes y roles 
- Tatiana: Project owner  
- Cristian: Programador  
- Dayana: Programador  
- Diego: Scrum master  

## Planificación del Proyecto
Nuestro primer día tuvimos una reunión en la cual hablamos un poco sobre 
la realización de nuestro proyecto y próximas reuniones.  
Como equipo nos pusimos de acuerdo para la realización de nuestra segunda reunión,
donde se llevó a cabo la distribución de roles, tareas que los integrantes deben desarrollar
durante la realización del proyecto y completamos el Product Backlog.

## Orden de nuestras Funcionalidades 
- Registro de Usuario  
- Iniciar sesión  
- Crear publicación Gamer  
- Creación de menú principal  

## Épicas e Historias de Usuario

### Épica 1: Gestión de Usuarios  
- **Registro de Usuario**: Como usuario nuevo, quiero registrarme en la plataforma proporcionando mi nombre de usuario y contraseña, para poder acceder y participar en la red social.  
- **Inicio de Sesión**: Como usuario registrado, quiero iniciar sesión con mis credenciales, para acceder a mi cuenta y realizar publicaciones.  
- **Listado de Usuarios**: Como usuario de la plataforma, quiero ver una lista de los usuarios registrados, para poder conectarme y conocer nuevas personas dentro de la red social.  

### Épica 2: Publicación de Contenidos  
- **Crear una Publicación**: Como usuario registrado, quiero publicar mensajes en la red social, para compartir mis pensamientos con otros usuarios.  
- **Ver Publicaciones de Otros Usuarios**: Como usuario de la red social, quiero ver las publicaciones de otros usuarios, para mantenerme informado y conocer sus opiniones.  
- **Interactuar con Publicaciones (Me gusta)**: Como usuario de la red social, quiero poder dar "Me gusta" a las publicaciones, para mostrar mi apoyo o interés en un contenido.  
- **Comentar en una Publicación**: Como usuario de la red social, quiero poder comentar en las publicaciones de otros usuarios, para interactuar y expresar mi opinión sobre los temas compartidos.  

### Épica 3: Interfaz de Usuario y Experiencia  
- **Navegación en la Consola**: Como usuario de la red social, quiero navegar fácilmente a través de las opciones disponibles, para acceder a las funciones sin complicaciones.  
- **Cierre de Sesión**: Como usuario registrado, quiero cerrar sesión en la red social, para asegurar que mi cuenta no sea utilizada sin mi autorización.  

## Sprint Backlog 
Después de definir el Product Backlog seleccionamos las tareas prioritarias
que se pueden realizar en el primer sprint. Cada integrante eligió actividades
de acuerdo con su rol y capacidades. Estas tareas forman parte del Sprint Backlog,
el cual servirá como guía de trabajo para esta primera fase del proyecto.

### Especificación de cada Sprint
- **Registro de usuario**:  
Crear una cuenta nueva validando que el nombre no se repita, guardar usuario y contraseña en `usuarios.json`, y mostrar un mensaje según el resultado.  

- **Inicio de sesión**:  
Validar las credenciales del jugador desde `usuarios.json`, guardar sus datos activos en memoria y mostrarle un submenú personalizado.  

- **Creación de publicaciones gamer**:  
Permitir al jugador crear una publicación con tipo y descripción, y guardarla en `publicaciones.json`.  

- **Ver publicaciones**:  
Leer `publicaciones.json` y mostrar al jugador el contenido compartido por otros: autor, tipo, descripción, likes y comentarios.  

- **Dar like**:  
Permitir al jugador dar like a publicaciones, evitando duplicados, aumentando el contador y registrando el like en su perfil.  

- **Comentar publicación**:  
Permitir al jugador dejar comentarios en publicaciones, agregándolos a la estructura y guardándolos en `publicaciones.json`.  

- **Listado de jugadores registrados**:  
Permitir al jugador ver los nombres y usuarios registrados, leyendo desde `usuarios.json` sin mostrar contraseñas.  

- **Cierre de sesión**:  
Agregar una opción en el menú para que el usuario cierre sesión y regrese al menú principal.  

- **Menú principal completamente navegable**:  
Crear un menú funcional para que el jugador acceda fácilmente a todas las opciones disponibles dentro de la red social.  

- **Documentación del proyecto**:  
Organizar y documentar el proyecto en `README.md` y `docs/proceso.md`, incluyendo roles, historias, Scrum, funciones y retrospectiva del equipo.  

- **Presentación final del producto**:  
Mostrar el funcionamiento del sistema en consola, explicar el uso de Scrum y compartir aprendizajes del proyecto. Responsable: Diego (Scrum Master).  

- **Validaciones**:  
Validar cada dato ingresado por el jugador mediante funciones específicas para asegurar que sean correctos.  

- **Detalles del README**:  
Se ingresó información más detallada del proyecto en el Readme.  

## Desarrollo de Nuestro Proyecto
En nuestro proyecto utilizamos varias herramientas para facilitar el desarrollo:  
- Python  
- VScode  
- GitHub  
- Discord  

## Organización de tareas de los Programadores
A continuación se mostrarán las tareas asignadas a cada integrante del equipo de desarrollo durante el sprint:  
- 🟠**Inicio de sesión** = Cristian: Añadió la implementación de la funcionalidad del inicio de sesión permitiendo el acceso de los usuarios al sistema.  
- 🟠**Cierre de sesión** = Cristian: Desarrollo del cierre de sesión asegurando que los usuarios puedan salir de forma segura y correcta.  
- 🟠**Registro de Usuario** = Tatiana: Desarrollo del registro de usuario, permitiendo la creación de nuevas cuentas.  
- 🟠**Validaciones** = Tatiana: Verificación de que los enlaces y funciones principales estuvieran elaboradas correctamente.  
- 🟠**Publicación Gamer** = Dayana: Creación de la sección de publicación gamer, para que los usuarios puedan compartir contenido relacionado con videojuegos.  

## Aporte del Scrum Master 
- El Scrum Master principalmente fue el encargado de la realización de las reuniones del equipo  
- Dio opiniones sobre el avance del proyecto y apoyo en la solución de dudas  
- Verificó que cada prueba saliera correctamente (Tati)  
- Creador de las diapositivas del proyecto final para la exposición y explicación a detalle  

## Realización de Daily Scrum
- **Viernes 04 (4:10pm)**: Se realizó una reunión donde se acordó más a detalle los días en los cuales se realizarán las reuniones y se hizo una encuesta para elegir el tema del proyecto.  
- **Sábado 05 (9:11pm)**: Reunión en Discord para trabajar los sprint, verificar funcionalidad y acordar nuevos sprint. También se elaboró el Sprint Backlog.  
- **Domingo 06 (1:00pm)**: Profundización del proyecto en cada tema específico, definición del rol del Scrum Master y solución de dudas.  
- **Lunes 07 (4:15pm)**: Reunión para la solución de dudas y revisión del avance individual de cada integrante.  
- **Martes 08 (6:55pm)**: El equipo se reencontró para retomar el proyecto, resolver dudas y revisar avances.  

## Logros del Proyecto  
Como equipo logramos dos grandes metas:  
1. Los avances realizados por parte de los programadores quedaron funcionales para la continuación con las siguientes funciones asignadas.  
2. Se verificó que el código de cada integrante fuera funcional y compatible con el resto del proyecto. Luego se realizaron pruebas funcionales, que confirmaron que todo se ejecutaba correctamente y permitió avanzar al siguiente sprint.  

## Retrospectiva

<<<<<<< HEAD
- Que cosas salieron bien: La buena comunicacion y la asignacion adecuada de las tareas 
- Que podemos mejorar si se diera la oportunidad: El conocimiento sobre las funciones de GitHub a la hora de trabajar en equipo

# Reflexion Scrum Master

- Como Scrum Master, me siento conforme con el trabajo realizado por el equipo. Logramos mantener una buena comunicacion, organizar bien nuestras tareas y avanzar de forma constante. Las reuniones nos ayudaron a tomar decisiones en conjunto y a resolver dudas. El equipo mostro compromiso y responsabilidad durante todo el sprint :b
=======
- **Qué cosas salieron bien**: La buena comunicación y la asignación adecuada de las tareas.  
- **Qué podemos mejorar si se diera la oportunidad**: El conocimiento sobre las funciones de GitHub a la hora de trabajar en equipo.  

## Reflexión Scrum Master

Como Scrum Master, me siento conforme con el trabajo realizado por el equipo. Logramos mantener una buena comunicación,  
organizar bien nuestras tareas y avanzar de forma constante. Las reuniones nos ayudaron a tomar decisiones en conjunto y a resolver dudas.  
El equipo mostró compromiso y responsabilidad durante todo el sprint. :b  
>>>>>>> 96a8891 (:memo: Se culmina documentacion)
