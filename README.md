# Projeto: Reconhecimento de Placas com Abertura de Porta

Este projeto utiliza Python, OpenCV e EasyOCR para capturar imagens de uma câmera, reconhecer placas veiculares e validar se estão autorizadas para permitir a abertura de uma porta (simulada).

## Funcionalidades
- Reconhecimento de placas via OCR
- Validação com lista de placas autorizadas
- Interface gráfica com status de permissão
- Simulação de abertura de porta
- Modularização do código
- Testes automatizados com `pytest`

## Requisitos
- Python 3.8+
- Webcam conectada ao computador

## Instalação
```bash
pip install -r requirements.txt
```

## Execução
```bash
python main.py
```

Pressione `q` para sair da execução.

## Testes
```bash
pytest tests/
```

## Estrutura
- `main.py`: loop principal
- `camera.py`: controle da webcam
- `interface.py`: visualização
- `reconhecimento.py`: OCR com EasyOCR
- `controle_porta.py`: simulação do relé
- `autorizadas.txt`: placas permitidas
