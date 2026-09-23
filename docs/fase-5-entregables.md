# Fase 5 — Traducción a decisión + entregables finales (estado: completada)

> Rama: `welovereviews-sentiment` | Entra: todo lo anterior (`reviews_pred.csv`, notebook con Fases 1-4)

## Explicación sencilla (léeme primero)

**Idea en una frase:** convertir 500 filas técnicas en una respuesta que la account manager entienda y pueda llevar al cliente.

Hasta ahora cada reseña tiene `rating`, `pred_stars`, `pred_label` y `pred_score`. Pero la manager no va a leer 500 filas: necesita el resumen y la conclusión. Eso es Fase 5.

**La respuesta final, en números ya verificados:**

| Banda      | Reseñas | %     |
|------------|---------|-------|
| Positivo   | 412     | 82.4% |
| Neutral    | 41      | 8.2%  |
| Negativo   | 47      | 9.4%  |

- Acuerdo modelo vs estrellas: **95.0%** (475/500).
- Media real: **4.5** | media del modelo: **4.4**.
- Falsos negativos: **16** (4-5 → Negativo), falsos positivos: **0**.
- Causa de la brecha: desajuste de dominio — modelo entrenado en *productos*, reseñas sobre *servicios* (personal, espera, ambiente).

**Las 4 acciones de esta fase:**
1. **Cierre narrativo en `src/explore.ipynb`:** celdas finales con objetivo → recorrido → conclusión ejecutiva. El notebook debe leerse solo, sin informe aparte.
2. **`src/app.py` reutilizable:** script independiente que lee datos, carga el modelo una sola vez, predice, mapea a bandas e imprime el resumen. Sin `db_connect()` (este proyecto usa CSV, no necesita PostgreSQL).
3. **Esta ficha** con resultado, interpretación, limitaciones y cómo ejecutar.
4. **Verificación final:** ejecutar notebook + `python src/app.py`, comprobar que ambos dan el mismo conteo, commit y push.

**Estructura final esperada:**

```text
data/raw/reviews.csv
data/processed/reviews_clean.csv
data/processed/reviews_pred.csv
src/explore.ipynb
src/app.py
run.py
docs/fase-1-eda.md … docs/fase-5-entregables.md
```

**Lo que NO es esta fase:** no se cambia el modelo, no se reentrena, no se re-limpia. Solo cierre, código limpio y verificación.

## Preguntas de Fase 5 (corrección: 3/3)

1. Qué recibe la manager → resumen + detalle (anexo de 500) ✓
2. Los 16 casos → revisión humana, no invalidan ✓
3. Conclusión → coincide con matiz (95%, desajuste de dominio) ✓

## Build ejecutado (verificado)

- `src/app.py` reescrito: sin `db_connect`, pipeline pineado 1 vez, batch 8, regenera `reviews_pred.csv` e imprime el resumen. Ejecutado OK: 412/41/47, 95%, 4.50/4.40, 16 FN.
- `src/explore.ipynb`: 25 celdas, cierre ejecutivo + cómo reproducir.
- Limitaciones: modelo de productos aplicado a servicios; 16 FN a revisión humana; 30 negativas reales → métricas sobre negativos con ruido.
