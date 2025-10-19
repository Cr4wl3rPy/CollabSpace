# 🚀 CollabSpace

> Sistema de Colaboración en Tiempo Real con Whiteboard Colaborativo y Chat Instantáneo

![Status](https://img.shields.io/badge/status-🚧%20en%20construcción-orange)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![React](https://img.shields.io/badge/react-18+-61dafb)
![License](https://img.shields.io/badge/license-MIT-green)

---

> ⚠️ **Proyecto en desarrollo activo** - Este README se actualiza semanalmente conforme avanza el proyecto.  
> 📅 **Última actualización:** Octubre 2025 | **Progreso:** Semana 1 - Setup Inicial

---

## 📋 Descripción

**CollabSpace** es una plataforma web que permite a equipos colaborar en tiempo real a través de un whiteboard digital compartido. Múltiples usuarios pueden dibujar simultáneamente, comunicarse mediante chat instantáneo, y ver las acciones de otros participantes al instante gracias a la tecnología WebSocket.

Este proyecto está siendo desarrollado como proyecto final para la materia de **Interacción Hombre-Máquina**, con enfoque en diseño de interfaces intuitivas, experiencia de usuario y comunicación en tiempo real.

### 🎯 Enfoque MVP (Producto Mínimo Viable)
Dado el plazo de 4 semanas, el proyecto adopta una filosofía MVP enfocándose en **pocas funcionalidades pero excelentes** en lugar de muchas features mediocres. Priorizamos calidad sobre cantidad.

---

## ✨ Características Principales

### ✅ Features CORE (En Desarrollo)

#### 🎨 Whiteboard Colaborativo
- Dibujo libre en tiempo real
- Múltiples herramientas: lápiz, colores, grosor, borrador
- Sincronización instantánea entre usuarios (< 500ms)
- Cursores visibles de cada participante con colores únicos

#### 💬 Chat en Tiempo Real
- Mensajería instantánea dentro de cada sala
- Historial de mensajes persistente
- Notificaciones visuales de nuevos mensajes

#### 🚪 Gestión de Salas
- Crear salas privadas con códigos únicos de 6 dígitos
- Unirse a salas mediante código
- Lista de usuarios conectados en vivo

#### 🔐 Autenticación Segura
- Sistema de registro e inicio de sesión
- Tokens JWT para sesiones seguras
- Hashing de contraseñas con Werkzeug

### ⭐ Features Opcionales (Si da tiempo - Semana 4)
- Formas geométricas (círculos, rectángulos)
- Herramienta de texto en canvas
- Exportar canvas como imagen
- Notas compartidas con editor de texto
- Dark mode

---

## 🛠️ Stack Tecnológico

### Backend
- **Python 3.10+**
- **Flask 3.0** - Framework web minimalista y flexible
- **Flask-SocketIO** - WebSockets para comunicación en tiempo real
- **Flask-SQLAlchemy** - ORM para interacción con base de datos
- **Flask-JWT-Extended** - Autenticación con tokens JWT
- **Flask-CORS** - Manejo de CORS para frontend-backend
- **PostgreSQL** - Base de datos relacional
- **Eventlet** - Servidor asíncrono para WebSockets

### Frontend
- **React 18** - Librería de UI moderna
- **Vite** - Build tool rápido y servidor de desarrollo
- **Socket.io-client** - Cliente WebSocket
- **Fabric.js** - Librería para manipulación de canvas HTML5
- **Tailwind CSS** - Framework CSS utility-first
- **Axios** - Cliente HTTP para llamadas a API
- **React Router DOM** - Navegación entre páginas
- **Lucide React** - Librería de íconos

### DevOps & Herramientas
- **Git & GitHub** - Control de versiones y colaboración
- **VSCode** - Editor de código
- **Postman** - Testing de API REST
- **Figma** - Diseño UI/UX
- **Render.com** - Hosting backend (próximamente)
- **Vercel** - Hosting frontend (próximamente)

---

## 📦 Instalación

> **Nota:** Instrucciones actualizadas conforme se desarrolla el proyecto

### Prerrequisitos
- Python 3.10 o superior
- Node.js 18 o superior
- PostgreSQL 14 o superior (o SQLite para desarrollo local)
- Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Cr4wl3rPy/collabspace.git
cd collabspace
```

### 2. Configurar Backend

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones (ver sección de Configuración)

# Inicializar base de datos
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Correr servidor backend
python app.py
```

El backend estará corriendo en `http://localhost:5000`

### 3. Configurar Frontend

```bash
# En otra terminal, navegar a la carpeta frontend
cd frontend

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env.local
# Editar .env.local con la URL del backend

# Correr servidor de desarrollo
npm run dev
```

El frontend estará corriendo en `http://localhost:5173`

---

## ⚙️ Configuración

### Variables de Entorno - Backend (.env)
```env
FLASK_ENV=development
SECRET_KEY=tu-clave-secreta-super-segura-cambiala
DATABASE_URL=postgresql://usuario:contraseña@localhost/collabspace
# O para desarrollo con SQLite:
# DATABASE_URL=sqlite:///collabspace.db
JWT_SECRET_KEY=otra-clave-secreta-para-jwt-cambiala
CORS_ORIGINS=http://localhost:5173
```

### Variables de Entorno - Frontend (.env.local)
```env
VITE_API_URL=http://localhost:5000
VITE_SOCKET_URL=http://localhost:5000
```

> ⚠️ **Importante:** Nunca subas archivos `.env` a GitHub. Están incluidos en `.gitignore`

---

## 🚀 Uso

> 📝 **Instrucciones detalladas se agregarán cuando la aplicación esté funcional**

### Flujo Básico (Planificado):
1. **Crear una Cuenta** - Registro con email y contraseña
2. **Crear una Sala** - Generar código único de 6 dígitos
3. **Invitar a Otros** - Compartir código con compañeros
4. **Colaborar en Tiempo Real** - Dibujar, chatear, y ver acciones de otros instantáneamente

---

## 📁 Estructura del Proyecto

```
collabspace/
├── backend/
│   ├── app.py                 # Punto de entrada principal Flask
│   ├── models.py              # Modelos SQLAlchemy (User, Room, Message)
│   ├── config.py              # Configuración de Flask
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py           # Rutas de autenticación (login, register)
│   │   └── rooms.py          # Rutas de salas (CRUD)
│   ├── sockets/
│   │   ├── __init__.py
│   │   ├── chat.py           # Eventos WebSocket de chat
│   │   ├── whiteboard.py     # Eventos WebSocket de whiteboard
│   │   └── presence.py       # Gestión de presencia de usuarios
│   ├── requirements.txt       # Dependencias Python
│   ├── .env.example          # Ejemplo de variables de entorno
│   └── .gitignore            # Archivos ignorados por Git
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Componentes React reutilizables
│   │   │   ├── Whiteboard/   # Componente del canvas
│   │   │   ├── Chat/         # Componente de chat
│   │   │   ├── Toolbar/      # Herramientas de dibujo
│   │   │   └── UserList/     # Lista de usuarios
│   │   ├── pages/            # Páginas principales
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Home.jsx
│   │   │   └── Room.jsx
│   │   ├── services/         # Servicios
│   │   │   ├── api.js        # Llamadas a API REST
│   │   │   └── socket.js     # Configuración Socket.io
│   │   ├── context/          # Context API para estado global
│   │   │   ├── AuthContext.jsx
│   │   │   └── RoomContext.jsx
│   │   ├── App.jsx           # Componente principal
│   │   └── main.jsx          # Entry point
│   ├── package.json          # Dependencias Node.js
│   ├── vite.config.js        # Configuración Vite
│   ├── tailwind.config.js    # Configuración Tailwind
│   ├── .env.example          # Ejemplo de variables de entorno
│   └── .gitignore            # Archivos ignorados por Git
│
├── docs/                     # Documentación adicional (próximamente)
│   ├── images/              # Screenshots del proyecto
│   ├── ARCHITECTURE.md      # Diagrama de arquitectura
│   └── API.md              # Documentación de endpoints
│
├── README.md                # Este archivo
├── LICENSE                  # Licencia MIT (próximamente)
└── .gitignore              # Gitignore global
```

---

## 👥 Equipo de Desarrollo

| Rol | Responsabilidades | Tecnologías Principales |
|-----|-------------------|------------------------|
| **👨‍💻 Backend Lead** | API REST, WebSocket server, Base de datos, Autenticación | Flask, PostgreSQL, Flask-SocketIO, JWT |
| **⚛️ Frontend Lead** | Arquitectura React, Estado global, Integración WebSocket | React, Context API, Socket.io-client |
| **🎨 Whiteboard Specialist** | Canvas colaborativo, Herramientas de dibujo, Optimización | Fabric.js, Canvas API, JavaScript |
| **🎨 UI/UX Designer** | Diseño de interfaces, Componentes visuales, Responsive | Figma, Tailwind CSS, React Components |
| **📝 QA & Documentation** | Testing, Documentación, Deployment, Video demo | pytest, Jest, Markdown, OBS Studio |

---

## 🗓️ Roadmap de Desarrollo

### ✅ Semana 1: Fundamentos (19-25 Oct) - EN PROGRESO
- [x] Crear repositorio GitHub
- [x] README inicial
- [x] Definir stack tecnológico
- [ ] Setup proyecto Flask
- [ ] Setup proyecto React con Vite
- [ ] Configurar PostgreSQL/SQLite
- [ ] Modelos de base de datos (User, Room, Message)
- [ ] API REST básica (autenticación)
- [ ] Wireframes en Figma
- [ ] Componentes React base

**🎯 Milestone Semana 1:** Autenticación funciona, se puede crear/unir salas (sin WebSocket)

---

### 🔄 Semana 2: Tiempo Real (26 Oct - 1 Nov)
- [ ] Configurar Flask-SocketIO
- [ ] Eventos WebSocket (connect, disconnect, join_room)
- [ ] Integrar Socket.io-client en React
- [ ] Chat en tiempo real funcionando
- [ ] Canvas básico con Fabric.js
- [ ] Envío de eventos de dibujo por WebSocket
- [ ] Lista de usuarios conectados
- [ ] UI de la página principal de sala

**🎯 Milestone Semana 2:** Chat funciona en tiempo real, whiteboard sincroniza entre 2+ usuarios

---

### 📅 Semana 3: Features Core (2-8 Nov)
- [ ] Todas las herramientas del whiteboard (colores, grosor, borrador)
- [ ] Cursores de otros usuarios visibles
- [ ] Optimización de sincronización (throttling)
- [ ] Persistencia de mensajes en DB
- [ ] Responsive design completo
- [ ] Animaciones y transiciones
- [ ] Testing con 5 usuarios simultáneos
- [ ] Corrección de bugs críticos

**🎯 Milestone Semana 3:** Aplicación completamente funcional, lista para demo

---

### 📅 Semana 4: Deployment & Presentación (9-15 Nov)
- [ ] Testing exhaustivo (frontend + backend)
- [ ] Deploy backend en Render.com
- [ ] Deploy frontend en Vercel
- [ ] Configurar PostgreSQL en la nube
- [ ] Screenshots de todas las funcionalidades
- [ ] Video demo (3-5 minutos)
- [ ] Presentación final (10 slides)
- [ ] Documentación completa
- [ ] Features opcionales (si sobra tiempo)

**🎯 Entregable Final:** App en producción + Video + Presentación + Repo documentado

---

## 🧪 Testing

> 🚧 Sección en desarrollo - Se agregará conforme se implementen tests

### Backend (pytest)
```bash
cd backend
pytest
```

### Frontend (Jest)
```bash
cd frontend
npm test
```

---

## 🚢 Deployment

> 🚧 Instrucciones de deployment se agregarán en la Semana 4

### Backend (Render.com) - Próximamente
- Guía de deployment pendiente

### Frontend (Vercel) - Próximamente
- Guía de deployment pendiente

---

## 📸 Screenshots

> 🎬 Screenshots se agregarán conforme avance el desarrollo visual del proyecto

### Pantalla de Inicio
🚧 *Próximamente*

### Whiteboard Colaborativo
🚧 *Próximamente*

### Chat en Tiempo Real
🚧 *Próximamente*

---

## 🎥 Demo en Vivo

> 🌐 Links se agregarán cuando la aplicación esté desplegada

- **Aplicación Web:** 🚧 *En desarrollo*
- **Video Demo:** 🚧 *Próximamente en Semana 4*
- **Repositorio:** [GitHub - CollabSpace](https://github.com/Cr4wl3rPy/collabspace)

---

## 🤝 Contribuir

Este es un proyecto académico desarrollado por un equipo de 5 estudiantes. Mientras está en desarrollo activo, las contribuciones externas no están siendo aceptadas. Sin embargo, apreciamos el interés y feedback.

### Para el equipo interno:

1. Crear una rama para tu feature (`git checkout -b feature/NombreFeature`)
2. Hacer commits descriptivos (`git commit -m 'feat: add whiteboard tools'`)
3. Push a la rama (`git push origin feature/NombreFeature`)
4. Abrir un Pull Request
5. Esperar review de al menos 1 miembro del equipo
6. Merge a `main` solo los domingos en reunión grupal

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 🙏 Agradecimientos

- Profesor de Interacción Hombre-Máquina por la guía y retroalimentación
- Documentación oficial de Flask-SocketIO
- Comunidad de React y Fabric.js
- Stack Overflow y GitHub por recursos invaluables

---

## 📞 Contacto

**Equipo CollabSpace**

- 🐙 GitHub: [@Cr4wl3rPy](https://github.com/Cr4wl3rPy/collabspace)
- 📧 Email: *Se agregará próximamente*

---

## 📚 Recursos y Referencias

### Documentación Oficial
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [React Documentation](https://react.dev/)
- [Fabric.js Documentation](http://fabricjs.com/docs/)
- [Socket.io Client](https://socket.io/docs/v4/client-api/)

### Tutoriales Útiles
- [Building Real-time Apps with Flask-SocketIO](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
- [Collaborative Whiteboard Tutorial](https://www.youtube.com/results?search_query=collaborative+whiteboard+tutorial)

---

## 🔄 Historial de Cambios

### v0.1.0 (Octubre 2025)
- ✅ Proyecto inicializado
- ✅ README inicial creado
- ✅ Stack tecnológico definido
- ✅ Estructura de carpetas planificada
- ✅ Roadmap de 4 semanas establecido

---

<div align="center">

### 🚧 Proyecto en Desarrollo Activo 🚧

**Este README se actualiza semanalmente**

⭐ **Última actualización:** Semana 1 - Setup Inicial

---

Desarrollado con ❤️ por el equipo CollabSpace  
*Proyecto Académico - Interacción Hombre-Máquina 2025*

</div>
