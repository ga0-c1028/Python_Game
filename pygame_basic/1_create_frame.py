import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 만들기")

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("D:/2022/others/python_game/pygame_basic/background.png")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("D:/2022/others/python_game/pygame_basic/character.png")

character_size = character.get_rect().size #이미지 크기 구하기
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#이벤트 루프
running = True 
while running :
    dt = clock.tick(50) # 게임화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps()))

    #캐릭터가 100만큼 이동해야함
    #10 fps : 1초동안 10번 동작 => 1번에 10만큼 이동해야 100
    #20 fps : 1초동안 20번 동작 => 1번에 5만큼 이동해야 100

    for event in pygame.event.get() : # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는가
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed
            elif event.key == pygame.K_UP :
                to_y -= character_speed
            else :
                to_y += character_speed

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width :
        character_x_pos = screen_width-character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height :
        character_y_pos = screen_height-character_height

    #screen.fill((0,0,255)) #RGB로 화면 색깔 주기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임 화면 다시 그리기


#pygame 종료
pygame.quit()