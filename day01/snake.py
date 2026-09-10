import random
import sys
from collections import deque

import pygame


GRID = 24
COLS, ROWS = 26, 20
BOARD_WIDTH, BOARD_HEIGHT = COLS * GRID, ROWS * GRID
PANEL_HEIGHT = 76
WIDTH, HEIGHT = BOARD_WIDTH, BOARD_HEIGHT + PANEL_HEIGHT
FPS = 12
MAX_SPEED = 24

BG = (12, 18, 31)
PANEL = (20, 29, 48)
GRID_COLOR = (29, 40, 61)
TEXT = (235, 242, 250)
MUTED = (145, 160, 181)
GREEN = (46, 204, 113)
HEAD_GREEN = (103, 230, 153)
GREEN_SHADOW = (24, 125, 73)
RED = (255, 91, 105)
RED_LIGHT = (255, 160, 167)
GOLD = (255, 204, 92)
OVERLAY = (5, 9, 17, 205)

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇 · 智能寻食")
clock = pygame.time.Clock()
font = pygame.font.SysFont("microsoftyahei,simhei,arial", 22)
small_font = pygame.font.SysFont("microsoftyahei,simhei,arial", 16)
large_font = pygame.font.SysFont("microsoftyahei,simhei,arial", 40, bold=True)


def random_food(snake):
    """在蛇身之外随机生成食物。"""
    occupied = set(snake)
    empty_cells = [
        (x, y)
        for x in range(COLS)
        for y in range(ROWS)
        if (x, y) not in occupied
    ]
    return random.choice(empty_cells) if empty_cells else None


def add_pos(position, direction):
    return position[0] + direction[0], position[1] + direction[1]


def inside_board(position):
    return 0 <= position[0] < COLS and 0 <= position[1] < ROWS


def legal_directions(snake):
    """返回下一步不会立刻碰撞的方向，尾巴会在本回合移走。"""
    blocked = set(snake[:-1])
    return [
        direction
        for direction in DIRECTIONS
        if inside_board(add_pos(snake[0], direction))
        and add_pos(snake[0], direction) not in blocked
    ]


def reachable_area(start, blocked):
    """估算一个位置周围仍可活动的格子数。"""
    queue = deque([start])
    visited = {start}
    while queue:
        current = queue.popleft()
        for direction in DIRECTIONS:
            neighbor = add_pos(current, direction)
            if (
                inside_board(neighbor)
                and neighbor not in blocked
                and neighbor not in visited
            ):
                visited.add(neighbor)
                queue.append(neighbor)
    return len(visited)


def auto_direction(snake, food, current_direction):
    """用 BFS 寻找食物；无路可走时选择活动空间最大的安全方向。"""
    if food is None:
        return current_direction

    head = snake[0]
    blocked = set(snake[:-1])
    blocked.discard(head)
    queue = deque([head])
    previous = {head: None}

    while queue:
        current = queue.popleft()
        if current == food:
            break
        for direction in DIRECTIONS:
            neighbor = add_pos(current, direction)
            if (
                inside_board(neighbor)
                and neighbor not in blocked
                and neighbor not in previous
            ):
                previous[neighbor] = current
                queue.append(neighbor)

    if food in previous:
        step = food
        while previous[step] != head:
            step = previous[step]
        candidate = step[0] - head[0], step[1] - head[1]
        if candidate in legal_directions(snake):
            return candidate

    choices = legal_directions(snake)
    if not choices:
        return current_direction

    def safety_score(direction):
        next_head = add_pos(head, direction)
        area = reachable_area(next_head, set(snake[:-1]) - {next_head})
        distance = abs(next_head[0] - food[0]) + abs(next_head[1] - food[1])
        return area * 100 - distance

    return max(choices, key=safety_score)


def cell_rect(position, padding=2):
    x, y = position
    return pygame.Rect(
        x * GRID + padding,
        PANEL_HEIGHT + y * GRID + padding,
        GRID - padding * 2,
        GRID - padding * 2,
    )


def draw_background():
    screen.fill(BG)
    pygame.draw.rect(screen, PANEL, (0, 0, WIDTH, PANEL_HEIGHT))
    pygame.draw.line(screen, GRID_COLOR, (0, PANEL_HEIGHT - 1), (WIDTH, PANEL_HEIGHT - 1), 2)
    for x in range(0, BOARD_WIDTH + 1, GRID):
        pygame.draw.line(screen, GRID_COLOR, (x, PANEL_HEIGHT), (x, HEIGHT), 1)
    for y in range(PANEL_HEIGHT, HEIGHT + 1, GRID):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)


