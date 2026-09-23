"""WeLoveReviews: inferencia de sentimiento con modelo HF pineado.

Modelo: nlptown/bert-base-multilingual-uncased-sentiment (1-5 estrellas
-> Negativo 1-2, Neutral 3, Positivo 4-5). Sin entrenar, sin subir pesos.
Uso: python run.py  (desde la raiz del proyecto)
"""
import truststore  # antivirus local hace MITM: usar almacen de Windows para verificar SSL

truststore.inject_into_ssl()

import pandas as pd
from transformers import pipeline

MODEL = "nlptown/bert-base-multilingual-uncased-sentiment"  # pin exacto

clf = pipeline("sentiment-analysis", model=MODEL, truncation=True, max_length=512)

df = pd.read_csv("data/processed/reviews_clean.csv", encoding="utf-8")
col = "review_text_clean" if "review_text_clean" in df.columns else "review_text"
textos = df[col].astype(str).tolist()

outs = clf(textos, batch_size=8, truncation=True, max_length=512)


def a_banda(label: str):
    estrellas = int(str(label).strip()[0])
    banda = "Positivo" if estrellas >= 4 else ("Neutral" if estrellas == 3 else "Negativo")
    return estrellas, banda


df["pred_stars"] = [a_banda(o["label"])[0] for o in outs]
df["pred_label"] = [a_banda(o["label"])[1] for o in outs]
df["pred_score"] = [float(o["score"]) for o in outs]

df.to_csv("data/processed/reviews_pred.csv", index=False, encoding="utf-8")
print(df["pred_label"].value_counts().to_string())
print(df["pred_stars"].value_counts().sort_index().to_string())
print("OK data/processed/reviews_pred.csv", df.shape)
