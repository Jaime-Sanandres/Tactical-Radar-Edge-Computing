import serial
import time
import math
import pygame
import sys

# 1. SERIAL PORT CONFIGURATION
try:
    arduino_port = serial.Serial('COM3', 9600)
    time.sleep(2)
except:
    print("Error: Could not open the serial port. Check your connection or close the Serial Monitor.")
    sys.exit()

# 2. PYGAME WINDOW CONFIGURATION
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tactical Radar System - Ultra-Short Range (20cm)")

# Colors
BLACK = (0, 0, 0)
RADAR_GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT - 50

# --- THE TRAIL TRICK (MOTION BLUR) ---
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill(BLACK)
fade_surface.set_alpha(15) # Opacity for the sweep trail

clock = pygame.time.Clock()
current_angle = 0 

screen.fill(BLACK)

print("Tactical radar active. Video mode: Extreme sensitivity set to 20 cm.")

# 3. MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            arduino_port.close()
            pygame.quit()
            sys.exit()

    # A. APPLY FADE
    screen.blit(fade_surface, (0, 0))

    # B. DRAW THE STATIC GRID (New ultra-short scale)
    # Each circle represents exactly 5 real physical cm (100 pixels)
    pygame.draw.circle(screen, DARK_GREEN, (CENTER_X, CENTER_Y), 100, 1) # 5 cm mark
    pygame.draw.circle(screen, DARK_GREEN, (CENTER_X, CENTER_Y), 200, 1) # 10 cm mark
    pygame.draw.circle(screen, DARK_GREEN, (CENTER_X, CENTER_Y), 300, 1) # 15 cm mark
    pygame.draw.circle(screen, DARK_GREEN, (CENTER_X, CENTER_Y), 400, 1) # 20 cm mark
    # Horizontal baseline
    pygame.draw.line(screen, DARK_GREEN, (CENTER_X - 400, CENTER_Y), (CENTER_X + 400, CENTER_Y), 1)

    # C. READ DATA AND DRAW RED DOTS
    if arduino_port.in_waiting > 0:
        line = arduino_port.readline().decode('utf-8').strip()
        try:
            parts = line.split(',')
            if len(parts) == 2:
                current_angle = float(parts[0]) 
                distance = float(parts[1])
                
                # Safety filter: Only read objects between 2 and 20 cm
                if 2 <= distance <= 20:
                    angle_rad = math.radians(current_angle)
                    
                    # Multiply by 20 (Extreme scale factor)
                    x = CENTER_X + int(distance * 20 * math.cos(angle_rad))
                    y = CENTER_Y - int(distance * 20 * math.sin(angle_rad))
                    
                    # Draw detected object (Red dot)
                    pygame.draw.circle(screen, RED, (x, y), 6)
        except ValueError:
            pass

    # D. DRAW THE SWEEP LINE (The radar "pointer")
    angle_rad = math.radians(current_angle)
    line_x = CENTER_X + int(400 * math.cos(angle_rad))
    line_y = CENTER_Y - int(400 * math.sin(angle_rad))
    pygame.draw.line(screen, RADAR_GREEN, (CENTER_X, CENTER_Y), (line_x, line_y), 3)

    # Update screen
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(60)
