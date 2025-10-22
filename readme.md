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

2. **Crear entorno virtual:**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar dependencias:**
   ```bash
   pip install -r assets/requirements.txt
   ```

## 🎯 Uso de la Aplicación

### Ejecutar la Aplicación

Para ejecutar la aplicación principal:

```bash
python widget.py
```

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