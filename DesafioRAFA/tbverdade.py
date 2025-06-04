import pygame
import random
# Inicia o jogo
pygame.init()

# Determina as cores que vão aparecer no jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (185, 240, 208)
RED = (247, 148, 233)
GRAY = (180, 180, 180)
BLUE = (176, 186, 255)

# Define as propriedades da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desafio da Verdade")

# Fontes usadas
FONT = pygame.font.SysFont('Arial', 28)
BIG = pygame.font.SysFont('Arial', 36)

# Botões
true_button = pygame.Rect(150, 450, 150, 60)
false_button = pygame.Rect(500, 450, 150, 60)

# Responsável por transformar o True em V e False em F
def bool_str(b):
    return "V" if b else "F"

# Vai montar a proposição que vai ser analisada
def avaliar_expr(P, Q, R, expr):
    contexto = {"P": P, "Q": Q, "R": R}
    return eval(expr, {"__builtins__": None}, contexto)

# Responsável por criar as dificuldades do jogo
def gerar_expr(nivel):
    P, Q, R = random.choice([True, False]), random.choice([True, False]), random.choice([True, False])
    if nivel == "Fácil":
        op = random.choice(["and", "or"])
        expr = f"P {op} Q"
    elif nivel == "Médio":
        op = random.choice(["not P or Q", "not Q and P", "P and Q", "P or Q"])
        expr = op
    else:  # Difícil
        op1 = random.choice(["and", "or"])
        op2 = random.choice(["and", "or"])
        expr = f"(P {op1} Q) {op2} R"
    resultado = avaliar_expr(P, Q, R, expr)
    visivel = expr.replace("and", "AND").replace("or", "OR").replace("not", "NOT")
    return P, Q, R, visivel, resultado

# Responsável por carregar todos os textos no pygame
def desenhar_texto(texto, x, y, fonte=FONT, cor=BLACK):
    img = fonte.render(texto, True, cor)
    screen.blit(img, (x, y))

# Vai carregar os botões
def menu_nivel():
    bot_f = pygame.Rect(100, 200, 200, 60)
    bot_m = pygame.Rect(100, 300, 200, 60)
    bot_d = pygame.Rect(100, 400, 200, 60)
    while True:
        screen.fill(WHITE)
        desenhar_texto("Escolha o Nível", 100, 100, BIG)
        pygame.draw.rect(screen, GREEN, bot_f)
        pygame.draw.rect(screen, BLUE, bot_m)
        pygame.draw.rect(screen, RED, bot_d)
        desenhar_texto("Fácil", 160, 215)
        desenhar_texto("Médio", 155, 315)
        desenhar_texto("Difícil", 150, 415)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bot_f.collidepoint(event.pos):
                    return "Fácil"
                if bot_m.collidepoint(event.pos):
                    return "Médio"
                if bot_d.collidepoint(event.pos):
                    return "Difícil"

# Vai mostrar o resultado final com uma frase de incentivo
def fim_jogo(pontos):
    screen.fill(WHITE)
    desenhar_texto(f"Você acertou {pontos} de 5!", 100, 200, BIG)
    if pontos == 5:
        desenhar_texto("🎉 Perfeito! Você já apresenta domínio dos conteúdos!", 100, 260)
    elif pontos >= 3:
        desenhar_texto("👍 Muito bem! Continue sempre se aprimorando, está ", 100, 260)
        desenhar_texto("no caminho certo!", 100, 300)
    else:
        desenhar_texto("📘 Continue praticando! Errar faz parte do ", 100, 260)
        desenhar_texto("processo de aprendizado, não desista!", 100, 300)
    desenhar_texto("Clique para jogar novamente...", 100, 350)
    pygame.display.flip()
    pygame.time.wait(2000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Loop principal
while True:
    nivel = menu_nivel()
    pontos = 0
    for rodada in range(5):
        P, Q, R, expr, correto = gerar_expr(nivel)
        esperando = True
        while esperando:
            screen.fill(WHITE)
            desenhar_texto(f"Rodada {rodada+1}/5", 50, 30)
            desenhar_texto(f"P = {bool_str(P)}, Q = {bool_str(Q)}, R = {bool_str(R)}", 50, 100)
            desenhar_texto(f"Qual o valor lógico de:", 50, 160)
            desenhar_texto(expr, 50, 200, BIG)
            pygame.draw.rect(screen, GREEN, true_button)
            pygame.draw.rect(screen, RED, false_button)
            desenhar_texto("V", true_button.x + 60, true_button.y + 15, BIG)
            desenhar_texto("F", false_button.x + 60, false_button.y + 15, BIG)
            pygame.display.flip()
# Fecha o jogo e mostra a pontuação
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if true_button.collidepoint(event.pos):
                        if correto:
                            pontos += 1
                        esperando = False
                    elif false_button.collidepoint(event.pos):
                        if not correto:
                            pontos += 1
                        esperando = False
    fim_jogo(pontos)
