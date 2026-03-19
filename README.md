#  YOLO Object Detection with Voice Feedback

> Sistema de detecção de objetos utilizando YOLO com feedback por voz em tempo real.

---

## 📌 Sobre o projeto

Este projeto utiliza técnicas de Inteligência Artificial e Visão Computacional para detectar objetos em imagens e fornecer feedback por voz com base nos objetos identificados.

A aplicação detecta objetos e informa sua posição na tela (ex: "bottom left cat"), podendo ser utilizada principalmente para acessibilidade e navegação assistida.

---

##  Funcionalidades

- Detecção de objetos com YOLO
- Uso de modelo pré-treinado (COCO dataset)
- Identificação da posição do objeto na tela (esquerda, centro, direita / cima, meio, baixo)
- Conversão de texto para voz (Text-to-Speech)
- Suporte para imagens

---

##  Tecnologias utilizadas

- Python
- OpenCV (cv2)
- YOLO (You Only Look Once)
- gTTS (Google Text-to-Speech)
- NumPy

---

##  Como funciona

1. A imagem é enviada para o modelo YOLO
2. O modelo detecta objetos e gera bounding boxes
3. O sistema calcula a posição do objeto na tela
4. A descrição é convertida em texto
5. O texto é transformado em áudio (voz)

Exemplo de saída:


bottom left cat


---

## ⚙️ Como rodar o projeto

```bash
# Clonar o repositório
git clone https://github.com/juniornapoles/yolo-object-detection-voice.git

# Entrar na pasta do projeto
cd yolo-object-detection-voice

# Instalar dependências
pip install -r requirements.txt

# Rodar o projeto
python script.py -i caminho/da/imagem.jpg -y caminho/do/yolo
📂 Estrutura do projeto
yolo-object-detection-voice
│
├── script.py
├── yolo/
├── images/
├── object_detection.mp3
├── requirements.txt
└── README.md
