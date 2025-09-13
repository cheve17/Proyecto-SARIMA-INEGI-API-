# Índice Nacional de Precios al Consumidor 

## Descripción General
Este proyecto implementa un modelo de series de tiempo SARIMA para pronosticar el Índice Nacional de Precios al Consumidor (INPC) en México. 

¿Qué es un INPC?
INPC es un indicador económico del Inegi que mide la variación promedio de los precios de una canasta representativa de bienes y servicios que consumen los hogares mexicanos a lo largo del tiempo, reflejando así el aumento de la inflación y la pérdida del poder adquisitivo de la moneda. 

¿Cómo funciona?

El INEGI toma una canasta representativa de bienes y servicios (más de 300 conceptos).Cada quincena, recolecta precios en miles de establecimientos en todo el país. Calcula un índice comparando esos precios con los de una base (año base = 2018 = 100).
Si el índice sube, significa que aumentaron los precios (inflación).

📈 Usos del INPC

* Medir la inflación (qué tan rápido suben los precios).
* Ajustar salarios (salario mínimo, contratos colectivos).
* Revisar rentas y pensiones que están indexadas al INPC.
* Política monetaria: el Banco de México lo usa para decidir las tasas de interés.
* Análisis económico: sirve para evaluar el poder adquisitivo y costo de vida.


El pipeline incluye:

- Conexión a la API de INEGI para descarga de datos.

- Procesamiento y ajustes de la serie temporal.

- Entrenamiento del modelo SARIMA.

- Generación de pronósticos para los próximos 12 ciclos.

- Visualización interactiva con Plotly.

- Evaluación del desempeño mediante el MAPE usando los últimos 12 valores reales.


Datos:

| Variable        | Descripción                                                         |
| --------------- | ------------------------------------------------------------------- |
| `TIME_PERIOD`   | Periodo temporal de la observación.                                 |
| `OBS_VALUE`     | Valor del INPC en ese periodo.                                      |
| `OBS_EXCEPTION` | Marca si la observación tiene alguna excepción.                     |
| `OBS_STATUS`    | Estado de la observación.                                           |
| `OBS_SOURCE`    | Fuente de la información (INEGI).                                   |
| `OBS_NOTE`      | Nota o comentario metodológico asociado al dato.                    |
| `COBER_GEO`     | Cobertura geográfica de la serie.                                   |


## Estructura del Proyecto
📂 Proyecto-SARIMA-INEGI-API-

 ┣ 📜 fetcher.py         # ETL básico 

 ┣ 📜 README.md          # Explicación del proyecto

 ┣ 📜 .gitignore         # Para ignorar archivos sensibles o pesados

 ┣ 📜 observaciones.csv  # Base de datos del INEGI 
 
 ┣ 📜 SARIMA.ipynb       # Script del modelo 
 


## Metodología y Modelo

Selección del modelo SARIMA

SARIMA (1,1,3)(1,0,2,24) es apropiado porque la serie presenta estacionalidad y tendencia.

Se eligió un parámetro de 24 ya que la base de datos nos arroja valores de manera quincenal, es decir dos datos menusuales, dado que la frecuencia es quincenal y nuestra proyección es a 12 meses se utilizó un t-24. 



## Resultados

MAPE: 0.61%


## Conclusiones

SARIMA es adecuado porque permite modelar simultáneamente la tendencia, la estacionalidad y las dependencias temporales que caracterizan a esta serie quincenal. Además, su flexibilidad para incluir términos estacionales lo hace más apropiado que un ARIMA tradicional, dado que el INPC tiene un claro componente estacional anual.


