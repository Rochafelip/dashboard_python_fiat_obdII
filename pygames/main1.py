import pygame
import random
import obd
from dashboard1 import loading_screen, dashboard_screen, dashboard_screen_2

# Configuração da tela
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dashboard do Carro')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

connection = obd.OBD()
obd_connected = connection.is_connected()

if not obd_connected:
    print("[AVISO] OBD-II não encontrado! Usando valores simulados.")

def get_obd_data():
    if obd_connected:
        def safe_query(cmd):
            response = connection.query(cmd)
            return response.value if response and response.value is not None else None
        
        rpm = safe_query(obd.commands.RPM)
        speed = safe_query(obd.commands.SPEED)
        temp = safe_query(obd.commands.COOLANT_TEMP)
        intake_air_temp = safe_query(obd.commands.INTAKE_TEMP)
        throttle_position = safe_query(obd.commands.THROTTLE_POS)
        
        return rpm, speed, temp, intake_air_temp, throttle_position
    else:
        return None, None, None, None, None


def get_obd_data_simulation():
    return (0, 0, 0, 0, 0)

def draw_connection_status(screen, status):
    font = pygame.font.Font(None, 30)
    text = f"OBD2: {'Conectado' if status else 'Falha na Conexão'}"
    color = GREEN if status else RED
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (10, 10))

loading_screen(screen)
pygame.display.update()
pygame.time.delay(3000)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = get_obd_data()
    if obd_connected and all(value is not None for value in data):
        rpm, speed, temp, intake_air_temp, throttle_position = data
    else:
        rpm, speed, temp, intake_air_temp, throttle_position = get_obd_data_simulation()

    dashboard_screen(screen, rpm, speed, temp, intake_air_temp, throttle_position, obd_connected)
    draw_connection_status(screen, obd_connected)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
