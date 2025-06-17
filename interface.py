import cv2

BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (0, 0, 255)


def desenha_interface(frame, placa, liberado):
    cv2.rectangle(frame, (0, 0), (600, 110), (0, 0, 0, 0.5), -1)

    cv2.putText(frame, f"Placa Detectada: {placa}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, VERDE if liberado else VERMELHO, 2)

    status = "LIBERADA" if liberado else "NEGADA"
    cor = VERDE if liberado else VERMELHO
    cv2.putText(frame, f"PASSAGEM {status}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor, 2)

    return frame
