import pygame
import sys
import subprocess
import random
from make_txt import make
from make_txt import seed_value


pygame.init()

# 화면
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move with Arrows")

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#폰트
font = pygame.font.SysFont(None, 50)
# 타이밍용
clock = pygame.time.Clock()

pygame.mixer.music.load("BGM/test_bgm.mp3")  # 백그라운드 뮤직 파일 로드
pygame.mixer.music.play(-1)  # 백그라운드 뮤직 재생 (반복)

# 소리
pygame.mixer.init()
sound = pygame.mixer.Sound("Sound_effect/make_txt_sound.wav")  # 사운드 파일 로드

player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = (SCREEN_HEIGHT - player_height) // 2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.collide_triggered = False
        self.collide_triggered_b = False
        self.collide_triggered_e = False

    def update(self, dx, dy):
        # 새로운 위치 계산
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # 새로운 위치가 화면을 벗어나지 않는지 확인 
        if 0 <= new_x <= SCREEN_WIDTH - player_width:
            self.rect.x = new_x
        if 0 <= new_y <= SCREEN_HEIGHT - player_height:
            self.rect.y = new_y

        # 빨간 네모와 충돌하는지 확인
        if self.rect.colliderect(red_square.rect) and not self.collide_triggered and keys[pygame.K_z]:
            self.collide_triggered = True
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': 'make_txt 실행함 ㅅㄱ'}))
            make()  # make 함수 호출
            sound.play()  # 사운드 재생
        
        if self.rect.colliderect(red_square.rect) and self.collide_triggered and not keys[pygame.K_z]:
            self.collide_triggered = False
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': '왜?'}))

        if self.rect.colliderect(blue_square.rect) and keys[pygame.K_z] and not self.collide_triggered_b:
            self.collide_triggered_b = True
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': '비번입력해'}))

        if self.rect.colliderect(blue_square.rect) and self.collide_triggered_b and not keys[pygame.K_z]:
            self.collide_triggered_b = False
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': '멍청이'}))
        
        if self.rect.colliderect(exit_square.rect) and keys[pygame.K_z] and not self.collide_triggered_e:
            self.collide_triggered_e = True
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': '입력함?'}))
        
        if self.rect.colliderect(exit_square.rect) and self.collide_triggered_e and not keys[pygame.K_z]:
            self.collide_triggered_e = False
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'message': '븅신'}))
            
            

red_square = pygame.sprite.Sprite()
red_square.image = pygame.Surface((50, 50))
red_square.image.fill((255, 0, 0))  # 빨간 네모 생성
red_square.rect = red_square.image.get_rect()
red_square.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)  # 임의의 위치

blue_square = pygame.sprite.Sprite()
blue_square.image = pygame.Surface((50, 50))
blue_square.image.fill((0, 0, 255))  # 파롼 네모 생성
blue_square.rect = blue_square.image.get_rect()
blue_square.rect.center = (SCREEN_WIDTH // 1.3 , SCREEN_HEIGHT // 1.3)  # 임의의 위치

exit_square = pygame.sprite.Sprite()
exit_square.image = pygame.Surface((50, 50))
exit_square.image.fill((0, 255, 0))  # 초록 네모 생성
exit_square.rect = blue_square.image.get_rect()
exit_square.rect.center = (SCREEN_WIDTH // 1.05 , SCREEN_HEIGHT // 1.3)  # 임의의 위치

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            print(event.message)  # 이벤트 메시지 출력

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    player.update(dx, dy)
    screen.fill(BLACK)
    screen.blit(player.image, player.rect)
    screen.blit(red_square.image, red_square.rect)
    screen.blit(blue_square.image, blue_square.rect)
    screen.blit(exit_square.image, exit_square.rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()