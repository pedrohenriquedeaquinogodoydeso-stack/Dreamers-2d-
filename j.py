import pgzrun
import random
import time
import os

#textoa = ''
###############################################################################
# Campo do jogo
cell = Actor('piso_da_torre_crystal.png')#0
cell1 = Actor('piso_da_torre_crystal2.png')#1
cell2 = Actor("piso_da_torre_crystal6.png")#2
cell3 = Actor("piso_da_torre_crystal5.png")#3
cell5 = Actor('piso_da_torre_crystal5.png')#4
cell6 = Actor('parede_de_tijolo.png')#5
cellr = Actor("piso_da_torre_crystal3.png")#6
cellava = Actor('pisolava.png')

###############################################################################
size_w = 9 # Largura do campo em células
size_h = 11 # Altura do campo em células
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
win = 0 

brilho1 = Actor('brilho_1.png', topleft = (1 * cell.width, 1* cell.height))
brilho2 = Actor('brilho_2.png', topleft = (1 * cell.width, 1* cell.height))

nucleo_claro = Actor('nucleo-claro.png', topleft = (4 * cell.width, 3* cell.height))
nucleo_escuro = Actor('nucleo-escuro.png', topleft = (4 * cell.width, 3* cell.height))
dreamers = Actor('dreamers.png', topleft = (1 * cell.width, 1* cell.height), size=(2,2))
mode = 'tela_inicial' 
botaoinicio = True

ultimomode = False


TITLE = "Dreamers" # Título do jogo
FPS = 30 # Quadros por segundo


level = 1
pontos = 0
###############################################################################
# VARIÁVEIS DA MISSÃO
fala = ' '
dialogo1 = 0
dialogo2 = 0


activate = 0 
quest_1 = 0 # VAI ATÉ 5 personagens derrotados
mission = 0
queststext = [ ' ', 'Mate 5 inimigos (0/5)','Mate 5 inimigos (1/5)','Mate 5 inimigos (2/5)','Mate 5 inimigos (3/5)','Mate 5 inimigos (4/5)']


#####################################################################################################

my_map = [[6, 6, 6, 6, 6, 6, 6, 6, 6], 
          [1, 7, 7, 7, 7, 7, 7, 7, 2], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [0, 7, 7, 7, 7, 7, 7, 7, 3],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Linha usada para indicar os valores de vida e ataque

#outros mapas     
my_map2 = [[6, 6, 6, 6, 6, 6, 6, 6, 6], 
          [1, 7, 7, 7, 7, 7, 7, 7, 2], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [7, 7, 7, 7, 7, 7, 7, 7, 7], 
          [0, 7, 7, 7, 7, 7, 7, 7, 3],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]]

my_map3 = [[6, 6, 6, 6, 6, 6, 6, 6, 6], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8],
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [8, 8, 8, 8, 8, 8, 8, 8, 8], 
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]]

# Personagem principal
char = Actor('down.png')
char.top = cell.height
char.left = cell.width
char.health = 100
char.healthmax = 100



char.attack = 5
#NPC
npc = Actor("emo.png", topleft = (6 * cell.width, 5* cell.height))
area = Actor('areadecontato.png', topleft = (5 * cell.width, 4* cell.height))
areacura = Actor('areadecura.png', topleft = (1 * cell.width, 4* cell.height))
healer = Actor("healer.png", topleft = (2 * cell.width, 5* cell.height))
morreu = Actor('morreu.png', topleft = (50, 100))

lugarseta = 0 # alterna de 0 - 1 - 2 - 0 - 1. .....
lugarseta2 = 0
lugarsetainicio = 0 

menuativado = 0 # mostra o menu e restringe o movimento do jogador se for 1
seta = Actor("seta.png", topleft = (0 * cell.width, lugarseta * cell.height))
seta2 = Actor("seta.png", topleft = (3 * cell.width, lugarseta2 * cell.height))
setainicio = Actor("seta.png", topleft = (3 * cell.width, 7 * cell.height))
menu = Actor("menu.png", topleft = (0 * cell.width, 0* cell.height))

