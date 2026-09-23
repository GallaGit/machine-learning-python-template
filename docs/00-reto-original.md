# 00 — Reto original (líneas pegadas por el usuario, copia literal para no perder contexto)

> Fecha: 2026-09-23
> Proyecto: machine-learning-python — Cliente WeLoveReviews

---

## 🎯 Tu reto (texto pegado)

Trabajas como ingeniero/a de IA freelance para una pequeña consultora de datos. Tu último cliente, WeLoveReviews, ayuda a empresas a entender lo que realmente piensan sus clientes. Acaban de incorporar una nueva cuenta: un negocio con una puntuación promedio de 4.5 / 5, pero la account manager tiene una duda que no la deja tranquila — ¿el sentimiento expresado en las reseñas escritas realmente coincide con esa puntuación? Antes de entregarle un reporte a su cliente, quieren una segunda opinión basada en datos, no en intuición.

No tienes tiempo (ni los datos) para entrenar un modelo desde cero — y no lo necesitas. Hay muchos modelos preentrenados en Hugging Face que ya saben leer sentimiento en texto. Tu trabajo es explorar los datos, integrar uno correctamente, validar su resultado contra la realidad, y convertir texto crudo en algo que la account manager pueda realmente usar.

La account manager te compartió esto por correo:

"Le vamos a entregar a este cliente 500 reseñas escritas la próxima semana. Necesito saber, en términos simples, cuántas de estas reseñas se leen como positivas, neutrales o negativas — y si esa distribución coincide con su promedio de 4.5 estrellas. Si hay una diferencia, quiero entender de dónde viene antes de ponerlo frente al cliente."

## 📓 Cómo se comunica este equipo

En este equipo, los líderes tratan los notebooks de Jupyter como documentos de comunicación para análisis y procesamiento de datos — no como borradores descartables. Tu entregable narrativo es src/explore.ipynb: un notebook ejecutado que guía al lector desde los objetivos hasta la exploración, los insights, las decisiones de modelado, los resultados y las conclusiones. Se espera markdown breve entre bloques de código importantes; el notebook debe sostenerse por sí solo sin un informe markdown aparte para el cliente.

Orden de trabajo: Puedes ejecutar primero el prompt de EDA y luego anteponer los objetivos y continuar con el resto del proyecto en el mismo src/explore.ipynb, para que el archivo final siga el arco completo descrito abajo.

## 🤖 Nota sobre el modelo

Modelo a utilizar: nlptown/bert-base-multilingual-uncased-sentiment de Hugging Face.

⚠️ Desajuste de dominio: Este modelo fue fine-tuneado sobre reseñas de productos (p. ej. estilo Amazon). Tu dataset contiene reseñas de servicios — los clientes hablan del personal, tiempos de espera y ambiente. Ese desajuste puede producir falsos negativos: reseñas que a un humano leen como positivas (o tienen alta puntuación en estrellas) pero el modelo las clasifica con bajo sentimiento. Debes usar este modelo primero de todos modos — encontrar y explicar esos falsos negativos es parte del ejercicio.

Este modelo predice el sentimiento como una puntuación de 1 a 5 estrellas (no una etiqueta simple POSITIVO/NEGATIVO). Mapea la salida a bandas de sentimiento:

| Predicción del modelo | Banda de sentimiento |
|-----------------------|----------------------|
| 1–2 estrellas         | Negativo             |
| 3 estrellas           | Neutral              |
| 4–5 estrellas         | Positivo             |

Reglas de integración:

- Carga el modelo con pipeline() o from_pretrained() — no descargues los pesos y los subas al repositorio.
- Carga el modelo una sola vez antes del loop de inferencia, no dentro de un loop por reseña.
- Fija (pin) el nombre/versión del modelo en tu código — no dependas silenciosamente de lo que sea que "latest" resuelva cuando otra persona clone tu repo.

## 🧪 EDA con tu agente de código

Antes de modelar, explora el dataset con ayuda de tu agente de código:

- Abre PROMPT.es.md en la carpeta de este proyecto.
- Copia todo lo que está debajo de la línea del encabezado en tu agente (Cursor, Copilot, Claude Code, etc.).
- Deja que el agente trabaje en la sección de EDA de src/explore.ipynb — solo exploración, insights y propuesta de limpieza.
- El prompt se detiene después de la EDA. Todo lo que sigue abajo es tu responsabilidad en el mismo notebook y en src/app.py.

---

## Instrucción de trabajo del usuario (cómo quiere avanzar)

> "vamos a darle vueltas a esto para que yo lo entienda, dividelo por fases documenta dichas fases para no repetirnos si se pierde contexto tambien documenta las lineas que te pegue. Y explicame cada fase de manera sencilla. Despues de la documentacion de las fases, la ruta es: Fase 1. Explicacion, 3 preguntas, mi respuesta, correcion, modo build, implementacion, docs/, fase 2... este ciclo hasta recorrer todas las fases"

Ciclo acordado por fase:
1. Explicación sencilla
2. 3 preguntas para verificar comprensión
3. Respuesta del usuario
4. Corrección
5. Modo build (implementación)
6. Guardar en docs/
7. Siguiente fase
