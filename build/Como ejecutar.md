## Ejecutar en Windows

```bash
python src/app.py
```

O haz doble clic en:

```text
ejecutar_app.bat
```

### Crear ejecutable en Windows

```bash
pip install pyinstaller
cd src
pyinstaller --onefile --windowed app.py
```

El ejecutable estará en:

```text
src/dist/app.exe
```
---
## Ejecutar en macOS

Desde Terminal:

```bash
python3 src/app.py
```

También puedes usar el lanzador incluido:

```bash
chmod +x ejecutar_app_mac.command
./ejecutar_app_mac.command
```

### Crear aplicación en macOS

Desde macOS:

```bash
pip3 install pyinstaller
cd src
pyinstaller --onefile --windowed --name MalScan app.py
```

El ejecutable aparecerá en:

```text
src/dist/MalScan
```

> Nota: para generar un `.exe` de Windows hay que hacerlo desde Windows. Para generar una app de macOS hay que hacerlo desde macOS.