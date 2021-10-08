pygame.display.update()
copy = screen.copy()
x = 0
y = 0

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_F1):
			while (event.type == pygame.KEYDOWN) and (event.key != pygame.K_f):
				pygame.display.update()
				screen = pygame.display.set_mode((Width, Height))
				screen.blit(copy, (0, 0))
				keys = pygame.key.get_pressed()
				if keys[pygame.K_s]:
					y += 10
				if keys[pygame.K_w]:
					y -= 10
				if keys[pygame.K_a]:
					x -= 10
				if keys[pygame.K_d]:
					x += 10
				Draw_UFO(screen, x, y, 0.6)