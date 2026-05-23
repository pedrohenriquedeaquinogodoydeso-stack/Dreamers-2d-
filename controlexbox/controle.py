import pygame
import sys

# Inicializa o Pygame e o módulo de joystick
pygame.init()
pygame.joystick.init()

# Verifica se há controles conectados
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Nenhum controle detectado.")
    pygame.quit()
    sys.exit()

# Obtém o primeiro controle detectado
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Controle detectado: " + joystick.get_name())

# Função para obter o nome do botão com base no seu ID
def get_button_name(button_id):
    """Retorna o nome do botão para um controle Xbox."""
    if button_id == 0:
        return "A"
    elif button_id == 1:
        return "B"
    elif button_id == 2:
        return "X"
    elif button_id == 3:
        return "Y"
    elif button_id == 4:
        return "LB"
    elif button_id == 5:
        return "RB"
    elif button_id == 6:
        return "Back"
    elif button_id == 7:
        return "Start"
    elif button_id == 8:
        return "Xbox"
    elif button_id == 9:
        return "L3"
    elif button_id == 10:
        return "R3"
    else:
        return "Botao " + str(button_id)

# Loop principal para capturar eventos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Evento de botão pressionado
        if event.type == pygame.JOYBUTTONDOWN:
            button_name = get_button_name(event.button)
            print("Botão pressionado: " + button_name)

        # Evento de movimento do D-pad (hat)
        if event.type == pygame.JOYHATMOTION:
            hat_id = event.hat
            hat_pos = event.value
            
            # O hat ID 0 é geralmente o D-pad principal
            if hat_id == 0:
                x, y = hat_pos
                
                # Para cima
                if y == 1:
                    print("D-pad: Cima")
                # Para baixo
                elif y == -1:
                    print("D-pad: Baixo")
                
                # Para esquerda
                if x == -1:
                    print("D-pad: Esquerda")
                # Para direita
                elif x == 1:
                    print("D-pad: Direita")
                
                # Posição neutra
                if x == 0 and y == 0:
                    print("D-pad: Neutro")

    pygame.time.delay(10)  # Pequeno atraso para evitar uso excessivo da CPU

# Encerra o Pygame
pygame.quit()