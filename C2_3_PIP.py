import pygame

# 1. Configuración inicial
run = True
width = 400
height = 100

pygame.init() # Inicializa todos los módulos de pygame
screen = pygame.display.set_mode((width, height)) # Crea la ventana
font = pygame.font.SysFont(None, 48) # Define la fuente (None = predeterminada)

# 2. Creación del texto (renderizado)
# "Texto", Antialias (suavizado), Color RGB (Blanco)
text = font.render("Welcome to pygame", True, (255, 255, 255))

# 3. Dibujado (Blit) y Actualización
# Calcula el centro para poner el texto
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip() # Actualiza la pantalla para mostrar lo dibujado

# 4. Ciclo de vida (Event Loop)
while run:
    for event in pygame.event.get():
        # El programa se cierra si: cierras la ventana, haces clic o sueltas una tecla
        if event.type == pygame.QUIT \
        or event.type == pygame.MOUSEBUTTONUP \
        or event.type == pygame.KEYUP:
            run = False

pygame.quit() # Cierra pygame correctamente al salir del ciclo