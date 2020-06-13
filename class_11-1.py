"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame
from snake import Snake, Food
import random
import time
# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()

snake = Snake(5, size)
g = pygame.sprite.Group()

def addFood():
    x = random.randrange(size[0])
    y = random.randrange(size[1])
    x -= x % 20
    y -= y % 20
    food = Food(WHITE, x, y)
    g.add(food)
for _ in range(10):
    addFood()

start = False

font = pygame.font.Font(None, 50)
text = font.render("PLEASE PRESS ANY KEY", True, (200, 230, 255))

# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯
    pressed = pygame.key.get_pressed() 
    
    if pressed.count(1) == 0 and not start: #1 有被按下
        screen.blit(text, (150, 230))
        pygame.display.flip()
        continue
    
    else:
        start = True #不再進入這個迴圈
    
    snake.move(pressed) 
    
    if snake.isOutOfBound() or snake.collideSelf():
        done = True
        font = pygame.font.Font(None, 100)
        text = font.render("GAME OVER", True, (255, 50, 50))
        screen.blit(text, (150, 230))
        pygame.display.flip()
        time.sleep(2)
        
        
    if len(g) < 10:
        addFood()
    
    snake.collideSelf()
    snake.eat(g)

    #eatFood = pygame.sprite.groupcollide(snake.group, g, False, True)
    #if eatFood:
    #    snake.append(len(eatFood.values()))
    
    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉
    screen.fill(BLACK)

    snake.group.draw(screen)
    g.draw(screen)
#    sprites.draw(screen)
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘5個frame
    clock.tick(5)

# 關閉式窗並離開程式
pygame.quit()
exit()


