# Rommex Fleet Management

Aplicación web para la gestión y control de flota de camionetas de la empresa Rommex.

## Características

- Registro manual y por archivo (Excel/CSV)
- Visualización y edición de datos por camioneta
- Cálculo automático de promedios, mantenimientos, proyecciones y alertas
- Registro y reporte de costos, reparaciones y observaciones
- Gráficos por vehículo y dashboard general

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/ciper12-alt/rommex-fleet.git
    cd rommex-fleet
    ```

2. Instala las dependencias (recomendado: crea un entorno virtual):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Inicia la aplicación:

    ```bash
    python app.py
    ```

4. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

## Estructura del Proyecto

- `app.py` — Lógica principal Flask
- `models.py` — Modelos de datos SQLAlchemy
- `utils.py` — Funciones de cálculo y utilidades
- `templates/` — Archivos HTML (Jinja2)
- `static/` — Archivos CSS/JS (gráficas, estilos)
- `requirements.txt` — Dependencias Python

## Importación por archivo

Admite archivos `.csv` o `.xlsx` con columnas: `placa`, `km_actual`, `km_prox_mantencion`.

## Licencia

MIT