def draw_food(food):
    if food is None:
        return
    rect = cell_rect(food, 3)
    center = rect.center
    pygame.draw.circle(screen, (88, 24, 37), (center[0] + 2, center[1] + 3), GRID // 2 - 3)
    pygame.draw.circle(screen, RED, center, GRID // 2 - 4)
    pygame.draw.circle(screen, RED_LIGHT, (center[0] - 4, center[1] - 4), 3)
    pygame.draw.line(screen, GREEN, (center[0], center[1] - 8), (center[0] + 4, center[1] - 12), 3)


def draw_snake(snake, direction):
    for index in range(len(snake) - 1, -1, -1):
        rect = cell_rect(snake[index], 2)
        color = HEAD_GREEN if index == 0 else GREEN
        pygame.draw.rect(screen, GREEN_SHADOW, rect.move(1, 2), border_radius=7)
        pygame.draw.rect(screen, color, rect, border_radius=7)

    head_rect = cell_rect(snake[0], 2)
    cx, cy = head_rect.center
    if direction[0]:
        eye_positions = [(cx + direction[0] * 5, cy - 5), (cx + direction[0] * 5, cy + 5)]
    else:
        eye_positions = [(cx - 5, cy + direction[1] * 5), (cx + 5, cy + direction[1] * 5)]
    for eye in eye_positions:
        pygame.draw.circle(screen, BG, eye, 2)


def draw_panel(score, speed, auto_mode):
    score_surface = font.render(f"得分  {score}", True, TEXT)
    screen.blit(score_surface, (18, 12))
    speed_surface = small_font.render(f"速度 {speed}", True, MUTED)
    screen.blit(speed_surface, (20, 43))

    mode_text = "G  自动寻食：开启" if auto_mode else "G  自动寻食：关闭"
    mode_color = GOLD if auto_mode else MUTED
    mode_surface = small_font.render(mode_text, True, mode_color)
    screen.blit(mode_surface, mode_surface.get_rect(midright=(WIDTH - 18, 25)))

    control_surface = small_font.render("方向键 / WASD 移动   ·   P 暂停", True, MUTED)
    screen.blit(control_surface, control_surface.get_rect(midright=(WIDTH - 18, 52)))


def draw_center_message(title, subtitle, title_color=TEXT):
    shade = pygame.Surface((WIDTH, BOARD_HEIGHT), pygame.SRCALPHA)
    shade.fill(OVERLAY)
    screen.blit(shade, (0, PANEL_HEIGHT))
    center_y = PANEL_HEIGHT + BOARD_HEIGHT // 2
    title_surface = large_font.render(title, True, title_color)
    subtitle_surface = font.render(subtitle, True, TEXT)
    screen.blit(title_surface, title_surface.get_rect(center=(WIDTH // 2, center_y - 28)))
    screen.blit(subtitle_surface, subtitle_surface.get_rect(center=(WIDTH // 2, center_y + 28)))


def main():
    while True:
        snake = [(13, 10), (12, 10), (11, 10)]
        direction = (1, 0)
        next_direction = direction
        food = random_food(snake)
        score = 0
        speed = FPS
        auto_mode = False
        started = False
        paused = False
        game_over = False
        won = False

        while True:
            restart = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type != pygame.KEYDOWN:
                    continue
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if not started or game_over:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        if game_over:
                            restart = True
                        else:
                            started = True
                    continue
                if event.key == pygame.K_g:
                    auto_mode = not auto_mode
                elif event.key == pygame.K_p:
                    paused = not paused
                elif not paused:
                    requested = None
                    if event.key in (pygame.K_UP, pygame.K_w):
                        requested = (0, -1)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        requested = (0, 1)
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        requested = (-1, 0)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        requested = (1, 0)
                    if requested and requested != (-direction[0], -direction[1]):
                        next_direction = requested
                        auto_mode = False

            if restart:
                break

            if started and not paused and not game_over:
                if auto_mode:
                    next_direction = auto_direction(snake, food, direction)
                direction = next_direction
                head = add_pos(snake[0], direction)
                growing = head == food
                collision_body = snake if growing else snake[:-1]

                if not inside_board(head) or head in collision_body:
                    game_over = True
                else:
                    snake.insert(0, head)
                    if growing:
                        score += 1
                        speed = min(FPS + score // 3, MAX_SPEED)
                        food = random_food(snake)
                        if food is None:
                            won = True
                            game_over = True
                    else:
                        snake.pop()

            draw_background()
            draw_food(food)
            draw_snake(snake, direction)
            draw_panel(score, speed, auto_mode)

            if not started:
                draw_center_message("贪吃蛇", "空格 / 回车开始 · G 开启自动寻食", HEAD_GREEN)
            elif paused:
                draw_center_message("已暂停", "按 P 继续游戏", GOLD)
            elif game_over:
                title = "全部吃完！" if won else "游戏结束"
                color = GOLD if won else RED
                draw_center_message(title, f"得分 {score} · 空格 / 回车重新开始", color)

            pygame.display.flip()
            clock.tick(speed if started and not paused and not game_over else 30)


if __name__ == "__main__":
    main()
