


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#GRUPO 
# Pedro Fonseca
# Sophia Oelke Verdi
# Daniel Langner
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

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
pygame.display.set_caption("Desafio da Tabela Verdade")

# Fontes usadas
FONT = pygame.font.SysFont('Arial', 24)
BIG = pygame.font.SysFont('Arial', 32)

# Botões
true_button = pygame.Rect(150, 450, 150, 60)
false_button = pygame.Rect(500, 450, 150, 60)

# Responsável por transformar o True em V e False em F
def bool_str(b):
    return "V" if b else "F"

# Função para implicação (P → Q equivale a ¬P ∨ Q)
def implicacao(p, q):
    return not p or q

# Função para bicondicional (P ↔ Q equivale a (P → Q) ∧ (Q → P))
def bicondicional(p, q):
    return (not p or q) and (not q or p)

# Vai montar a proposição que vai ser analisada
def avaliar_expr(P, Q, R, expr):
    contexto = {
        "P": P, 
        "Q": Q, 
        "R": R,
        "implicacao": implicacao,
        "bicondicional": bicondicional
    }
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
    else:  # Difícil - incluindo implicação e bicondicional
        opcoes = [
            # Expressões com conectivos básicos
            "(P and Q) or R",
            "(P or Q) and R", 
            "not (P and Q)",
            "not (P or Q)",
            "(not P and Q) or R",
            "(P and not Q) or R",
            # Expressões com implicação
            "implicacao(P, Q)",
            "implicacao(Q, P)",
            "implicacao(P, R)",
            "implicacao(not P, Q)",
            "implicacao(P and Q, R)",
            "implicacao(P, Q and R)",
            # Expressões com bicondicional
            "bicondicional(P, Q)",
            "bicondicional(P, R)",
            "bicondicional(Q, R)",
            "bicondicional(P and Q, R)",
            "bicondicional(P, Q or R)",
            # Combinações mais complexas
            "implicacao(P, Q) and R",
            "bicondicional(P, Q) or R",
            "implicacao(P, bicondicional(Q, R))",
            "bicondicional(implicacao(P, Q), R)"
        ]
        expr = random.choice(opcoes)
    
    resultado = avaliar_expr(P, Q, R, expr)
    
    # Formatação visual das expressões - CORRIGIDA PARA TODOS OS NÍVEIS
    visivel = expr
    
    # Tratar implicação primeiro (apenas no nível difícil)
    if "implicacao(" in expr:
        if expr.startswith("implicacao("):
            # Extrair argumentos da implicação
            temp = expr[11:-1]  # Remove "implicacao(" e ")"
            if ", " in temp:
                args = temp.split(", ", 1)
                arg1 = args[0]
                arg2 = args[1]
                # Aplicar formatação nos argumentos
                for i, arg in enumerate([arg1, arg2]):
                    arg = arg.replace("and", " ^ ").replace("or", " v ")
                    arg = arg.replace("not ", "~")
                    if i == 0:
                        arg1 = arg
                    else:
                        arg2 = arg
                visivel = f"({arg1}) -> ({arg2})"
        else:
            # Substituições específicas para casos complexos
            visivel = visivel.replace("implicacao(P, Q)", "(P -> Q)")
            visivel = visivel.replace("implicacao(Q, P)", "(Q -> P)")
            visivel = visivel.replace("implicacao(P, R)", "(P -> R)")
            visivel = visivel.replace("implicacao(not P, Q)", "(~P -> Q)")
            visivel = visivel.replace("implicacao(P and Q, R)", "((P ^ Q) -> R)")
            visivel = visivel.replace("implicacao(P, Q and R)", "(P -> (Q ^ R))")
            visivel = visivel.replace("implicacao(P, bicondicional(Q, R))", "(P -> (Q <-> R))")
    
    # Tratar bicondicional depois (apenas no nível difícil)
    if "bicondicional(" in expr:
        if expr.startswith("bicondicional(") and "implicacao(" not in expr:
            # Extrair argumentos do bicondicional
            temp = expr[13:-1]  # Remove "bicondicional(" e ")"
            if ", " in temp:
                args = temp.split(", ", 1)
                arg1 = args[0]
                arg2 = args[1]
                # Aplicar formatação nos argumentos
                for i, arg in enumerate([arg1, arg2]):
                    arg = arg.replace("and", " ^ ").replace("or", " v ")
                    arg = arg.replace("not ", "~")
                    if i == 0:
                        arg1 = arg
                    else:
                        arg2 = arg
                visivel = f"({arg1}) <-> ({arg2})"
        else:
            # Substituições específicas para casos complexos
            visivel = visivel.replace("bicondicional(P, Q)", "(P <-> Q)")
            visivel = visivel.replace("bicondicional(P, R)", "(P <-> R)")
            visivel = visivel.replace("bicondicional(Q, R)", "(Q <-> R)")
            visivel = visivel.replace("bicondicional(P and Q, R)", "((P ^ Q) <-> R)")
            visivel = visivel.replace("bicondicional(P, Q or R)", "(P <-> (Q v R))")
            visivel = visivel.replace("bicondicional(implicacao(P, Q), R)", "((P -> Q) <-> R)")
    
    # SEMPRE fazer substituições finais de conectivos básicos (para todos os níveis)
    # Usando caracteres mais compatíveis com Pygame
    visivel = visivel.replace("and", " ^ ")  # ou use " & " para AND
    visivel = visivel.replace("or", " v ")   # ou use " | " para OR
    visivel = visivel.replace("not ", "~")   # ou use " ! " para NOT
    visivel = visivel.replace("not(", "~(")
    
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
        
        # Adiciona informação sobre o nível difícil
        desenhar_texto("Nivel Dificil inclui:", 400, 200, FONT, GRAY)
        desenhar_texto("• Implicacao (->)", 400, 230, FONT, GRAY)
        desenhar_texto("• Bicondicional (<->)", 400, 260, FONT, GRAY)
        desenhar_texto("• Expressoes complexas", 400, 290, FONT, GRAY)
        
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
            
            # Adiciona legenda para símbolos no modo difícil
            if nivel == "Difícil":
                desenhar_texto("Legenda: ^ = E, v = OU, ~ = NAO", 50, 250, pygame.font.SysFont('Arial', 18), GRAY)
                desenhar_texto("-> = IMPLICACAO, <-> = BICONDICIONAL", 50, 275, pygame.font.SysFont('Arial', 18), GRAY)
            
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