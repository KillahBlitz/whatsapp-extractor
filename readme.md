# WhatsApp Extractor

Una aplicación de escritorio desarrollada en Python para extraer números telefónicos de grupos de WhatsApp utilizando web scraping.

## 📋 Descripción

WhatsApp Extractor es una herramienta que permite automatizar la extracción de números telefónicos de grupos de WhatsApp mediante técnicas de web scraping. La aplicación cuenta con una interfaz gráfica desarrollada con PySide6 (Qt) y un sistema modular para el procesamiento y almacenamiento de datos.

## 🏗️ Arquitectura del Proyecto

```
whatsapp-extractor/
├── form.ui                    # Archivo de diseño de la interfaz (Qt Designer)
├── widget.py                  # Archivo principal de la aplicación
├── ui_form.py                 # Archivo generado automáticamente desde form.ui
├── readme.md                  # Documentación del proyecto
├── whatsapp-extractor.pyproject   # Configuración del proyecto Qt
├── assets/
│   └── requirements.txt       # Dependencias de Python
└── src/
    ├── media/
    │   └── data.csv          # Archivo CSV con números extraídos
    ├── models/               # Modelos de datos
    └── scripts/
        ├── scrappy.py        # Script principal de extracción
        ├── save_data.py      # Módulo para guardar datos
        └── errors.py         # Manejo de errores y UI
```

### Módulos Principales

- **`scrappy.py`**: Módulo principal encargado de iniciar el proceso de extracción de números telefónicos desde grupos de WhatsApp.
- **`save_data.py`**: Se encarga del almacenamiento y gestión de los números telefónicos extraídos.
- **`errors.py`**: Maneja los errores del sistema y la interfaz de usuario.
- **`src/media/`**: Directorio donde se almacenan los archivos CSV con los datos extraídos.

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.13.0
- Git

### Configuración del Entorno

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/KillahBlitz/whatsapp-extractor.git
   cd whatsapp-extractor
   ```

2. **Cambiar a la rama de desarrollo:**
   ```bash
   git checkout devel
   ```

3. **Crear entorno virtual:**
   ```bash
   python -m venv .venv
   ```

4. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

5. **Instalar dependencias:**
   ```bash
   pip install -r assets/requirements.txt
   ```

## 🎯 Uso de la Aplicación

### Ejecutar la Aplicación

Para ejecutar la aplicación principal:

```bash
python widget.py
```

### Configuración del Perfil de Chrome (`CHROME_USER_DATA_DIR`)

La aplicación reutiliza tu sesión de WhatsApp Web abriendo Chrome con el perfil indicado en la constante `CHROME_USER_DATA_DIR` definida en `widget.py`.

Ruta actual por defecto:
```python
CHROME_USER_DATA_DIR = r'C:\Users\emanu\AppData\Local\Google\Chrome\User Data\Profile 1'
```

Si tu sesión activa está en otro perfil (por ejemplo `Profile 3` o un perfil personalizado), cambia la constante. Para saber tu ruta exacta:
1. Abre Chrome.
2. Escribe `chrome://version` en la barra de direcciones y pulsa Enter.
3. Busca el campo "Profile Path" (Ruta de perfil).
4. Copia esa ruta y reemplázala en `widget.py` respetando el formato raw string `r''`.

Ejemplo de modificación:
```python
CHROME_USER_DATA_DIR = r'C:\Users\tu_usuario\AppData\Local\Google\Chrome\User Data\Profile 3'
```

Si usas un perfil creado manualmente dentro de `User Data`, apúntalo igual (p.ej. `Profile 5`, `Default`, etc.). Asegúrate de tener la sesión ya iniciada en WhatsApp Web en ese perfil antes de presionar "Aceptar" en la ventana de proceso.

### Flujo Completo de Extracción

1. Ejecuta la aplicación: `python widget.py` (con el entorno virtual activado).
2. Ingresa el nombre EXACTO del grupo en el campo correspondiente.
3. Presiona el botón "Extraer".
4. Se abrirá la ventana de proceso mostrando el nombre del grupo y el mensaje para iniciar.
5. El scraping NO comienza todavía: debes presionar el botón "Aceptar" en esa ventana para iniciar. Hasta que no hagas clic ahí, no se abre el navegador.
6. Tras presionar "Aceptar" se abrirá Chrome con tu perfil y comenzará la extracción.
7. Espera a que el mensaje indique "completado" junto con el número de participantes extraídos.
8. El contador en la ventana principal (label de números recuperados) se actualiza automáticamente.
9. Ingresa tu "Número de teléfono" y la "Nomenclatura" (etiqueta) que quieras para el archivo.
10. Presiona "Descargar" para guardar el CSV.

### Formato y Nombre del Archivo CSV

