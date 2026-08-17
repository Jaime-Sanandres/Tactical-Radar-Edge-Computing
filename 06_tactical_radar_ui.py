import serial
import time
import math
import pygame
import sys

# 1. SERIAL PORT CONFIGURATION
try:
    puerto_arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
except:
    print("Error: Could not open the serial port. Check your connection or close the Serial Monitor.")
    sys.exit()

# 2. PYGAME WINDOW CONFIGURATION
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tactical Radar System - Ultra-Short Range (20cm)")

# Colors
NEGRO = (0, 0, 0)
VERDE_RADAR = (0, 255, 0)
VERDE_OSCURO = (0, 100, 0)
ROJO = (255, 0, 0)

CENTRO_X = ANCHO // 2
CENTRO_Y = ALTO - 50

# --- THE TRAIL TRICK (MOTION BLUR) ---
superficie_fade = pygame.Surface((ANCHO, ALTO))
superficie_fade.fill(NEGRO)
superficie_fade.set_alpha(15) # Opacity for the sweep trail

reloj = pygame.time.Clock()
angulo_actual = 0 

pantalla.fill(NEGRO)

print("Tactical radar active. Video mode: Extreme sensitivity set to 20 cm.")

# 3. MAIN LOOP
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            puerto_arduino.close()
            pygame.quit()
            sys.exit()

    # A. APPLY FADE
    pantalla.blit(superficie_fade, (0, 0))

    # B. DRAW THE STATIC GRID (New ultra-short scale)
    # Each circle represents exactly 5 real physical cm (100 pixels)
    pygame.draw.circle(pantalla, VERDE_OSCURO, (CENTRO_X, CENTRO_Y), 100, 1) # 5 cm mark
    pygame.draw.circle(pantalla, VERDE_OSCURO, (CENTRO_X, CENTRO_Y), 200, 1) # 10 cm mark
    pygame.draw.circle(pantalla, VERDE_OSCURO, (CENTRO_X, CENTRO_Y), 300, 1) # 15 cm mark
    pygame.draw.circle(pantalla, VERDE_OSCURO, (CENTRO_X, CENTRO_Y), 400, 1) # 20 cm mark
    # Horizontal baseline
    pygame.draw.line(pantalla, VERDE_OSCURO, (CENTRO_X - 400, CENTRO_Y), (CENTRO_X + 400, CENTRO_Y), 1)

    # C. READ DATA AND DRAW RED DOTS
    if puerto_arduino.in_waiting > 0:
        linea = puerto_arduino.readline().decode('utf-8').strip()
        try:
            partes = linea.split(',')
            if len(partes) == 2:
                angulo_actual = float(partes[0]) 
                distancia = float(partes[1])
                
                # Safety filter: Only read objects between 2 and 20 cm
                if 2 <= distancia <= 20:
                    angulo_rad = math.radians(angulo_actual)
                    
                    # Multiply by 20 (Extreme scale factor)
                    x = CENTRO_X + int(distancia * 20 * math.cos(angulo_rad))
                    y = CENTRO_Y - int(distancia * 20 * math.sin(angulo_rad))
                    
                    # Draw detected object (Red dot)
                    pygame.draw.circle(pantalla, ROJO, (x, y), 6)
        except ValueError:
            pass

    # D. DRAW THE SWEEP LINE (The radar "pointer")
    angulo_rad = math.radians(angulo_actual)
    linea_x = CENTRO_X + int(400 * math.cos(angulo_rad))
    linea_y = CENTRO_Y - int(400 * math.sin(angulo_rad))
    pygame.draw.line(pantalla, VERDE_RADAR, (CENTRO_X, CENTRO_Y), (linea_x, linea_y), 3)

    # Update screen
    pygame.display.flip()
    
    # Limit to 60 frames per second
    reloj.tick(60)
