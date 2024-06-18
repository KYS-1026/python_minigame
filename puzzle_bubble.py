import pygame # ���̺귯�� ����Ʈ

pygame.init() # ���̰��� �ʱ�ȭ

# 3. ���̰��ӿ� ���Ǵ� ���� ���� ����
WHITE = (255,255,255) # �� rgb �ڵ�  ��� 
size = [448,720] # ����Ʈ �������� x,y ��ǥ�� �Է�?? ũ�� 
screen = pygame.display.set_mode(size) # size ������ŭ ���÷��� ��ũ�� ũ�� ��ü 
pygame.display.set_caption("Puzzle Bubble")

done = False # ���� ���Ḧ Ȯ���� ���� 
clock = pygame.time.Clock() # FPS�� �����ϴ� ���� : ȭ���� �󸶳� ���ֱ׷��� ���̳� ! 

# 4. pygame ���� ���� 
def runGame():
    global done # ���� ���� ���� 
    while not done:
        clock.tick(60) # Clock Ŭ������ �ִ� �޼��� ���...-> 1�ʿ� 60�� ȭ�� ��� 
        screen.fill(WHITE) # fill �޼���� ���� �Ͼ������ ä�� 
        
        for event in pygame.event.get(): 
        # pygame.event.get() : ���� �ȿ��� �߻��ϴ� �̺�Ʈ�� ������, ����Ʈ ���·� ���� 
            if event.type == pygame.QUIT: # �̺�Ʈ�� 
                done = True
            
            # ����Ű �Է¿� ���� �̺�Ʈ ó��
            if event.type == pygame.KEYDOWN: # Ű���� ��ư�� �������� �߻� ! 
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
                    
        screen.blit(airplane, (x,y)) # airplane�� x,y ��ǥ�� ��ġ! 
        pygame.display.update() # ��ġ�� ����Ⱑ ���̵��� ��ũ�� ������Ʈ 
        
runGame()
pygame.quit()