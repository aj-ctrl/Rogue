from ast import walk
from math import floor
from typing import Tuple

import numpy as np

# Tile graphics structured type compatible with Console.tile_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),   # Unicode codepoint for "char"
        ("fg", "3B"),       # 3 unsigned bytes for RGB colors.
        ("bg", "3B"),       # ^ for foreground and background
    ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),      # True if tile can be walked on
        ("transparent", np.bool),   # True if this tile doesn't block fov
        ("dark", graphic_dt)        # graphics for when this tile is not in fov
    ]
)

def new_tile(
    *, #enforce the use of keywords, so that paramater doesnt matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helperr function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255,255,255), (50,50,150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255,255,255), (0,0,100)),
)