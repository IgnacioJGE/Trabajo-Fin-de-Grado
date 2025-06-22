# 🤖 Chatbot con Rasa + Web en Next.js

Este proyecto integra un chatbot hecho con **Rasa** en Python y una interfaz web desarrollada con **Next.js**.
A continuación se explica cómo levantar el entorno de desarrollo en cualquier PC de forma manual o usando Docker.

---

## 🧱 Requisitos

### 1. Python 3.9
Asegúrate de tener **Python 3.9** instalado en tu sistema (no es compatible con versiones más recientes para Rasa).

Puedes descargarlo desde: https://www.python.org/downloads/release/python-390/

### 2. Node.js
Instala Node.js (recomendado: versión 18 LTS o superior).

Puedes descargarlo desde: https://nodejs.org/

---

## ⚙️ Instalación Manual

### 🔹 1. Backend (Chatbot)

En el CMD

# Navega a la carpeta del backend
cd backend

# Crea un entorno virtual

"C:\Program Files\Python39\python.exe" -m venv venv // entre comillas el lugar dondde se tenga instalado python 3.9 en el PC

# Activa el entorno virtual

# En Windows:

Desde el CMD
venv\Scripts\activate

Desde Powershell
.\venv\Scripts\Activate.ps1  

# En macOS/Linux:
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

### 🔹 2. Fronted (Web Next.js)

# Desde la carpeta raíz del proyecto
cd ia_chatbot

# Instala las dependencias
npm install

##🚀 Ejecución del Proyecto

1. Ejecutar Rasa
Desde dos terminales distintos, estando dentro de la carpeta backend, ejecuta:

# Terminal 1 - Servidor principal de Rasa
rasa run --enable-api --cors "*" -p 5005

# Terminal 2 - Servidor de acciones personalizadas
rasa run actions --actions actions --cors "*" -p 5055

2. Configurar la IP para la Web
Para que la web se comunique con Rasa:

- 1. Abre una terminal y ejecuta:
  ipconfig

- 2. Copia la ip y ve al archivo:
  trabajo-fin-de-grado/ia_chatbot/app/componentes/respuestachatbot.tsx

- 3. Reemplaza tu ip en la llamada de axios:
  const response = await axios.post("http://TU_IPV4:5005/webhooks/rest/webhook", {...})

3. Compilar e iniciar la web

#Terminal 3 en la carpeta trabjo-fin-de-grado/ia_chatbot

npm run build
npx next start -H 0.0.0.0 -p 3000

Finalmente podrás acceder al proyecto desde tu navegador en http://localhost:3000.



🐳 Alternativa: Usar Docker

Si tienes Docker y Docker Compose instalado:

1. Ejecuta ipconfig como antes y actualiza el archivo respuestachatbot.tsx con tu IP local.
2. Luego, desde la carpeta trabajo-fin-de-grado/ia_chatbot:
npm run build

4. Finalmente desde la carpeta raiz:
docker compose up --build


Esto levantará tanto el frontend como el backend de forma automática.