portal_promap2 = Actor("piso_da_torre_crystal4.png", topleft = (8 * cell.width, 3* cell.height))
portal_map1 = Actor("piso_da_torre_crystal4.png", topleft = (0 * cell.width, 3* cell.height))


# Gerando inimigos
enemies = []# posso usar um sistema de troca de mapa e nesse mapa 2 pode ter os inimigos gerados com o mesmo código da plataforma
enemies2 = []
for i in range(5):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height 
    enemy = Actor("enemy.png", topleft = (x , y))
    enemy.health = random.randint(10, 20)
    enemy.attack = random.randint(5, 10)
    enemy.bonus = random.randint(0, 3)
    enemies.append(enemy)

for i in range(1):
    x = random.randint(1, 7) * cell.width
    y = random.randint(1, 7) * cell.height 
    enemy = Actor("escorpiao.png", topleft = (x , y))
    enemy.health = random.randint(50, 100)
    enemy.attack = random.randint(10, 40)
    enemy.bonus = random.randint(0, 3)
    enemies2.append(enemy)

# FUNÇÕES CRIADAS

#ação do inimigo
def inimigo_atk():
    #
    
    #se a distância dele para o player for de 1 quadrado:
    #   atacar (Vida -= sla quantos pontos)
    #elif (o x é maior que 1 quadrado):
    #   se aproxima em X até o player
    #elif (o y é maior que 1 quadrado):
    #   se aproxima em y até o player
    pass



# Desenhando o mapa
def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 
            elif my_map[i][j] == 4:
                cell5.left = cell.width*j
                cell5.top = cell.height*i 
                cell5.draw()
            elif my_map[i][j] == 6:
                cell6.left = cell.width*j
                cell6.top = cell.height*i 
                cell6.draw()
            elif my_map[i][j] == 7:
                cellr.left = cell.width*j
                cellr.top = cell.height*i 
                cellr.draw()
            
