import pgzero, pgzrun, pygame, math

# Tamanho da tela
HEIGHT = 900
WIDTH = 800

# Define os atores (Ciso é os CIlios e a SOmbrancelha juntos)
shuriken = Actor('shuriken')
branco = Actor('branco')
pupila1 = Actor('pupila1')
pupila2 = Actor('pupila2')
ciso = Actor('ciso')

# Cria o overlay do poder do sharingan e do cabelo
overlay_efeito_sharingan = pygame.image.load('images/efeito_sharingan.png')
efeito_sharingan = pygame.transform.scale(overlay_efeito_sharingan, (WIDTH, HEIGHT))
overlay_cabelo = pygame.image.load('images/cabelo.png')
cabelo = pygame.transform.scale(overlay_cabelo, (WIDTH, HEIGHT-200))

# Define a posição das pupilas
pupila1.pos = ((WIDTH/2)-225,(HEIGHT/2)+20)
pupila2.pos = ((WIDTH/2)+225,(HEIGHT/2)+20)

# Define a variável poder e tempo
Poder = False
Tempo_poder = 0

# Desenha as pupilas, o cabelo, a shuriken, a esclera, o rosto e os textos
def draw():
    global Poder

    screen.fill((244,217,208))
    branco.pos = ((WIDTH/2)-225,(HEIGHT/2)+20)
    branco.draw()
    move_pupila(pupila1)
    pupila1.draw()
    branco.pos = ((WIDTH/2)+225,(HEIGHT/2)+20)
    branco.draw()    
    move_pupila(pupila2)
    pupila2.draw()
    ciso.pos = ((WIDTH/2),(HEIGHT/2)+200)
    ciso.draw()
    screen.blit(cabelo, (0,0))
    screen.draw.text('Sasuke  Uchiha', ((WIDTH/5), 100), fontname="njnaruto", fontsize=60, color=( 255, 255, 255), align="center", shadow=(2,2), scolor="#202020")
    screen.draw.text('Aperte  ESPACO  para  ativar  o  poder  do  sharingan!', ((WIDTH/5), 180), fontname="njnaruto", fontsize=20, color=( 255, 255, 255), align="center", shadow=(2,2), scolor="#202020")
    shuriken.draw()
 
    if Poder:
        screen.blit(efeito_sharingan, (0,0))

# Essa função que dá animação e vida as pupílas para se moverem
def move_pupila(self):
    global Poder

    distancia_x = shuriken.x - branco.x
    distancia_y = shuriken.y - branco.y
    angulo = calc_angulo(distancia_x, distancia_y)
    if Poder:
        animate(self, pos=((branco.x + calc_deslocax(angulo)), (branco.y + calc_deslocay(angulo))), tween="linear", duration=0.1)
    else:
        animate(self, pos=((branco.x + calc_deslocax(angulo)), (branco.y + calc_deslocay(angulo))), tween="linear", duration=1)
    
# Faz os cálculos dos angulos, senos, arcotangente dos olhos   
def calc_angulo(x, y):
    return math.atan2(y, x)
def calc_deslocax(angulo):
    return 25*math.cos(angulo)
def calc_deslocay(angulo):
    return 25*math.sin(angulo)

# Verifica se o espaço foi apertado para ativar o poder
def on_key_down(key):
    global Poder

    if key == keys.SPACE and Poder == False:
        Poder = True

# Função que administra o poder do sharingan        
def sharingan():
    global Poder, Tempo_poder
    if Poder == True and Tempo_poder == 0:
        sounds.sharingan.play()
        
    if Poder:
        animate(shuriken, pos=(pygame.mouse.get_pos()), tween="linear", duration=1)
        shuriken.angle -= 1
        Tempo_poder += 1
        pupila1.angle += 10
        pupila2.angle += 10
        
    else:
        animate(shuriken, pos=(pygame.mouse.get_pos()), tween="linear", duration=0.1)
        shuriken.angle -= 10

    if Tempo_poder >= 500:
        Poder = False
        Tempo_poder = 0
        pupila1.angle = 0
        pupila2.angle = 0

# Função que atualiza o projetp
def update():
    sharingan()
    pass

# Inicia a tela
pgzrun.go()