import re
from pathlib import Path


def analizar_sentimiento(texto: str) -> dict:
    resultado = {
        "Positivo": 0,
        "Neutro": 0,
        "Negativo": 0,
        "Descartada": 0
    }

    positivas = [
        "excelente", "genial", "perfecto", "increíble",
        "muy buena", "recomendado", "lo amo"
    ]

    negativas = [
        "pésimo", "fatal", "porquería", "horrible",
        "desastre", "decepcionado", "lo peor"
    ]

    for linea in texto.splitlines():
        linea = linea.strip()

        if not linea:
            continue

        rating = extraer_rating(linea)


        # Review inválida si no hay rating válido
        if rating is None:
            print(f"DESCARTADA (sin rating válido): {linea}")
            resultado["Descartada"] += 1
            continue

        texto_lower = linea.lower()

        # Detectar contradicciones simples
        tiene_positivo = any(p in texto_lower for p in positivas)
        tiene_negativo = any(n in texto_lower for n in negativas)

        if rating >= 4 and tiene_negativo or rating <= 2 and tiene_positivo:
            print(f"DESCARTADA (ambigua): {linea}")
            resultado["Descartada"] += 1
            continue

        # Clasificación
        if rating >= 4:
            print(f"POSITIVA: {linea}")
            resultado["Positivo"] += 1
        elif rating == 3:
            print(f"Neutro: {linea}")
            resultado["Neutro"] += 1
        else:
            print(f"Negativo: {linea}")
            resultado["Negativo"] += 1

    return resultado


def extraer_rating(texto: str):
    texto = texto.lower()

    # rating: 5 / rating 5 / puntaje: 5
    match = re.search(r"(rating|puntaje)\s*:?\s*([1-5])\b", texto)
    if match:
        return int(match.group(2))

    # 5/5 o 3/5
    match = re.search(r"\b([1-5])/5\b", texto)
    if match:
        return int(match.group(1))

    # 5 estrellas
    match = re.search(r"\b([1-5])\s*estrellas\b", texto)
    if match:
        return int(match.group(1))

    # ★★★★★
    estrellas = re.search(r"★+", texto)
    if estrellas:
        cantidad = len(estrellas.group())
        if 1 <= cantidad <= 5:
            return cantidad

    return None


if __name__ == "__main__":
    texto = Path("reviews.txt").read_text(encoding="utf-8")
    print("Resumen:", analizar_sentimiento(texto))