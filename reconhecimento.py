import easyocr

reader = easyocr.Reader(['pt'])


def reconhecer_placa(frame):
    resultado = reader.readtext(frame)
    placas_detectadas = []

    for detection in resultado:
        texto = detection[1].upper().replace(" ", "")
        if texto.isalnum() and 6 <= len(texto) <= 8:
            placas_detectadas.append(texto)

    return placas_detectadas
