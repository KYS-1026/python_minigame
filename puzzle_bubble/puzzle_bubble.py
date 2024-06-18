import os
import pygame
from pygame.sprite import Group # 라이브러리 임포트

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

# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center = position)
    
# 발사대 클래스 생성
class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        self.image = image
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_img = image
        self.position = position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def rotate(self, angle):
        self.angle += angle
        if self.angle > 170:
            self.angle = 170
        elif self.angle <10:
            self.angle = 10
        
        self.image = pygame.transform.rotozoom(self.original_img, self.angle, 1)
        self.rect = self.image.get_rect(center= self.position)
        
# 맵 만들기
def setup():
    global map
    map = [
        list("RRYYBBGG"),
        list("RRYYBBG/"),
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
    ]
    
    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue
            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_img(col)
            bubble_group.add(Bubble(image, col, position))

# 버블 위치 정보 얻어오기   
def get_bubble_position(row_idx, col_idx):
    x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1:
        x += CELL_SIZE // 2
    return x,y

# 버블 이미지 얻어오기 
def get_bubble_img(color):
    if color == "R":
        return bubble_imgs[0]
    elif color == "Y":
        return bubble_imgs[1]
    elif color == "B":
        return bubble_imgs[2]
    elif color == "G":
        return bubble_imgs[3]
    elif color == "P":
        return bubble_imgs[4]
    else:
        return bubble_imgs[-1]
    
# 이미지 불러오기 
bubble_imgs = [
    pygame.image.load(os.path.join(path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(path, "black.png")).convert_alpha()
]

pointer_image = pygame.image.load(os.path.join(path, "pointer.png"))
pointer = Pointer(pointer_image, (size[0] //2, 624), 90)

# 게임 변수 
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62

to_angle = 0 # 각도
angle_speed = 1.5 # 1.5도씩 움직이게 됨 

map = [] # 맵
bubble_group = pygame.sprite.Group()
setup()

# pygame 무한 루프 
def runGame():
    global done,to_angle # 전역 변수 선언 
    while not done:
        clock.tick(60) # Clock 클래스에 있는 메서드 사용...-> 1초에 60번 화면 출력 
        screen.fill(WHITE) # fill 메서드로 색을 하얀색으로 채움 
        
        for event in pygame.event.get(): 
        # pygame.event.get() : 게임 안에서 발생하는 이벤트를 가져옴, 리스트 형태로 리턴 
            if event.type == pygame.QUIT: # 이벤트의 
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_angle += angle_speed
                elif event.key == pygame.K_RIGHT:
                    to_angle -= angle_speed
            
            # 키보드에서 손을 뗐을 때 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_angle = 0
            
        screen.blit(background, (0,0)) # 배경 배치! 
        bubble_group.draw(screen)
        pointer.rotate(to_angle)
        pointer.draw(screen)
        pygame.display.update() # 배치한 비행기가 보이도록 스크린 업데이트 
        
runGame()
pygame.quit()