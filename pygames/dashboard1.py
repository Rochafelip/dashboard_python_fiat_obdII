import pygame
import os

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
SHADOW_COLOR = (50, 50, 50)  
SHADOW_OFFSET = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
SHADOW_COLOR = (50, 50, 50)
SHADOW_OFFSET = 2
SEMI_TRANSPARENT_BG = (0, 0, 0, 150)  # Fundo semi-transparente

# Inicializar o Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dashboard do Carro")

# Verificar se a fonte existe
font_path = 'assets/designer_2/Designer.otf'
if not os.path.exists(font_path):
    print("[AVISO] Fonte não encontrada. Usando fonte padrão.")
    font_path = None  

# Carregar fonte
font = pygame.font.Font(font_path, 45) if font_path else pygame.font.Font(None, 40)
def draw_text_with_shadow(screen, text, font, color, x, y):
    shadow = font.render(text, True, SHADOW_COLOR)
    text_surface = font.render(text, True, color)
    screen.blit(shadow, (x + SHADOW_OFFSET, y + SHADOW_OFFSET))
    screen.blit(text_surface, (x, y))

def draw_obd_warning(screen):
    font_warning = pygame.font.Font(font_path, 25) if font_path else pygame.font.Font(None, 25)
    warning_text = "OBD-II NÃO DETECTADO"
    text_surface = font_warning.render(warning_text, True, RED)
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT - 50))

def draw_rpm_bar(screen, rpm):
    max_rpm = 6000  
    bar_width = SCREEN_WIDTH - 80
    bar_height = 20
    bar_x = 40
    bar_y = 50

    rpm_ratio = min(rpm / max_rpm, 1)
    filled_width = int(bar_width * rpm_ratio)

    pygame.draw.rect(screen, DARK_RED, (bar_x, bar_y + 2, bar_width, bar_height), border_radius=6)

    for i in range(5):
        shade = max(50, 255 - (i * 50))
        pygame.draw.rect(screen, (shade, 0, 0), (bar_x, bar_y + i, filled_width, bar_height - (i * 2)), border_radius=6)

    pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height), 2, border_radius=6)
    font_rpm = pygame.font.Font(font_path, 25) if font_path else pygame.font.Font(None, 25)
    draw_text_with_shadow(screen, str(rpm), font_rpm, YELLOW, bar_x, bar_y - 30)

def draw_sensor_box(screen, sensors):
    box_x = 40
    box_y = 90
    box_width = SCREEN_WIDTH - 80
    box_height = 150

    # Criando um fundo semi-transparente
    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    box_surface.fill(SEMI_TRANSPARENT_BG)
    screen.blit(box_surface, (box_x, box_y))

    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height), 2, border_radius=10)

    col_x_positions = [box_x + (box_width // 4), box_x + (box_width // 4) * 3]
    row_start_y = box_y + 25
    row_spacing = 40

    for i, (label, _) in enumerate(sensors):
        column = i % 2
        row = i // 2
        text_x = col_x_positions[column]
        text_y = row_start_y + row * row_spacing
        draw_text_with_shadow(screen, label, font, WHITE, text_x - font.size(label)[0] // 2, text_y)
        
def draw_sensor_box2(screen, sensors):
    box_x = 23
    box_y = 60  # Ajustar posição vertical
    box_width = SCREEN_WIDTH - 50  # Aumentar um pouco a largura
    box_height = 200  # Mais altura para acomodar bem as linhas

    # Desenha a caixa
    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height), 2, border_radius=10)

    row_start_y = box_y + 30  # Melhorar espaçamento superior
    row_spacing = 40  # Aumentar espaçamento entre linhas

    for i, (label, _) in enumerate(sensors):
        font_dashboar2 = pygame.font.Font(font_path, 30) if font_path else pygame.font.Font(None, 35)
        text_surface = font_dashboar2.render(label, True, WHITE)
        text_width, text_height = text_surface.get_size()

        # Centralizar horizontalmente
        text_x = box_x + (box_width - text_width) // 2
        text_y = row_start_y + i * row_spacing

        # Renderiza o texto na tela
        screen.blit(text_surface, (text_x, text_y))

        
def load_image_safe(path):
    if os.path.exists(path):
        return pygame.image.load(path)
    else:
        print(f"[AVISO] Imagem {path} não encontrada.")
        return None

def loading_screen(screen):
    loading_img = load_image_safe('assets/FiatLoading.png')
    if loading_img:
        loading_img = pygame.transform.scale(loading_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:
        if loading_img:
            screen.blit(loading_img, (0, 0))
        pygame.display.update()

def dashboard_screen(screen, rpm, speed, temp, intake_air_temp, throttle_position, obd_connected):
    screen.fill(BLACK)
    background_img = load_image_safe('assets/logo.png')
    if background_img:
        background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background_img, (0, 0))
    sensors = [
        (f"{speed} km/h", speed),
        (f"{temp} °C", temp),
        (f"{throttle_position:.2f}%", throttle_position),
        (f"{intake_air_temp} °C", intake_air_temp),
    ]
    draw_rpm_bar(screen, rpm)
    draw_sensor_box(screen, sensors)
    if not obd_connected:
        draw_obd_warning(screen)

def dashboard_screen_2(screen, avg_consumption, inst_consumption, avg_distance, total_distance):
    screen.fill(BLACK)
    
    background_img = load_image_safe('assets/logo.png')
    if background_img:
        background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background_img, (0, 0))

    sensors = [
        (f"Avg Cons: {avg_consumption:.2f} km/L", avg_consumption),
        (f"Avg Inst: {inst_consumption:.2f} km/L", inst_consumption),
        (f"Avg Dist: {avg_distance:.2f} km", avg_distance),
        (f"Total Dist: {total_distance:.2f} km", total_distance),
    ]
    draw_sensor_box2(screen, sensors)

running = True
current_screen = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_screen = 2 if current_screen == 1 else 1
    
    if current_screen == 1:
        dashboard_screen(screen, 3000, 80, 90, 35, 45, True)
    else:
        dashboard_screen_2(screen, 12.5, 8.3, 250, 500)
    
    pygame.display.update()
pygame.quit()
