# Interpolación de Lagrange y Newton: población de Colombia

Proyecto final de Análisis Numérico I, Universidad Industrial de Santander (UIS).

Se aplican los métodos de interpolación de **Lagrange** y de **Newton (diferencias divididas)** a la población total censada de Colombia en los censos del DANE, para estimar la población de años intermedios sin censo.

## Contenido

| Archivo | Descripción |
|---|---|
| `index.html` | Aplicación interactiva que explica paso a paso cada método (se abre en el navegador) |
| `interpolacion_poblacion_colombia.py` | Implementación en Python de ambos métodos, estimaciones y validación |
| `imagenes/grafica_poblacion.png` | Gráfica generada por el script |
| `requirements.txt` | Librerías de Python necesarias |

## Datos

Población total censada (conteo efectivo):

| Censo | Población |
|---|---|
| 1964 | 17.484.508 |
| 1973 | 20.666.920 |
| 1985 | 27.867.326 |
| 1993 | 33.109.840 |
| 2005 | 41.468.384 |
| 2018 | 44.164.417 |

Nota: el DANE también publica 48.258.494 para 2018, pero esa cifra incluye un ajuste por omisión censal (4.094.077 personas). Como los censos anteriores no tienen ese ajuste, se usó el conteo efectivo para comparar datos del mismo tipo.

Fuentes:
- DANE, cuadro 2 «Población total censada en 1964, 1973, 1985, 1993 y 2005»: https://www.dane.gov.co/files/censo2005/total_censo.pdf
- DANE, Censo Nacional de Población y Vivienda 2018, presentaciones de resultados: https://www.dane.gov.co/files/censo2018/informacion-tecnica/

## Cómo ejecutar el script

```bash
pip install -r requirements.txt
python interpolacion_poblacion_colombia.py
```

Imprime los coeficientes de Newton, las estimaciones para 1970, 1980, 1990, 2000, 2010 y 2015, y una validación dejando un censo fuera (*leave-one-out*). Además genera `grafica_poblacion.png`.

## Cómo ver la aplicación web

Abre `index.html` con doble clic en el navegador. Para publicarla con GitHub Pages: *Settings → Pages → Deploy from a branch → main / (root)*.

## Resultados principales

- Lagrange y Newton producen el mismo polinomio de grado 5 (solo cambia la forma de construirlo).
- La interpolación funciona bien entre 1973 y 2005, donde el crecimiento es regular.
- Entre 2005 y 2018 el polinomio oscila y supera los datos reales, por lo que las estimaciones de 2010 y 2015 no son confiables. Es un ejemplo de que más grado no implica mejor resultado.

## Autores

Nombres de la pareja aquí.
