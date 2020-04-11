"""
 Pygame 模板程式
 
"""
# 匯入pygame模組
import pygame

# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

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
#載入圖片
player = pygame.image.load("pusheen.png")
x = y = 0
# -------- 主要的程式迴圈 -----------
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    # --- 程式的運算與邏輯

    # --- 繪圖的程式碼
    #       先將畫面塗滿底色(將原有畫面清掉)
    #       繪圖的程式要寫在這行後面，不然會被這行清掉

    #顯示圖片
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_w]:
        y -= 1
        
    screen.fill(BLACK)
    screen.blit(player, (x,y))
    # --- 更新畫面
    pygame.display.flip()

    # --- 每秒鐘60個frame
    clock.tick(60)

# 關閉式窗並離開程式
pygame.quit()

