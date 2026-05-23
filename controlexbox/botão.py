import pygame

# Inicializa o Pygame
pygame.init()

# Inicializa o joystick (controle)
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("Nenhum controle detectado.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Funções para obter informações sobre o controle
def get_button_name(button_id):
    """Retorna o nome do botão."""
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
        return "Unknown"


        
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONDOWN:
            button_name = get_button_name(event.button)
            print(f"Botão pressionado: {button_name}")
        

    pygame.time.delay(10)  # Pequeno atraso para evitar uso excessivo da CPU

# Encerra o Pygame
pygame.quit()