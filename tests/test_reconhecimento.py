import cv2
import numpy as np

from reconhecimento import reconhecer_placa


def test_reconhecer_placa_vazia():
    imagem = np.zeros((100, 200), dtype=np.uint8)
    placas = reconhecer_placa(imagem)
    assert isinstance(placas, list)
