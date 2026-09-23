# Fase 1 — EDA: entender los datos sin modelar (completada)

> Rama original: `main` (commit `4277666`) | Datos: `data/raw/reviews.csv` | Notebook: `src/explore.ipynb` (celdas 1-12)

## Explicación sencilla (qué es y por qué va primero)

**Idea en una frase:** mirar la nevera antes de cocinar — ver qué hay, qué falta y qué está raro, antes de usar ningún modelo.

La EDA (Exploración) responde: ¿qué columnas tenemos? ¿hay huecos o repetidos? ¿cómo se reparten las estrellas? ¿los textos son normales o hay vacíos/cortes? Sin esto, el modelo de sentimiento podría dar un % que no significa nada.

**Reglas de esta fase:** solo explorar. Nada de modelo de sentimiento, nada de `src/app.py`, nada de reporte de cliente.

## Lo que hicimos (pasos del notebook)

1. Carga de `data/raw/reviews.csv` → shape, columnas, tipos, 3 primeras filas.
2. Nulos + duplicados + vacíos.
3. Distribución de `rating` (conteo, %, media, mediana).
4. Longitud de texto (`n_chars`, `n_words`, describe).
5. Una reseña de ejemplo por estrella (1-5) para oír el tono.

## Resultados reales (500 reseñas)

- **Forma:** 500 filas × 3 columnas (`review_id` int, `rating` int, `review_text` str).
- **Calidad:** 0 nulos, 0 vacíos, 0 filas duplicadas completas, `review_id` únicos.
- **Duplicados de texto:** 7 valores exactos repetidos (14 filas implicadas) + frases plantilla recicladas ("Great spot…", "Will definitely be back!").
- **Estrellas:** 1→12 (2.4%), 2→18 (3.6%), 3→38 (7.6%), 4→72 (14.4%), 5→360 (72%). Media **4.5**, mediana **5.0**. El 86.4% son 4-5.
- **Longitud:** media 170 caracteres / 29 palabras; min 86/14, p50 173/29, max 230/42. Nada cortado ni gigante.
- **Tono por estrella:** 1-2 quejas claras (frío, rude, "won't be returning"); 3 tibio ("fine", "average", "slow"); 4-5 elogio aunque algunos 4-5 traen queja dentro ("25 min… pero la comida lo compensó").

## Insights (cortos y accionables)

1. **El 4.5 cuadra en estrellas** — el texto debería leerse mayormente positivo; si el modelo dice otra cosa, sospechamos del modelo.
2. **Pocas negativas (30 de 1-2, 6%)** — métricas sobre negativos serán ruidosas; leerlas a mano en Fase 4.
3. **Plantilla + duplicados** — inflan conteos; marcarlos en Fase 2 antes de calcular %.
4. **Reseñas mixtas = trampa** — 4-5 con queja interna anticipan falsos negativos del modelo de productos (Fase 4).

## Propuesta de limpieza (la ejecuta Fase 2)

- Normalizar espacios/unicode (`Café`, comillas) sin tocar puntuación ni negaciones.
- No quitar stopwords/emojis.
- Columna `is_duplicate_text`, decidir conteo en Fase 4.
- Validar `rating` 1-5. Guardar en `data/processed/`, `data/raw/` intacto.

## Quiz Fase 1 (corrección)

- P1 "para qué mirar primero" → Evitar sorpresas ✓
- P2 "qué esperas con media 4.5" → inicialmente "reparto uniforme" ✗ → corrección: mayoría 4-5, sesgo arriba; si no aparece, algo raro.
- P3 "qué sale de Fase 1" → Insights + propuesta ✓
