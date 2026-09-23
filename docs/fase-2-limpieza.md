# Fase 2 — Limpieza y preparación (estado: explicación lista, pendiente quiz + build)

> Rama: `fase-2-limpieza` | Base: EDA Fase 1 sobre `data/raw/reviews.csv` (500 filas)

## Explicación sencilla (léeme primero)

**Idea en una frase:** dejar el texto limpio y ordenado para el modelo, sin romper lo que da sentimiento.

Piensa en lavar fruta antes de cocinar: quitas polvo y pegatinas, pero no quitas la pulpa. Aquí igual.

**Lo que encontró la EDA (por eso limpiamos así):**
- 500 filas, columnas `review_id, rating, review_text`. 0 nulos, 0 vacíos, IDs únicos.
- 7 textos exactos repetidos (14 filas implicadas) + muchas frases plantilla ("Great spot…", "Will definitely be back!").
- Encoding roto: se ve `Caf�` en vez de `Café`. Espacios y comillas irregulares por el CSV.
- Reseñas mixtas: 4-5 estrellas con queja dentro ("esperamos 25 min… pero la comida lo compensó").
- Longitudes sanas: 14-42 palabras, nada cortado.

**Las 5 acciones de esta fase (y por qué):**
1. **Normalizar espacios y unicode** (ej. `Café`, comillas, dobles espacios) → el modelo lee mejor, no cambia el sentido.
2. **NO quitar puntuación, negaciones ("not/no"), stopwords ni emojis** → "no me gustó" sin "no" se vuelve "me gustó". Quitarlos destruye sentimiento.
3. **Marcar duplicados, no borrar a ciegas** → columna `is_duplicate_text`. Luego decidimos si contar una vez (análisis) o conservar (volumen). Borrar sin avisar falsea el % positivo/neutral/negativo.
4. **Validar `rating` 1-5 y tipos** → ahora está bien, solo se verifica.
5. **Guardar en `data/processed/reviews_clean.csv`, dejar `data/raw/` intacto** → raw es evidencia, processed es trabajo.

**Lo que NO es esta fase:** no se aplica ningún modelo de sentimiento, no se toca `src/app.py`, no se escribe reporte de cliente.

**Salida del build:** celdas nuevas en `src/explore.ipynb` + `data/processed/reviews_clean.csv` + esta ficha actualizada a "completada".
