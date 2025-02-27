import pygame
import random
import obd
from dashboard1 import loading_screen, dashboard_screen, display_no_connection_message

# Configuração da tela
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dashboard do Carro')

# Cores definidas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicializa conexão com OBD2
connection = obd.OBD()  # Tenta conectar automaticamente
obd_connected = connection.is_connected()

# Função para obter dados do OBD2
def get_obd_data():
    if obd_connected:
        rpm = connection.query(obd.commands.RPM).value or 0
        speed = connection.query(obd.commands.SPEED).value or 0
        temp = connection.query(obd.commands.COOLANT_TEMP).value or 0
        intake_air_temp = connection.query(obd.commands.INTAKE_TEMP).value or 0
        throttle_position = connection.query(obd.commands.THROTTLE_POS).value or 0
        return rpm, speed, temp, intake_air_temp, throttle_position
    else:
        return get_obd_data_simulation()

# Função para gerar dados simulados
def get_obd_data_simulation():
    simulated_rpm = random.randint(0, 6000)
    simulated_speed = random.randint(0, 200)
    simulated_temp = random.randint(0, 120)
    simulated_intake_air_temp = random.randint(20, 50)
    simulated_throttle_position = random.uniform(0, 100)
    return simulated_rpm, simulated_speed, simulated_temp, simulated_intake_air_temp, simulated_throttle_position

# Função para exibir o status de conexão OBD2
def draw_connection_status(screen, status):
    font = pygame.font.Font(None, 30)
    text = f"OBD2: {'Conectado' if status else 'Falha na Conexão'}"
    color = GREEN if status else RED
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (10, 10))  # Exibir no canto superior esquerdo
    
# Exibir tela de loading antes de iniciar o dashboard
loading_screen(screen)
pygame.display.update()  # Atualizar a tela para exibir o loading
pygame.time.delay(3000)  # Esperar 3 segundos antes de continuar

# Loop principal do dashboard
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)  # Limpar a tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obter dados do OBD2 ou simulação
    rpm, speed, temp, intake_air_temp, throttle_position = get_obd_data()

    # Exibir o dashboard
    dashboard_screen(screen, rpm, speed, temp, intake_air_temp, throttle_position)

    # Exibir status de conexão com OBD2
    draw_connection_status(screen, obd_connected)

    pygame.display.flip()  # Atualizar a tela
    clock.tick(60)  # Controlar FPS

pygame.quit()
