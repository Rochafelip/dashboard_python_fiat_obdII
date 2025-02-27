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

# Função para simular dados OBD2
def get_obd_data_simulation():
    simulated_rpm = random.randint(0, 6000)  # RPM ajustado ao limite da barra
    simulated_speed = random.randint(0, 200)  # Limite aumentado para 200 km/h
    simulated_temp = random.randint(0, 120)  # Ajuste para temperatura do motor
    simulated_lambda = random.uniform(0.85, 1.25)  # Valores mais precisos
    simulated_intake_air_temp = random.randint(20, 50)  # Temperatura do ar de entrada
    simulated_throttle_position = random.uniform(0, 100)  # Posição do acelerador
    return simulated_rpm, simulated_speed, simulated_temp, simulated_lambda, simulated_intake_air_temp, simulated_throttle_position


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
