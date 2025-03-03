from __future__ import annotations

from functools import cache

from pygame import Rect, Surface

HitMaskType = list[list[bool]]


def clamp(n: float, min_: float, max_: float) -> float:
    """Clamps a number between two values"""
    return max(min(max_, n), min_)


@cache
def get_hit_mask(image: Surface) -> HitMaskType:
    """returns a hit mask using an image's alpha."""
    return list(
        (
            list((bool(image.get_at((x, y))[3]) for y in range(image.get_height())))
            for x in range(image.get_width())
        )
    )


def pixel_collision(
    rect1: Rect, rect2: Rect, hitmask1: HitMaskType, hitmask2: HitMaskType
):
    """Checks if two objects collide and not just their rects"""
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1 + x][y1 + y] and hitmask2[x2 + x][y2 + y]:
                return True
    return False
