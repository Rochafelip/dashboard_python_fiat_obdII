import pygame

# Configuração da tela
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
SHADOW_COLOR = (50, 50, 50)  # Cor da sombra do texto
SHADOW_OFFSET = 2  # Deslocamento da sombra em pixels

# Inicializar o Pygame
pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dashboard do Carro")

# Fonte digital
font_path = 'assets/designer_2/Designer.otf'
font = pygame.font.Font(font_path, 40)

def draw_text_with_shadow(screen, text, font, color, x, y):
    """ Renderiza um texto com sombra para melhorar a legibilidade """
    shadow = font.render(text, True, SHADOW_COLOR)
    text_surface = font.render(text, True, color)

    # Desenhar a sombra deslocada
    screen.blit(shadow, (x + SHADOW_OFFSET, y + SHADOW_OFFSET))
    # Desenhar o texto principal por cima
    screen.blit(text_surface, (x, y))

def draw_rpm_bar(screen, rpm):
    """ Desenha a barra de RPM com efeito de brilho e melhor contraste """
    max_rpm = 6000  
    bar_width = SCREEN_WIDTH - 80
    bar_height = 20
    bar_x = 40
    bar_y = 50

    rpm_ratio = min(rpm / max_rpm, 1)
    filled_width = int(bar_width * rpm_ratio)

    # Fundo da barra (sombra)
    pygame.draw.rect(screen, DARK_RED, (bar_x, bar_y + 2, bar_width, bar_height), border_radius=6)

    # Criando gradiente de brilho
    for i in range(5):
        shade = max(50, 255 - (i * 50))  # Criando tons mais claros
        pygame.draw.rect(screen, (shade, 0, 0), (bar_x, bar_y + i, filled_width, bar_height - (i * 2)), border_radius=6)

    # Contorno da barra
    pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height), 2, border_radius=6)

    font_rpm = pygame.font.Font(font_path, 25)
    draw_text_with_shadow(screen, str(rpm), font_rpm, YELLOW, bar_x, bar_y - 30)

def draw_sensor_box(screen, sensors):
    """ Desenha a caixa dos sensores com borda arredondada e alinhamento melhorado """
    box_x = 40
    box_y = 90
    box_width = SCREEN_WIDTH - 80
    box_height = 130

    # Caixa com borda arredondada
    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height), 2, border_radius=10)

    # Configuração do layout
    col_x_positions = [
        box_x + (box_width // 4),  # Centro da primeira coluna
        box_x + (box_width // 4) * 3  # Centro da segunda coluna
    ]
    row_start_y = box_y + 20
    row_spacing = 40

    # Exibir os sensores centralizados com sombra
    for i, (label, _) in enumerate(sensors):
        column = i % 2
        row = i // 2
        text_x = col_x_positions[column]
        text_y = row_start_y + row * row_spacing
        draw_text_with_shadow(screen, label, font, WHITE, text_x - font.size(label)[0] // 2, text_y)
        
        # Função para exibir mensagem de desconexão OBD2
def display_no_connection_message(screen):
    font = pygame.font.Font(None, 36)
    text_surface = font.render('No OBD-II connection', True, YELLOW)
    screen.blit(text_surface, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2))

def loading_screen(screen):
    loading_img = pygame.image.load('assets/FiatLoading.png')
    loading_img = pygame.transform.scale(loading_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    start_time = pygame.time.get_ticks()
    
    while pygame.time.get_ticks() - start_time < 3000:  # Espera 3 segundos
        screen.blit(loading_img, (0, 0))
        pygame.display.update()

def dashboard_screen(screen, rpm, speed, temp, intake_air_temp, throttle_position):
    """ Renderiza a tela principal do dashboard """
    screen.fill(BLACK)  # Fundo preto

    # Carregar e exibir a imagem de fundo
    background_img = pygame.image.load('assets/logo.png')
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background_img, (0, 0))

    # Desenhar a barra de RPM
    draw_rpm_bar(screen, rpm)

    # Sensores a serem exibidos
    sensors = [
        (f"{speed} km/h", speed),
        (f"{temp} °C", temp),
        (f"{intake_air_temp} °C", intake_air_temp),
        (f"{throttle_position:.2f}%", throttle_position),
    ]

    # Desenhar a caixa de sensores
    draw_sensor_box(screen, sensors)

    # Loop principal de execução
    running = True
    clock = pygame.time.Clock()
    rpm = 3500
    speed = 80
    temp = 90
    intake_air_temp = 35
    throttle_position = 45.5

    dashboard_screen(screen, rpm, speed, temp, intake_air_temp, throttle_position)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
