# Proyecto de Web Scraping con Selenium

Este proyecto realiza web scraping en un sitio web de empleos utilizando Selenium para extraer información relevante sobre ofertas de trabajo, como el puesto, sueldo, comodidades y la empresa que ofrece la posición. Los datos se guardan en un archivo CSV para su posterior análisis.

## Descripción

El script automatiza la búsqueda de empleos en un sitio web específico, permitiendo al usuario especificar el estado, la ciudad y el puesto deseado. A través de la paginación, se recopila información de todas las páginas de resultados y se almacena en un diccionario de Python, que luego se convierte en un DataFrame de pandas y se guarda en un archivo CSV.

### Estructura del proyecto

- **manejoDatos(datos: dict)**: Función que guarda los datos extraídos en un archivo CSV.
- **paginacion(driver) -> dict**: Función que realiza la extracción de datos a través de la paginación de resultados en el sitio web.
- **main()**: Función principal que inicia el navegador, realiza la búsqueda de empleos y coordina la extracción y almacenamiento de datos.

### Tecnologías utilizadas

- **Python 3**
- **Selenium**
- **Pandas**
- **NumPy**

## Requisitos

- Python 3.x
- Selenium
- Geckodriver (si usas Firefox)
- Pandas
- NumPy

Puedes instalar las dependencias con pip:

```bash
pip install selenium pandas numpy
