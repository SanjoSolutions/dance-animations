"""Author one House candidate in a fresh Blender 5.2 process."""
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]
for directory in (ROOT / 'scripts', Path(__file__).resolve().parent):
    sys.path.insert(0, str(directory))
import dance_tools
from author import HouseAuthor
from floor import FloorAuthor
from transitions import TransitionAuthor
from turns import HeadingAuthor, TurnAuthor
from foot_accents import FootAccentAuthor
from repertoire import CATALOG


def main():
    name = sys.argv[sys.argv.index('--') + 1]
    actor, move = name.removeprefix('house_').split('_', 1)
    role = {'man': 'player', 'woman': 'partner'}[actor]
    phrase, module = next((phrase, module) for phrase, module in CATALOG if phrase.name == move)
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / 'main.blend'))
    dance_tools.register()
    author_class = {'author': HouseAuthor, 'floor': FloorAuthor, 'transitions': TransitionAuthor}[module]
    if move == 'half_turn_return':
        author_class = TurnAuthor
    elif move in ('quarter_turn_left', 'quarter_turn_right'):
        author_class = HeadingAuthor
    elif actor == 'woman' and move in ('heel_toe', 'toe_touch'):
        author_class = FootAccentAuthor
    author = author_class()
    try:
        author.create(phrase, role)
    finally:
        author.evaluation.restore()


if __name__ == '__main__':
    main()
