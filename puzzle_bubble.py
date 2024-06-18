import os
import pygame # 라이브러리 임포트

pygame.init() # 파이게임 초기화

# 전역 변수 선언
WHITE = (255,255,255) # 색 rgb 코드  배경 
size = [448,720] # 리스트 형식으로 x,y 좌표를 입력?? 크기 
screen = pygame.display.set_mode(size) # size 변수만큼 디스플레이 스크린 크기 객체 
pygame.display.set_caption("Puzzle Bubble")

done = False # 게임 종료를 확인할 변수 
clock = pygame.time.Clock() # FPS을 설정하는 변수 : 화면을 얼마나 자주그려줄 것이냐 ! 

# 배경이미지 불러오기
path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(path, "pngtree_bg_img.jpg"))

# 버블 이미지 불러오기 
bubble_imgs = [
    pygame.image.load(os.path.join(path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "black.png")).convert_alpha()
]

# pygame 무한 루프 
def runGame():
    global done # 전역 변수 선언 
    while not done:
        clock.tick(60) # Clock 클래스에 있는 메서드 사용...-> 1초에 60번 화면 출력 
        screen.fill(WHITE) # fill 메서드로 색을 하얀색으로 채움 
        
        for event in pygame.event.get(): 
        # pygame.event.get() : 게임 안에서 발생하는 이벤트를 가져옴, 리스트 형태로 리턴 
            if event.type == pygame.QUIT: # 이벤트의 
                done = True
            
            # 방향키 입력에 대한 이벤트 처리
            '''
            if event.type == pygame.KEYDOWN: # 키보드 버튼을 눌렀을때 발생 ! 
                if event.key == pygame.K_UP:
                    if y > 0:
                        y -= 10
                elif event.key == pygame.K_DOWN:
                    if y < size[0]-a_height :
                        y += 10
                elif event.key == pygame.K_LEFT:
                    if x > 0:
                        x -= 10 
                elif event.key == pygame.K_RIGHT:
                    if x < size[0]-a_width:
                        x += 10 
            '''
            
                    
        screen.blit(background, (0,0)) # 배경 배치! 
        pygame.display.update() # 배치한 비행기가 보이도록 스크린 업데이트 
        
runGame()
pygame.quit()