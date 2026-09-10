
import pygame
import random
from collections import deque

# ---------- 基本设置 ----------
CELL = 25
COLS, ROWS = 24, 18          # 24x18 的网格
TOP_BAR = 32                 # 顶部信息栏高度
WIDTH  = COLS * CELL
HEIGHT = TOP_BAR + ROWS * CELL

BLACK    = (12, 12, 12)
WHITE    = (240, 240, 240)
GREEN    = (0, 180, 0)
DARK_GREEN = (0, 120, 0)
RED      = (230, 50, 50)
YELLOW   = (255, 215, 0)
GRAY     = (140, 140, 140)

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
KEY_MAP = {
    pygame.K_UP: (0, -1),   pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),  pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0), pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0), pygame.K_d: (1, 0),
}


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake - G: auto hunt")
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.Font(None, 48)
        self.font = pygame.font.Font(None, 22)
        self.reset()

    def reset(self):
        cx, cy = COLS // 2, ROWS // 2
        self.snake = [(cx + 1, cy), (cx, cy), (cx - 1, cy)]  # snake[0] 是头
        self.direction = (1, 0)
        self.buffer = []       # 方向缓冲队列
        self.score = 0
        self.auto = False
        self.paused = False
        self.game_over = False
        self.food = self.spawn_food()

    def spawn_food(self):
        empty = [(x, y) for x in range(COLS) for y in range(ROWS)
                 if (x, y) not in self.snake]
        return random.choice(empty) if empty else None

    # ---------- 自动寻食：BFS 找最短安全路径 ----------
    def bfs_first_step(self):
        """从蛇头到食物的第一步方向；找不到路返回 None"""
        head, food = self.snake[0], self.food
        if food is None or head == food:
            return None
        body = set(self.snake)          # 整个身体都是障碍（保守但安全）
        visited = {head}
        parent = {head: None}
        queue = deque([head])
        found = False
        while queue and not found:
            cur = queue.popleft()
            for d in DIRECTIONS:
                nxt = (cur[0] + d[0], cur[1] + d[1])
                if (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS
                        and nxt not in body and nxt not in visited):
                    visited.add(nxt)
                    parent[nxt] = cur
                    if nxt == food:
                        found = True
                        break
                    queue.append(nxt)
        if not found:
            return None
        step = food                     # 从食物往回走到蛇头的下一格
        while parent[step] != head:
            step = parent[step]
        return step[0] - head[0], step[1] - head[1]

    def is_safe(self, direction):
        head = self.snake[0]
        nxt = (head[0] + direction[0], head[1] + direction[1])
        # 不吃食物时，尾巴会同时移走，可以进入尾巴当前所在的格子。
        body = self.snake if nxt == self.food else self.snake[:-1]
        return (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS
                and nxt not in body)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_r:
            self.reset()
        elif event.key == pygame.K_SPACE:
            self.paused = not self.paused
        elif event.key == pygame.K_g:
            self.auto = not self.auto
            self.buffer.clear()
        elif (event.key in KEY_MAP and not self.auto
              and not self.paused and not self.game_over):
            direction = KEY_MAP[event.key]
            previous = self.buffer[-1] if self.buffer else self.direction
            if (direction != previous
                    and direction != (-previous[0], -previous[1])
                    and len(self.buffer) < 2):
                self.buffer.append(direction)

    def update(self):
        if self.paused or self.game_over:
            return
        if self.auto:
            direction = self.bfs_first_step()
            if direction is None:
                # 没有通往食物的路时，优先保持方向，再尝试其他安全方向。
                direction = next((d for d in (self.direction,) + DIRECTIONS
                                  if self.is_safe(d)), None)
            if direction is None:
                self.game_over = True
                return
            self.direction = direction
        elif self.buffer:
            self.direction = self.buffer.pop(0)

        if not self.is_safe(self.direction):
            self.game_over = True
            return
        head = self.snake[0]
        nxt = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.snake.insert(0, nxt)
        if nxt == self.food:
            self.score += 1
            self.food = self.spawn_food()
            if self.food is None:
                self.game_over = True
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)
        status = 'Score: {}  Auto: {}  G: auto  Space: pause  R: restart'.format(
            self.score, 'ON' if self.auto else 'OFF')
        self.screen.blit(self.font.render(status, True, WHITE), (8, 8))
        pygame.draw.line(self.screen, GRAY, (0, TOP_BAR - 1),
                         (WIDTH, TOP_BAR - 1))
        for index, (x, y) in enumerate(self.snake):
            rect = pygame.Rect(x * CELL + 1, TOP_BAR + y * CELL + 1,
                               CELL - 2, CELL - 2)
            pygame.draw.rect(self.screen, GREEN if index == 0 else DARK_GREEN, rect)
        if self.food is not None:
            x, y = self.food
            pygame.draw.circle(self.screen, RED,
                               (x * CELL + CELL // 2,
                                TOP_BAR + y * CELL + CELL // 2), CELL // 2 - 2)
        if self.game_over or self.paused:
            message = 'Paused'
            if self.game_over:
                message = 'You win! R: restart' if self.food is None else 'Game over! R: restart'
            label = self.font_big.render(message, True, YELLOW)
            rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            pygame.draw.rect(self.screen, BLACK, rect.inflate(16, 16))
            self.screen.blit(label, rect)
        pygame.display.flip()

    def run(self):
        running = True
        elapsed = 0
        try:
            while running:
                elapsed += self.clock.tick(60)
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT
                            or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                        running = False
                    else:
                        self.handle_event(event)
                if not running:
                    break
                if elapsed >= 120:
                    self.update()
                    elapsed = 0
                self.draw()
        finally:
            pygame.quit()


if __name__ == '__main__':
    SnakeGame().run()
