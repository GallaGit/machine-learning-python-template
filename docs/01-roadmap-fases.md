# 01 — Roadmap por fases (documento maestro anti-pérdida de contexto)

> Si se pierde el contexto, leer en orden: `00-reto-original.md` → este archivo → `fase-X-*.md` correspondiente.

## Estado actual del repo (2026-09-23)

- Template base: `src/app.py` (vacío), `src/explore.ipynb` (vacío, solo "Explore here"), `src/utils.py`, `requirements.txt` (sin transformers/torch todavía).
- `data/raw|interim|processed/` vacías.
- Falta `PROMPT.es.md` en el repo → la EDA guiada por prompt aún no se puede ejecutar tal cual. Lo haremos manual en Fase 1.
- Modelo fijado: `nlptown/bert-base-multilingual-uncased-sentiment` (1-5 estrellas → Negativo 1-2, Neutral 3, Positivo 4-5).

## Fases acordadas

### Fase 1 — EDA: entender los datos (sin modelar)
**Objetivo:** Responder ¿qué tenemos? 500 reseñas: columnas, idioma, nulos, duplicados, distribución de estrellas, largo de texto, palabras frecuentes.
**Entra:** `data/raw/*.csv` (cuando aparezca) + `PROMPT.es.md` (si aparece).
**Sale:** Sección EDA en `src/explore.ipynb` + `docs/fase-1-eda.md` (insights + propuesta de limpieza).
**Regla:** Solo exploración, nada de modelo todavía.

### Fase 2 — Limpieza y preparación
**Objetivo:** Dejar texto usable sin destruir sentimiento (minúsculas con cuidado, quitar nulos/duplicados, normalizar espacios, no quitar emojis/puntuación a lo loco).
**Entra:** Propuesta de limpieza de Fase 1.
**Sale:** Código de limpieza en `explore.ipynb` + datos en `data/processed/` + `docs/fase-2-limpieza.md`.

### Fase 3 — Integración del modelo preentrenado
**Objetivo:** Conectar Hugging Face correctamente: `pipeline("sentiment-analysis", model="nlptown/...")` una sola vez, pin del nombre, batch, mapeo 1-2→Negativo, 3→Neutral, 4-5→Positivo.
**Entra:** Texto limpio.
**Sale:** Código inferencia en `explore.ipynb` + `docs/fase-3-modelo.md`.
**Reglas duras:** No subir pesos al repo. No cargar modelo dentro del loop. Pin de versión.

### Fase 4 — Validación contra la realidad + falsos negativos
**Objetivo:** Responder a la account manager: ¿coincide el modelo con las 4.5 estrellas? Matriz estrellas vs sentimiento, % acuerdo, cazar falsos negativos por desajuste de dominio (producto→servicio: personal, espera, ambiente).
**Entra:** Predicciones + columna estrellas real.
**Sale:** Gráficos + tabla + explicación del desajuste en `explore.ipynb` + `docs/fase-4-validacion.md`.

### Fase 5 — Traducción a decisión + entregables finales
**Objetivo:** Respuesta simple: X% positivas, Y% neutrales, Z% negativas, ¿coincide con 4.5? ¿de dónde viene la diferencia? Cierre narrativo + migrar código limpio a `src/app.py`.
**Entra:** Todo lo anterior.
**Sale:** `src/explore.ipynb` ejecutado y narrado de principio a fin + `src/app.py` funcional + `docs/fase-5-entregables.md`.

## Ciclo de trabajo por fase (obligatorio)

1. Explicación sencilla
2. 3 preguntas
3. Respuesta usuario
4. Corrección
5. Modo build (implementación en código)
6. Guardar en `docs/fase-X-*.md`
7. Siguiente fase

## Dónde estamos

- [x] Docs base creados (00 + 01)
- [ ] Fase 1: explicación dada, esperando respuestas a las 3 preguntas
- [ ] Fase 2-5 pendientes
