import numpy as np

from interface import desenha_interface


def test_desenha_interface():
    frame = np.zeros((200, 600, 3), dtype=np.uint8)
    result = desenha_interface(frame, "ABC1234", True)
    assert result is not None
