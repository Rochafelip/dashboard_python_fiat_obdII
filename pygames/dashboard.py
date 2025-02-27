import pygame

# Configuração da tela
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Cores definidas diretamente no contexto do Pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)

# Função para desenhar a barra de RPM
def draw_rpm_bar(screen, rpm):
    if rpm is not None:
        rpm_percentage = rpm * 0.1  # Escala para ajustar o comprimento da barra
        rpm_width = min(rpm_percentage, SCREEN_WIDTH - 20)  # Limitar o comprimento ao tamanho da tela
        rpm_height = 30  # Espessura da barra
        color = RED if rpm >= 2500 else GREEN  # Muda a cor baseado no valor do RPM
        
        # Desenhar barra
        pygame.draw.rect(screen, color, (10, 10, rpm_width, rpm_height))
        
        # Exibir valor de RPM no canto esquerdo da barra
        font = pygame.font.Font(None, 24)
        rpm_label = font.render(f"RPM: {rpm}", True, YELLOW)
        screen.blit(rpm_label, (15, 15))

# Função para exibir mensagem de desconexão OBD2
def display_no_connection_message(screen):
    font = pygame.font.Font(None, 36)
    text_surface = font.render('No OBD-II connection', True, YELLOW)
    screen.blit(text_surface, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2))

# Função para desenhar a tela de Loading
def loading_screen(screen):
    # Carregar imagem de fundo para o Loading
    loading_img = pygame.image.load('assets/FiatLoading.png')
    loading_img = pygame.transform.scale(loading_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(loading_img, (0, 0))

# Função para desenhar o Dashboard com duas colunas
def dashboard_screen(screen, rpm, speed, temp, lambda_value, intake_air_temp, throttle_position):
    screen.fill(BLACK)  # Fundo preto
    
    # Carregar imagem de fundo para o Loading
    loading_img = pygame.image.load('assets/logo.png')
    loading_img = pygame.transform.scale(loading_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(loading_img, (0, 0))
    
    
    # Dados do OBD com rótulos
    sensors = [
        (f"RPM: {rpm} RPM", rpm),
        (f"Speed: {speed} km/h", speed),
        (f"Temp Motor: {temp} °C", temp),
        (f"Intake Air Temp: {intake_air_temp} °C", intake_air_temp),           
        (f"Throttle Position: {throttle_position:.2f}%", throttle_position),
        (f"Lambda: {lambda_value:.2f}", lambda_value),
    ]
    
    # Configuração de layout
    font = pygame.font.Font(None, 30)
    row_start_y = 50
    row_spacing = 40
    bar_height = 30

    # Exibir os sensores, sendo a barra de RPM a primeira
    for i, (label, value) in enumerate(sensors):
        if i == 0:  # RPM com barra especial
            pygame.draw.rect(screen, GRAY, (50, row_start_y, SCREEN_WIDTH - 100, bar_height))
            rpm_percentage = min(rpm / 5000, 1.0) * (SCREEN_WIDTH - 100)  # Limite de escala
            color = RED if rpm >= 2500 else GREEN
            pygame.draw.rect(screen, color, (50, row_start_y, rpm_percentage, bar_height))
            rpm_text = font.render(label, True, YELLOW)
            screen.blit(rpm_text, (55, row_start_y - 25))  # Texto acima da barra
            row_start_y += row_spacing
        else:
            sensor_surface = font.render(label, True, WHITE)
            screen.blit(sensor_surface, (50, row_start_y))
            row_start_y += row_spacing
