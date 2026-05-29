# MALSCAN

## 1. Nombre del proyecto

**MalScan – Escáner Educativo de Malware por Firmas**

---

## 2. Descripción breve

MalScan es una herramienta creada en Python que imita el funcionamiento básico de un antivirus que utiliza firmas. Este sistema permite examinar archivos utilizando hashes SHA-256 y patrones de contenido para identificar posibles riesgos. Su propósito es enseñar de manera didáctica los mecanismos esenciales de detección empleados en la ciberseguridad.

---

## 3. Integrantes del grupo

- Gisela Esteve
- Emma Rosendo
- Nuria Salas

---

## 4. Contexto y problemática

La identificación de software malicioso es uno de los retos más significativos en la ciberseguridad actual. Los sistemas computacionales están siempre en riesgo ante peligros como el malware, el ransomware, los scripts dañinos o las herramientas de sustracción de información.

Los programas antivirus actuales emplean diversas estrategias para reconocer estas amenazas, siendo la más frecuente la detección mediante firmas. Este enfoque se basa en confrontar archivos con un registro de patrones y hashes que ya han sido catalogados.

---

## 5. Funcionalidades principales

El sistema implementa las siguientes funcionalidades:
- Añadir archivos para su análisis.
- Visualizar los archivos cargados.
- Eliminar archivos del sistema.
- Escaneo rápido mediante hashes SHA-256.
- Escaneo profundo mediante análisis de patrones.
- Clasificación automática de archivos:
  - Limpio
  - Sospechoso
  - Malicioso
- Gestión de firmas y hashes registrados.
- Visualización de firmas cargadas.
- Persistencia automática de archivos mediante JSON.
- Exportación de informes en formato:
  - HTML
  - TXT
  - CSV
- Generación de estadísticas del análisis.
- Compatibilidad con Windows y macOS.

---

## 6. Uso de POO y polimorfismo

### Programación Orientada a Objetos

El proyecto está desarrollado siguiendo los principios de Programación Orientada a Objetos.

Las principales clases implementadas son:

| Clase             | Descripción                                             |
| ----------------- | ------------------------------------------------------- |
| Archivo           | Representa un archivo analizado por el sistema          |
| Carpeta           | Representa una estructura de directorios recursiva      |
| FirmaMalware      | Define una firma de malware con severidad y descripción |
| ResultadoEscaneo  | Almacena el resultado obtenido tras el análisis         |
| BaseFirmas        | Gestiona hashes y patrones registrados                  |
| MotorEscaneo      | Coordina todo el proceso de análisis                    |
| EstrategiaEscaneo | Clase abstracta para los distintos tipos de escaneo     |
| EscaneoRapido     | Implementa la detección mediante hashes                 |
| EscaneoProfundo   | Implementa la detección mediante patrones               |

### Polimorfismo

El polimorfismo se aplica mediante el patrón Strategy.

La clase abstracta:

```python
EstrategiaEscaneo
```

define la interfaz común para los distintos algoritmos de análisis.

De ella heredan:

```python
EscaneoRapido
EscaneoProfundo
```

El motor de escaneo puede trabajar con cualquiera de estas estrategias sin modificar su funcionamiento interno.

---

## 7. Instrucciones de ejecución y dependencias

### Requisitos

- Python 3.10 o superior

### Dependencias utilizadas

El proyecto utiliza únicamente librerías estándar de Python:

```python
tkinter
hashlib
json
csv
datetime
os
pathlib
```

No es necesario instalar paquetes externos mediante pip.

### Ejecución

1. Descargar o clonar el proyecto.
2. Acceder a la carpeta principal.
3. Ejecutar:

```bash
python app.py
```

o bien:

```bash
python src/app.py
```

según la estructura del proyecto.

### Generación del ejecutable (opcional)

Para crear un ejecutable:

```bash
pip install pyinstaller
```

```bash
pyinstaller --onefile --windowed app.py
```

---

## 8. Enlace al vídeo demostrativo

**Vídeo demostrativo del proyecto:**



---

## 9. Uso de herramientas externas o IA

Durante el desarrollo del proyecto se han usado las siguientes herramientas de apoyo:
- Visual Studio Code como plataforma de programación.
- GitHub para el control de versiones.
- ChatGPT (OpenAI) como ayudante de apoyo para aclarar preguntas técnicas y revisar código.