# Procesamiento de las reviews de los clientes.

## Descripción

Proyecto de procesamiento de datos no estructurados utilizando Python.

El objetivo es analizar reseñas de clientes provenientes de distintos canales y clasificarlas según su nivel de satisfacción a partir de la puntuación (rating) encontrada en cada comentario.

El dataset contiene información inconsistente, incluyendo formatos de rating diferentes, valores fuera de rango, reseñas sin puntuación y casos donde el texto no coincide con la valoración asignada.

---

## Objetivos

- Extraer ratings desde texto libre.
- Validar ratings dentro del rango permitido.
- Clasificar reseñas en categorías de sentimiento.
- Manejar datos incompletos o inconsistentes.
- Documentar criterios de limpieza y validación.

---

## Reglas de clasificación

| Rating | Categoría |
|----------|----------|
| 4 - 5 | Positivo |
| 3 | Neutro |
| 1 - 2 | Negativo |

---

## Problemas de calidad tratados

- Ratings faltantes.
- Ratings duplicados.
- Ratings fuera de rango.
- Formatos inconsistentes.
- Diferencias entre el contenido textual y la valoración.

---

## Tecnologías utilizadas

- Python
- Expresiones regulares (Regex)
- Manejo de archivos de texto

---

## Aprendizajes

Durante este proyecto se trabajó con:

- Limpieza de datos.
- Procesamiento de texto.
- Validación de información.
- Manejo de casos ambiguos.
- Toma de decisiones documentadas.

---

## Autor

Franco Jarc

