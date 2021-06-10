# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------


import pygame		#1
import time		#4

pygame.init()		#2
gameDisplay = pygame.display.set_mode((800,600))	#3
pygame.display.set_caption("Name of the Game")		#3
clock = pygame.time.Clock() 	#4
crashed = False	#5
while not crashed:	#6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
            
    pygame.display.update()
    clock.tick(60)

pygame.quit()		#7
quit()