El nombre del archivo se construye según los datos ingresados:
- Si ingresas teléfono y nomenclatura: `telefono nomenclatura.csv` (ej: `5512345678 CDMX.csv`)
- Si solo hay nomenclatura: `nomenclatura.csv`
- Si no hay ninguno de los dos: se usa el nombre del grupo: `nombre_del_grupo.csv`

El contenido del CSV incluye las columnas según los datos capturados por el scraper (nombre y teléfono). El archivo se guarda en el directorio `output/` del proyecto.

### Logs y Manejo de Errores

La aplicación sólo crea la carpeta `logs/` y archivos de log si ocurre un error durante la extracción. En ejecuciones normales sin errores no se generarán archivos de log.

Si ocurre un error:
- Se mostrará un mensaje de error.
- Se generará una entrada en `logs/` con el detalle técnico.

### Recomendaciones

- Asegúrate de tener tu sesión de WhatsApp Web previamente iniciada en el perfil de Chrome que configuraste.
- No interactúes con la ventana de Chrome mientras se realiza el scroll de extracción para evitar perder el foco.
- Si el grupo es muy grande (cientos de participantes), el tiempo de extracción puede aumentar.
- Si deseas cambiar el perfil frecuentemente, considera externalizar la ruta a una variable de entorno y leerla en `widget.py` (mejora opcional futura).

### Regenerar Interfaz desde Qt Designer

### Generar Interfaz desde Qt Designer

Si realizas cambios en el archivo `form.ui` usando Qt Designer, necesitas regenerar el archivo `ui_form.py`:

```bash
pyside6-uic form.ui -o ui_form.py
```

## 🛠️ Desarrollo

### Modificar la Interfaz

1. **Abrir Qt Designer:**
   - Instala Qt Designer por separado o utiliza la versión incluida con PySide6
   - Abre el archivo `form.ui`

2. **Realizar cambios en la interfaz**

3. **Regenerar el archivo Python:**
   ```bash
   pyside6-uic form.ui -o ui_form.py
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python widget.py
   ```

### Estructura del Código

#### Widget Principal (`widget.py`)
```python
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
```

#### Scripts de Extracción

Los scripts de extracción se encuentran en `src/scripts/`:

- **`scrappy.py`**: Punto de entrada para iniciar la extracción
- **`save_data.py`**: Funciones para guardar los datos en formato CSV
- **`errors.py`**: Manejo de excepciones y errores de la interfaz

## 📊 Datos de Salida

Los números telefónicos extraídos se almacenan en:
- **Ubicación**: `src/media/data.csv`
- **Formato**: CSV (Comma Separated Values)

## 🔧 Dependencias

Las dependencias del proyecto están listadas en `assets/requirements.txt`:

- **PySide6**: Framework para la interfaz gráfica (Qt para Python)

## 📝 Notas Importantes

- Asegúrate de tener Python 3.13.0 instalado
- El entorno virtual debe estar activado antes de ejecutar la aplicación
- Los cambios en `form.ui` requieren regenerar `ui_form.py`
- La aplicación utiliza web scraping, por lo que debe cumplir con los términos de servicio de WhatsApp

## 🌿 Manejo de Ramas

### Estructura de Ramas

El proyecto utiliza un flujo de trabajo con ramas para organizar el desarrollo:

- **`main`**: Rama principal estable con releases
- **`devel`**: Rama de desarrollo principal donde se integran las nuevas características
- **`staging`**: Rama para pruebas antes de merge a main
- **`feature/nombre-feature`**: Ramas individuales para desarrollar nuevas características

### Crear una Nueva Rama para Desarrollo

Antes de empezar cualquier desarrollo, asegúrate de crear una rama específica:

1. **Cambiar a la rama devel:**
   ```bash
   git checkout devel
   ```

2. **Actualizar la rama devel:**
   ```bash
   git pull origin devel
   ```

3. **Crear y cambiar a tu nueva rama:**
   ```bash
   git checkout -b feature/nombre-de-tu-feature
   ```

4. **Desarrollar tu funcionalidad**

5. **Hacer commit de los cambios:**
   ```bash
   git add .
   git commit -m "feat: descripción de tu feature"
   ```

6. **Subir la rama al repositorio:**
   ```bash
   git push origin feature/nombre-de-tu-feature
   ```

7. **Crear un Pull Request hacia la rama `devel`**

### Convenciones de Nombres de Ramas

- `feature/nueva-funcionalidad`: Para nuevas características
- `bugfix/corregir-error`: Para corrección de bugs
- `hotfix/error-critico`: Para correcciones urgentes
- `docs/actualizar-documentacion`: Para cambios en documentación

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

## ⚠️ Advertencia Legal

Esta herramienta debe utilizarse de manera responsable y conforme a los términos de servicio de WhatsApp. El uso indebido de esta aplicación puede violar los términos de servicio de la plataforma.