def map_draw2():
    for i in range(len(my_map2)):
        for j in range(len(my_map2[0])):
            if my_map2[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map2[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map2[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map2[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 
            elif my_map2[i][j] == 4:
                cell5.left = cell.width*j
                cell5.top = cell.height*i 
                cell5.draw()
            elif my_map2[i][j] == 6:
                cell6.left = cell.width*j
                cell6.top = cell.height*i 
                cell6.draw()
            elif my_map2[i][j] == 7:
                cellr.left = cell.width*j
                cellr.top = cell.height*i 
                cellr.draw()

def map_draw3():
    for i in range(len(my_map3)):
        for j in range(len(my_map3[0])):
            if my_map3[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map3[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map3[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map3[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 
            elif my_map3[i][j] == 4:
                cell5.left = cell.width*j
                cell5.top = cell.height*i 
                cell5.draw()
            elif my_map3[i][j] == 6:
                cell6.left = cell.width*j
                cell6.top = cell.height*i 
                cell6.draw()
            elif my_map3[i][j] == 7:
                cellr.left = cell.width*j
                cellr.top = cell.height*i 
                cellr.draw()

def salvar_jogo():
    global level, mode, pontos
    save = open('jogo/save.txt', 'w')
    save.write(str(level) + '\n')
    save.write(str(mode)+ '\n')
    save.write(str(char.healthmax)+ '\n')
    save.write(str(char.health)+ '\n')
    save.write(str(char.attack)+ '\n')
    save.write(str(char.left) + '\n')
    save.write(str(char.top) + '\n')
    save.write(str(pontos) + '\n')
    save.close()
    print('jogo salvo')

def carregar_jogo():
    global level, mode, pontos
    if os.path.exists('jogo/save.txt'):
        save = open('jogo/save.txt', 'r')
        linhas = save.readlines()
        level = int(linhas[0].strip())
        mode = str(linhas[1].strip())
        char.healthmax = int(linhas[2].strip())
        char.health = int(linhas[3].strip())
        char.attack = int(linhas[4].strip())
        char.left = float(linhas[5].strip())
        char.top = float(linhas[6].strip())
        pontos = int(linhas[7].strip())
        save.close()
        print('jogo carregado')
    else:
        create_save()

def create_save():
    global level, mode, pontos
    level = 1 
    mode = 'tela_inicial'
    char.healthmax = 100
    char.health = 100
    char.attack = 5
    char.left = cell.width
    char.top = cell.height
    pontos = 0
    




# FUNÇÕES BÁSICAS

# Desenha tudo dentro dele
def draw():
    global activate, mode, fala, enemies, pontos # , textoa
    screen.clear()
    
    def texto(textoa):
        #global textoa
        
        #screen.clear()  
        #screen.fill("#000000") # sobrescreve o último texto
        screen.draw.text(textoa, topleft = (3 * cell.width, 355), color = 'white')
        #screen.draw.text('Jogar', (4 * cell.width, 355), color = 'white')
    
    

    if mode == 'game':
        
        screen.fill("#2f3542")
        map_draw()

        area.draw()
        areacura.draw()
        portal_promap2.draw()
        char.draw()
        screen.draw.text("HP:", (25, 475), color = 'white', fontsize = 20)
        screen.draw.text(str(char.health), (75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", (375, 480), color = 'white', fontsize = 20)
        screen.draw.text(str(char.attack), center=(425, 485), color = 'white', fontsize = 20)

        screen.draw.text(fala, (25, 500), color = 'white', fontsize = 20)#DIÁLOGO

        screen.draw.text('Lv: ' + str(level), (200, 520), color = 'white', fontsize = 20)#Level

        screen.draw.text(queststext[mission], (300, 450), color = 'white', fontsize = 20)#quest
        
        npc.draw() 
        healer.draw()
        if menuativado == 1:
            menu.draw()
            seta.draw()
    elif mode == 'map_2':
        screen.fill("#2f3542")
        map_draw2()
        if enemies == []:
            for i in range(5):
                x = random.randint(1, 7) * cell.width
                y = random.randint(1, 7) * cell.height 
                enemy = Actor("enemy.png", topleft = (x , y))
                enemy.health = random.randint(10, 20)
                enemy.attack = random.randint(5, 10)
                enemy.bonus = random.randint(0, 3)
                enemies.append(enemy)
        if menuativado == 1:
            menu.draw()
            seta.draw()
        
        portal_map1.draw()
        char.draw()
        screen.draw.text("HP:", (25, 475), color = 'white', fontsize = 20)
        screen.draw.text(str(char.health), (75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", (375, 480), color = 'white', fontsize = 20)
        screen.draw.text(str(char.attack), center=(425, 485), color = 'white', fontsize = 20)
        
        for i in range(len(enemies)):
            enemies[i].draw()
            screen.draw.text(str(enemies[i].health), (enemies[i].x + 5, enemies[i].y - 30), color = 'white', fontsize = 20)

        screen.draw.text(fala, (25, 500), color = 'white', fontsize = 20)#DIÁLOGO

        screen.draw.text('Lv: ' + str(level), (200, 520), color = 'white', fontsize = 20)#Level
            
        screen.draw.text(queststext[mission], (300, 450), color = 'white', fontsize = 20)#quest
    elif mode == 'intro': # FAZER O TEMPO DE DELAY DAS FUNÇÕES AAAAAAAAAAAAAAAAAAA
        screen.fill("#000000")
        nucleo_claro.draw()
        

        screen.draw.text('Há muito tempo atrás...', topleft = (3 * cell.width, 355), color = 'white')
        mode = 'intro_2'
    elif mode == 'intro_2':
        time.sleep(2)
        nucleo_claro.draw()
        screen.draw.text('Os sonhos eram seguros', topleft = (3 * cell.width, 355), color = 'white')
        screen.draw.text('por causa do seu núcleo', topleft = (3 * cell.width, 400), color = 'white')
        
        mode = 'intro_3'
    elif mode == 'intro_3':
        time.sleep(4)
        nucleo_escuro.draw()
        screen.draw.text('Mas um dia,', topleft = (3 * cell.width, 355), color = 'white')
        screen.draw.text('Um ser desconhecido corrompeu os núcleos', topleft = (1 * cell.width, 400), color = 'white')
        mode = 'intro_4'
    elif mode == 'intro_4':
        time.sleep(4)
        brilho1.draw()
        screen.draw.text('após a corrupção, pesadelos surgiram e', topleft = (1 * cell.width, 355), color = 'white')
        screen.draw.text('dominaram quase todo mundo dos sonhos.', topleft = (1 * cell.width, 400), color = 'white')
        mode = 'intro_5'
    elif mode == 'intro_5': 
        time.sleep(4)
        brilho2.draw()
        screen.draw.text('Sua missão é salvar o mundo dos sonhos', topleft = (1 * cell.width, 355), color = 'white')
        screen.draw.text('derrotando a morte, lider dos pesadelos.', topleft = (1 * cell.width, 400), color = 'white')
        mode = 'intro_6'#SÓ O TIME SLEEP
    elif mode == 'intro_6':
        time.sleep(5)
        mode = 'game'


    elif mode == 'tela_inicial':
        screen.fill("#000000") 
        setainicio.draw()
        #seleção do início
        dreamers.draw()
        screen.draw.text('Jogar', (4 * cell.width, 355), color = 'white')
        screen.draw.text('configurações', (4 * cell.width, 404), color = 'white')
        screen.draw.text('sair', (4 * cell.width, 453), color = 'red')


    elif mode == "end":
        screen.fill("black")
        morreu.draw()
        screen.draw.text("", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)# motivo da morte

    '''if activate == 1:#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        screen.draw.text("Hello Pygame Zero!", (50, 50))'''
    if ultimomode:
        screen.fill("#000000")
        screen.draw.text('Vida: ' + str(char.healthmax), center = (WIDTH//2, 49/2), color = 'white')
        screen.draw.text('Ataque: ' + str(char.attack), center = (WIDTH//2, 70), color = 'white')

        screen.draw.text('Pontos:' + str(pontos), center = (WIDTH//2, 400), color = 'white')
        seta2.draw()

        

# Controles == se Tecla do teclado for ativada(essa tecla)
def on_key_down(key):
    global activate, dialogo1, fala, quest_1, mission, mode, level, dialogo2, lugarseta, menuativado, ultimomode, pontos, lugarseta2, pontos, lugarsetainicio
    
    
    old_x = char.x
    old_y = char.y
    
    if keyboard.right and char.x + cell.width < WIDTH and menuativado == 0:
        char.x += cell.width
        char.image = 'right.png'
    elif keyboard.left and char.x - cell.width > 0 and menuativado == 0:
        char.x -= cell.width
        char.image = 'left.png'
    elif keyboard.down:
        if menuativado == 0 and char.y + cell.height < HEIGHT - cell.height*3:
            char.y +=  cell.height
            char.image = 'down.png'
        elif menuativado == 1:
            if seta.y != 122.5:
                seta.y += 49
        if ultimomode:
            if seta2.y != 122.5:
                seta2.y += 49 
        elif botaoinicio:
            if setainicio.y != 465.5:
                setainicio.y += 49
        
        
    elif keyboard.up:
        if menuativado == 0 and char.y - cell.height > 0:
            char.y -= cell.height
            char.image = 'up.png'
        elif menuativado == 1:
            if seta.y != 24.5:
                seta.y -= 49
        if ultimomode:
            if seta2.y != 24.5:
                seta2.y -= 49 
        elif botaoinicio:
            if setainicio.y != 367.5:
                setainicio.y -= 49
            
    elif keyboard.z:
        if menuativado == 0:
            if char.colliderect(portal_promap2):
                mode = 'map_2'
                char.x = portal_map1.x + 1 * cell.width
            if char.colliderect(portal_map1):
                mode = 'game'
                char.x = portal_promap2.x - 1 * cell.width
        elif menuativado == 1 and ultimomode == False: # se tenta entrar em algo do menu
            if lugarseta == 1: #status
                ultimomode = True
            elif lugarseta == 2:#inventário
                pass
            elif lugarseta == 3:#sair FEITO
                #salvar
                salvar_jogo()
                quit()
        elif ultimomode == True and lugarseta2 == 1 and pontos > 0: #se tenta melhorar vida
            pontos -= 1
            char.healthmax += 25
        elif ultimomode == True and lugarseta2 == 2 and pontos > 0: # se tenta melhorar ataque
            pontos -= 1
            char.attack += 5
        if botaoinicio and mode == 'tela_inicial': #BOTÕES DO INICIO DO JOGO
            
            if lugarsetainicio == 1:
                if os.path.exists('jogo/save.txt'):
                    carregar_jogo() 
                else:
                    mode = 'intro' # COLOCAR INTRO DEPOIS
                
            elif lugarsetainicio == 2:
                pass # ATIVA AS SETTINGS
            elif lugarsetainicio == 3:
                salvar_jogo()
                quit()
	        

    elif keyboard.m:
        if menuativado == 1:
            menuativado = 0
            lugarseta = 0
        elif menuativado == 0:
            menuativado = 1
    elif keyboard.r and mode == 'end':
        char.health = char.healthmax
        char.x = 5 * cell.width /2
        char.y = 7 * cell.height
        mode = 'game'

    if seta.y == 24.5:
        lugarseta = 1
    elif seta.y == 73.5:
        lugarseta = 2
    elif seta.y == 122.5:
        lugarseta = 3

    if seta2.y == 24.5:
        lugarseta2 = 1
    elif seta2.y == 73.5:
        lugarseta2 = 2
    elif seta2.y == 122.5:
        lugarseta2 = 3
    
    if setainicio.y == 367.5:
        lugarsetainicio = 1
    elif setainicio.y == 416.5: 
        lugarsetainicio = 2
    elif setainicio.y == 465.5:
        lugarsetainicio = 3
    
    if char.colliderect(area):
        if keyboard.z and mode == 'game':
            if dialogo1 == 0:
                fala = 'Olá sonhador'
                dialogo1 = 1
            elif dialogo1 == 1:
                fala = 'Você pode derrotar 5 monstros para mim? Sim -  Z'
                dialogo1 = 2
            elif dialogo1 == 2:
                fala = 'Vá em frente'
                quest_1 = 0
                mission = 1
    elif char.colliderect(areacura):
        if keyboard.z and mode == 'game':
            if dialogo2 == 0:
                fala = 'Olá sonhador'
                dialogo2 = 1
            elif dialogo2 == 1:
                fala = 'Quer que eu te cure? Sim - [Z]'
                dialogo2 = 2
            elif dialogo2 == 2:
                fala = 'Perfeitamente curado'
                char.health = char.healthmax #condição para curar mais com base no nível
    #Areas de missões                     
    else:
        fala = ' '
        dialogo1 = 0
        dialogo2 = 0

    if keyboard.x:#voltar
        if ultimomode == True:
            ultimomode = False
        elif menuativado == 1:
            menuativado = 0


    npc_index = char.colliderect(npc)
    enemy_index = char.collidelist(enemies)
    healer_index = char.colliderect(healer)
    if npc_index == 1 and mode == 'game' or healer_index == 1 and mode == 'game': #OR -TODAS AS COISAS QUE ELE BATE
        char.x = old_x
        char.y = old_y
    if enemy_index != -1 and mode == 'map_2':
        char.x = old_x
        char.y = old_y
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            enemies.pop(enemy_index)
            if mission == 1:
                mission = 2
            elif mission == 2:
                mission = 3
            elif mission == 3:
                mission = 4
            elif mission == 4:
                mission = 5
            elif mission == 5:
                mission = 0
                char.health = char.healthmax

                level += 1
                pontos += 1
    if char.health <= 1:#GAME OVER
         mode = "end"
            


#atualiza cada frame com base no FPS definido lá em cima
def update(dt):
    pass


pgzrun.go()

