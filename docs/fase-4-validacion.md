# Fase 4 — Validación y falsos negativos (estado: completada)

> Rama: `fase-4-validacion` (se creará desde `fase-3-modelo`) | Entra: `data/processed/reviews_pred.csv` (500 filas)

## Explicación sencilla (léeme primero)

**Idea en una frase:** comprobar si el modelo dice lo mismo que las estrellas, y explicar dónde se equivoca.

Ya tenemos dos columnas que hablan del mismo cliente: la estrella que puso (`rating`) y lo que el modelo leyó (`pred_label`). Fase 4 las pone cara a cara con una tabla de confusión: ¿cuántas coinciden? ¿dónde discrepan? Esa comparación es la "segunda opinión basada en datos" que pidió la account manager.

**Números reales ya calculados (verificados sobre `reviews_pred.csv`):**

| Banda real (estrellas) | → Negativo | → Neutral | → Positivo |
|------------------------|-----------|----------|-----------|
| Negativo (1-2, n=30)   | 28        | 2        | 0         |
| Neutral (3, n=38)      | 3         | 35       | 0         |
| Positivo (4-5, n=432)  | **16**    | 4        | 412       |

- **Acuerdo global: 95.0%** (475/500). El modelo y las estrellas coinciden casi siempre.
- **Falsos negativos: 16** — reseñas de 4-5 estrellas que el modelo marca Negativo. Ej.: *"Every dish was bursting with flavor. The place has such a cozy, welcoming vibe..."* (5 estrellas → el modelo dice 1). Textos que a un humano le suenan claramente positivos.
- **Falsos positivos: 0** — ninguna reseña de 1-2 fue marcada Positiva. El modelo no "inventa" alegría donde no la hay.
- **Medias:** estrellas reales 4.5 vs estrellas del modelo 4.4. La brecha es pequeña pero viene de esos 16 casos.

**Por qué ocurren (el desajuste de dominio del reto):** el modelo se afinó con reseñas de *productos* (estilo Amazon: "buena batería, llegó rápido"). Nuestras reseñas hablan de *servicios* (personal, tiempos de espera, ambiente: "esperamos 25 min…", "el camarero…"). Ese vocabulario no estaba en su entrenamiento y lo empuja a marcar negativo aunque el cliente puso 4-5. Encontrar y explicar estos 16 casos **es** el ejercicio, no un fallo nuestro.

**Las 3 acciones de esta fase:**
1. Tabla de confusión + % de acuerdo (estrellas vs bandas del modelo).
2. Cazar y leer a mano los 16 falsos negativos: listar ejemplos y clasificar la causa (mención de espera, queja compensada, vocabulario de servicio…).
3. Conclusión para la manager: el 4.5 **sí** se sostiene (95% de acuerdo, media 4.4), y la diferencia viene de 16 reseñas positivas con lenguaje de servicio que confunde al modelo de productos.

**Lo que NO es esta fase:** no se reentrena nada, no se cambia el modelo, no se toca `src/app.py`, no se escribe el reporte final (% definitivo + narrativa → Fase 5).

**Salida del build:** celdas de validación en `src/explore.ipynb` (confusión + ejemplos) + esta ficha a "completada".

## Quiz Fase 4 (corrección: 3/3)

- P1 falso negativo → 4-5 que da Negativo (16 casos) ✓
- P2 causa → desajuste de dominio producto→servicio ✓
- P3 salida → % acuerdo + causa (95%, brecha explicada) ✓

## Build ejecutado

- Celdas 19-22 en `explore.ipynb`: `banda_real` vs `pred_label`, crosstab, acuerdo, caza de FN con 3 ejemplos citados por `review_id`.
- Sin reentrenar, sin tocar `app.py` (eso es Fase 5).
