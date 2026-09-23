# Fase 3 — Integración del modelo HF (estado: completada)

> Rama: `fase-3-modelo` | Modelo: `nlptown/bert-base-multilingual-uncased-sentiment` | Entra: `data/processed/reviews_clean.csv`

## Explicación sencilla (léeme primero)

**Idea en una frase:** enchufar un traductor que ya sabe leer sentimiento, sin entrenar nada.

El modelo es un BERT multilingüe afinado en reseñas de productos. Lee cada reseña y devuelve 1-5 estrellas. Nosotros mapeamos: 1-2→Negativo, 3→Neutral, 4-5→Positivo. Con eso respondemos a la manager: cuántas se leen positivas/neutrales/negativas.

**Las 3 reglas duras (del reto, no negociables):**
1. Cargar con `pipeline("sentiment-analysis", model="nlptown/...")` o `from_pretrained` — nunca descargar pesos y subirlos al repo (pesan cientos de MB, Git los rechaza).
2. Cargar el modelo **una sola vez** antes del loop, no una vez por reseña (500 cargas = horas vs minutos).
3. **Fijar el nombre** exacto en el código — no usar "latest" silencioso que cambie bajo tus pies.

**Detalles prácticos:**
- Entrada: `review_text_clean` (Fase 2). Textos de ~29 palabras, sin problema de truncado (límite 512 tokens).
- Batch: de 8-16 a la vez para ir rápido sin comerse la RAM.
- Truncado: `truncation=True, max_length=512` por seguridad.
- Salida por reseña: `pred_stars` (1-5), `pred_label` (Negativo/Neutral/Positivo), `pred_score` (confianza).
- Guardar en `data/processed/reviews_pred.csv`. Sin evaluar todavía (eso es Fase 4).

**Lo que NO es esta fase:** no se compara contra estrellas reales, no se explica el desajuste, no se toca `app.py`.

**Salida del build:** celdas de inferencia en `explore.ipynb` + `reviews_pred.csv` + esta ficha a "completada".

## Quiz Fase 3 (corrección: 3/3)

- P1 mapeo → 1-2 Neg, 3 Neu, 4-5 Pos ✓
- P2 carga → pipeline una vez antes del loop, nombre pineado ✓
- P3 entrada → `review_text_clean` con batch y truncado ✓

## Build ejecutado

- Script único: `run.py` (carga 1 vez, batch 8, `truncation=True, max_length=512`).
- Nota entorno: el antivirus local hace MITM a HTTPS → se usa `truststore` (almacén de Windows) solo para descargar el modelo; los pesos NO se suben al repo (quedan en caché local de HF).
- `requirements.txt`: añadidos `transformers`, `torch`, `truststore`.
- Resultado (500 reseñas): Positivo **412 (82.4%)**, Neutral **41 (8.2%)**, Negativo **47 (9.4%)**. Estrellas predichas: 1→22, 2→25, 3→41, 4→56, 5→356.
- Brecha vs estrellas reales (86.4% son 4-5): el modelo ve ~4 puntos menos de positivo → se investiga en Fase 4.
