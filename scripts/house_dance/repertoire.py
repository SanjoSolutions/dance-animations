"""House vocabulary expressed as eight-beat footfall phrases in meters."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Phrase:
    name: str
    family: str
    steps: tuple = ()
    lift: float = .09
    turn: float = 0
    depth: float = .11
    description: str = ''


# Alternating L/R landing offsets relative to each foot's neutral stance.
PHRASES = (
    Phrase('jack', 'jacking', description='Elastic knee compression with chest-led forward/back jack.'),
    Phrase('side_jack', 'jacking', depth=.14, description='Lateral weight transfer through a deeper jack.'),
    Phrase('body_roll', 'jacking', depth=.13, description='Chest-to-pelvis wave over planted feet.'),
    Phrase('side_step', 'footwork', ((.18,0),(.18,0),(0,0),(0,0),(-.12,0),(-.12,0),(0,0),(0,0))),
    Phrase('skate', 'footwork', ((.15,-.12),(-.08,.06),(.08,.06),(-.15,-.12),(.1,-.08),(-.1,-.08),(0,0),(0,0))),
    Phrase('shuffle', 'footwork', ((0,-.22),(0,.13),(0,.13),(0,-.22),(0,-.13),(0,.1),(0,0),(0,0)), .07),
    Phrase('loose_legs', 'footwork', ((-.1,-.14),(.1,.1),(.12,.1),(-.12,-.14),(-.1,.1),(.1,-.1),(0,0),(0,0)), .13),
    Phrase('pas_de_bourree', 'footwork', ((-.15,.16),(.13,0),(.08,-.16),(.15,.16),(-.13,0),(-.08,-.16),(0,0),(0,0)), .065),
    Phrase('cross_step', 'footwork', ((-.23,-.18),(.06,.08),(.08,0),(.23,-.18),(-.06,.08),(-.08,0),(0,0),(0,0))),
    Phrase('salsa_step', 'footwork', ((0,-.23),(0,0),(0,0),(0,.23),(0,0),(0,0),(0,0),(0,0)), .07),
    Phrase('train', 'footwork', ((0,-.22),(0,-.22),(0,.12),(0,.12),(0,-.12),(0,-.12),(0,0),(0,0)), .08),
    Phrase('running_man', 'footwork', ((0,-.2),(0,.16),(0,.16),(0,-.2),(0,-.16),(0,.16),(0,0),(0,0)), .23),
    Phrase('farmer', 'footwork', ((.18,-.16),(-.18,-.16),(.18,.12),(-.18,.12),(.12,-.12),(-.12,-.12),(0,0),(0,0)), .17),
    Phrase('stomp', 'footwork', ((.09,-.12),(-.09,-.12),(.09,.08),(-.09,.08),(.05,-.08),(-.05,-.08),(0,0),(0,0)), .18, depth=.15),
    Phrase('tip_tap', 'footwork', ((0,-.16),(0,-.16),(.12,0),(-.12,0),(0,.12),(0,.12),(0,0),(0,0)), .055),
    Phrase('kick_ball_change', 'footwork', ((0,-.12),(.08,.08),(0,0),(0,-.12),(-.08,.08),(0,0),(0,0),(0,0)), .25),
    Phrase('scissors', 'footwork', ((0,-.2),(0,.2),(0,.2),(0,-.2),(0,-.12),(0,.12),(0,0),(0,0)), .12),
    Phrase('charleston', 'footwork', ((0,-.22),(0,.18),(0,.18),(0,-.22),(.07,-.12),(-.07,.12),(0,0),(0,0)), .16),
    Phrase('box_step', 'footwork', ((0,-.2),(.18,-.2),(.18,0),(0,0),(0,.15),(-.12,.15),(0,0),(0,0))),
    Phrase('diamond_step', 'footwork', ((-.08,-.2),(-.15,0),(-.08,.2),(.15,0),(.08,-.15),(.08,.1),(0,0),(0,0))),
    Phrase('heel_dig', 'footwork', ((0,-.2),(0,-.2),(0,0),(0,0),(.1,-.15),(-.1,-.15),(0,0),(0,0)), .06),
    Phrase('toe_touch', 'footwork', ((0,.2),(0,.2),(0,0),(0,0),(.15,0),(-.15,0),(0,0),(0,0)), .06),
    Phrase('heel_toe', 'footwork', ((.06,-.05),(-.06,-.05),(-.04,.05),(.04,.05),(.06,-.05),(-.06,-.05),(0,0),(0,0)), .045),
    Phrase('swivel', 'footwork', ((.08,0),(-.08,0),(-.06,0),(.06,0),(.08,0),(-.08,0),(0,0),(0,0)), .05),
    Phrase('open_close', 'footwork', ((.18,0),(-.18,0),(-.07,0),(.07,0),(.12,0),(-.12,0),(0,0),(0,0)), .11),
    Phrase('quarter_turn_left', 'turns', ((0,0),)*8, .1, 1.57079632679),
    Phrase('quarter_turn_right', 'turns', ((0,0),)*8, .1, -1.57079632679),
    Phrase('half_turn_return', 'turns', ((0,0),)*8, .13, 3.14159265359),
    Phrase('low_sweep', 'lofting_preparation', ((.23,-.1),(-.23,-.1),(.23,.1),(-.23,.1),(.12,0),(-.12,0),(0,0),(0,0)), .055, depth=.24),
    Phrase('deep_jack', 'lofting_preparation', depth=.27, description='Grounded low-level jack for lofting entry.'),
    Phrase('relaxed_position', 'positions', depth=.04),
    Phrase('ready_position', 'positions', depth=.11),
    Phrase('low_position', 'positions', depth=.25),
    Phrase('wide_position', 'positions', depth=.15),
    Phrase('staggered_position', 'positions', depth=.13),
)


FLOOR_PHRASES=(
    Phrase('floor_support_position','positions'),
    Phrase('lofting_floor_rock','lofting'),
    Phrase('lofting_leg_sweep_left','lofting'),
    Phrase('lofting_leg_sweep_right','lofting'),
    Phrase('lofting_knee_switch','lofting'),
    Phrase('lofting_body_wave','lofting'),
)


TRANSITIONS={
    'relaxed_to_ready':(.04,.11),
    'ready_to_relaxed':(.11,.04),
    'ready_to_low':(.11,.25),
    'low_to_ready':(.25,.11),
}


CATALOG = tuple((phrase, "author") for phrase in PHRASES) + tuple((phrase, "floor") for phrase in FLOOR_PHRASES) + tuple((Phrase(name, "transitions"), "transitions") for name in TRANSITIONS)
