# car-dashboard
Dashboard interactivo para análisis exploratorio de anuncios de autos.  Esta aplicación permite analizar datos de anuncios de vehículos usando gráficos interactivos. Incluye un histograma y un gráfico de dispersión creados con plotly-express, integrados en una aplicación web desarrollada con Streamlit.
# Proyecto de Análisis de Anuncios de Autos

Este proyecto tiene como objetivo practicar el análisis exploratorio de datos (EDA) y la creación de una aplicación web interactiva.

## 📊 Análisis Exploratorio (EDA)

El análisis exploratorio se encuentra completo en el archivo `notebooks/EDA.ipynb`.  
Incluye:

- Histograma del odómetro.
- Gráfico de dispersión de odómetro vs precio.
- Distribución de precios.
- Precio promedio por año.

Cada visualización incluye explicaciones en celdas Markdown para facilitar la interpretación.

## 🌐 Aplicación web (Streamlit)

La intención era crear una aplicación web interactiva usando Streamlit.  
Sin embargo, debido a problemas de compatibilidad con mi equipo (macOS y versiones recientes de Python), no fue posible ejecutar Streamlit de manera local, ya que se producía un error crítico (Segmentation fault).

El archivo `app.py` y `requirements.txt` están preparados en el repositorio para una futura ejecución si se desea probar en otro entorno o servidor (por ejemplo, Render o un sistema operativo diferente).

##  Conclusión

El análisis exploratorio de datos está completamente realizado y documentado.  
Se incluyen todos los archivos y configuraciones necesarias para la ejecución del proyecto.

---

 **Nota:** Si se desea desplegar la aplicación web en el futuro, se recomienda realizarlo en un entorno Linux o con una configuración diferente a macOS 11, ya que Streamlit y ciertas librerías (como PyArrow) presentan conflictos conocidos en esta configuración.
