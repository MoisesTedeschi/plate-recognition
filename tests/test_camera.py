import pytest

from camera import iniciar_camera


def test_iniciar_camera():
    cap = iniciar_camera()
    assert cap.isOpened()
    cap.release()
