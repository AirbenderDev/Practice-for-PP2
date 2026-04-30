import pygame
from collections import deque


def pencil(surface, prev, curr, color, size):
    if prev:
        pygame.draw.line(surface, color, prev, curr, size)


def draw_line(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_rect(surface, start, end, color, size):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    pygame.draw.rect(surface, color, (x, y, w, h), size)


def draw_circle(surface, start, end, color, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    r = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5 // 2)
    if r > 0:
        pygame.draw.circle(surface, color, (cx, cy), r, size)


def draw_square(surface, start, end, color, size):
    side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
    x = start[0] if end[0] >= start[0] else start[0] - side
    y = start[1] if end[1] >= start[1] else start[1] - side
    pygame.draw.rect(surface, color, (x, y, side, side), size)


def draw_right_triangle(surface, start, end, color, size):
    p1 = start
    p2 = (start[0], end[1])
    p3 = end
    pygame.draw.polygon(surface, color, [p1, p2, p3], size)


def draw_eq_triangle(surface, start, end, color, size):
    import math
    base = abs(end[0] - start[0])
    h = int(base * math.sqrt(3) / 2)
    x = min(start[0], end[0])
    y = start[1]
    p1 = (x, y + h)
    p2 = (x + base, y + h)
    p3 = (x + base // 2, y)
    pygame.draw.polygon(surface, color, [p1, p2, p3], size)


def draw_rhombus(surface, start, end, color, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    p1 = (cx, start[1])
    p2 = (end[0], cy)
    p3 = (cx, end[1])
    p4 = (start[0], cy)
    pygame.draw.polygon(surface, color, [p1, p2, p3, p4], size)


def flood_fill(surface, pos, new_color):
    x, y = pos
    w, h = surface.get_size()
    old_color = surface.get_at((x, y))[:3]
    new_color = new_color[:3]
    if old_color == new_color:
        return
    q = deque()
    q.append((x, y))
    visited = set()
    visited.add((x, y))
    while q:
        cx, cy = q.popleft()
        if surface.get_at((cx, cy))[:3] != old_color:
            continue
        surface.set_at((cx, cy), new_color)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
