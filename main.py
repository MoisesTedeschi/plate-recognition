import signal
import sys
import time

import cv2

from camera import iniciar_camera
from controle_porta import acionar_porta
from interface import desenha_interface
from reconhecimento import reconhecer_placa


def sair_da_aplicacao(sig, frame):
    print("\nEncerrando a aplicação...")
    if cap:
        cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)


signal.signal(signal.SIGINT, sair_da_aplicacao)
signal.signal(signal.SIGTERM, sair_da_aplicacao)

tempo_espera = 2
ultima_leitura = 0

with open("autorizadas.txt") as f:
    placas_autorizadas = {linha.strip().upper() for linha in f.readlines()}

cap = iniciar_camera()
if cap is None:
    sys.exit("Encerrando aplicação: câmera indisponível.")

placa_detectada = ''
liberado = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    if time.time() - ultima_leitura > tempo_espera:
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        placas = reconhecer_placa(cinza)

        if placas:
            placa_detectada = placas[0]
            liberado = placa_detectada in placas_autorizadas
            if liberado:
                acionar_porta()
        else:
            placa_detectada = "NENHUMA"
            liberado = False

        ultima_leitura = time.time()

    frame = desenha_interface(frame, placa_detectada, liberado)
    cv2.imshow("Reconhecimento de Placas", frame)

    if cv2.getWindowProperty("Reconhecimento de Placas", cv2.WND_PROP_VISIBLE) < 1:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
