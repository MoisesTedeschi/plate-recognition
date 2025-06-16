import cv2


def iniciar_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("⚠️ ERRO: Não foi possível acessar a câmera.")
        return None
    print("✅ Câmera iniciada com sucesso.")
    return cap
