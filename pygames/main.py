import obd
import pygame
import random
from dashboard import loading_screen, dashboard_screen,  display_no_connection_message

# Configuração da tela
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dashboard do Carro')

# Cores definidas
BLACK = (0, 0, 0)

# Conectar ao OBD2
connection = obd.OBD("/dev/rfcomm0")

# Comando para obter a velocidade do carro
cmd = obd.commands.SPEED
response = connection.query(cmd)

print("Velocidade:", response.value)  # Deve exibir a velocidade em km/h

def get_obd_data():
    rpm = connection.query(obd.commands.RPM).value.magnitude if connection.supports(obd.commands.RPM) else 0
    speed = connection.query(obd.commands.SPEED).value.magnitude if connection.supports(obd.commands.SPEED) else 0
    temp = connection.query(obd.commands.COOLANT_TEMP).value.magnitude if connection.supports(obd.commands.COOLANT_TEMP) else 0
    intake_air_temp = connection.query(obd.commands.INTAKE_TEMP).value.magnitude if connection.supports(obd.commands.INTAKE_TEMP) else 0
    throttle_position = connection.query(obd.commands.THROTTLE_POS).value.magnitude if connection.supports(obd.commands.THROTTLE_POS) else 0
    lambda_value = 1  # Lambda não é um dado padrão, então pode precisar de um cálculo específico
    
    return rpm, speed, temp, lambda_value, intake_air_temp, throttle_position

# Loop principal
running = True
clock = pygame.time.Clock()

# Estado inicial
loading = True
loading_timer = 0
loading_time = 3  # Tempo da tela de carregamento (em segundos)

while running:
    screen.fill(BLACK)  # Limpar a tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if loading:
        loading_screen(screen)
        loading_timer += clock.get_time() / 1000  # Converter milissegundos para segundos
        if loading_timer >= loading_time:
            loading = False  # Encerrar a tela de carregamento
    else:
        # Obter dados simulados
        rpm, speed, temp, lambda_value, intake_air_temp, throttle_position = get_obd_data_simulation()

        # Exibir dados do dashboard
        dashboard_screen(screen, rpm, speed, temp, lambda_value, intake_air_temp, throttle_position)

    pygame.display.flip()  # Atualizar a tela
    clock.tick(60)  # Controlar os frames por segundo

pygame.quit()
