# Dashboard Python para Fiat OBD-II

Este repositório contém um dashboard interativo desenvolvido em Python para exibir dados automotivos obtidos via OBD-II. O projeto foi criado para funcionar em um **Raspberry Pi 3** com uma tela de **480x320**, utilizando **Pygame** para renderização da interface.

## 📌 Funcionalidades
- **Leitura de dados via OBD-II**: Captura informações em tempo real do veículo.
- **Visualização intuitiva**: Interface desenvolvida para facilitar a leitura rápida dos dados.
- **Sensores exibidos na primeira tela**:
  - **RPM**
  - **Velocidade (km/h)**
  - **Temperatura do motor (°C)**
  - **Temperatura do ar de admissão (°C)**
  - **Posição do acelerador (%)**
- **Troca de telas**: Implementação de uma área clicável para exibir novos sensores.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Pygame** (para renderização da interface)
- **OBD-Python** (para comunicação com o OBD-II)
- **Kivy** (possível suporte para interface alternativa)

## 📂 Estrutura do Projeto
- **kivt/**: Contém arquivos relacionados à implementação com Kivy.
- **pygames/**: Implementação principal do dashboard utilizando Pygame.
- **assets/**: Contém imagens e outros recursos visuais do projeto.
- **main.py**: Arquivo principal para execução do dashboard.

## 📦 Dependências Necessárias
Além do Python, será necessário instalar as seguintes dependências:
- **Pygame**
- **OBD-Python**
- **Kivy**
- **pip** (caso não esteja instalado)

### 1. Clonar o repositório
```bash
git clone https://github.com/Rochafelip/dashboard_python_fiat_obdII.git
cd dashboard_python_fiat_obdII
```

### 2. Instalar dependências
Certifique-se de ter o Python instalado e rode:
```bash
pip install -r requirements.txt
```
Caso precise instalar dependências manualmente:
```bash
pip install pygame obd kivy
```

### 3. Executar o dashboard
```bash
python main.py
```

## 📷 Capturas de Tela *(Opcional: Adicionar imagens da interface)*
### Loading Screen
![{41C26D0D-F2FC-4E0A-B370-4B17CEDA1CE0}](https://github.com/user-attachments/assets/5036c612-fc57-469d-9bfb-f644f0bcda5d)

### Home Screen
![{B0106C8D-0800-4111-9627-CDF15502FD1F}](https://github.com/user-attachments/assets/a526be25-68a0-490d-ac8c-9a6bfc014c39)

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

💡 **Sugestão**: Se desejar adicionar mais detalhes, como instruções de conexão ao OBD-II ou configuração do Raspberry Pi, podemos complementar o README! 😊

