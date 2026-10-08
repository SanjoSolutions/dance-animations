"""Salsa On1 footfalls and partner routes, in meters and musical counts."""

from dataclasses import dataclass
import math


def blend(first, last, amount):
    return tuple(a + (b - a) * amount for a, b in zip(first, last))


def ease(amount):
    amount = max(0, min(1, amount))
    return amount * amount * (3 - 2 * amount)


def rotate(position, angle):
    x, y, z = position
    return (
        x * math.cos(angle) - y * math.sin(angle),
        x * math.sin(angle) + y * math.cos(angle),
        z,
    )


@dataclass(frozen=True)
class SalsaMove:
    name: str
    family: str
    pattern: str = "basic"
    figure: str = "stationary"
    counts: int = 8
    turns: float = 0
    turning_actor: str = "partner"
    connection: str = "open"
    loop: bool = True


class SalsaLibrary:
    """A finite, explicitly named social-salsa repertoire."""

    def __init__(self):
        self.moves = [
            SalsaMove("basic", "Foundations"),
            SalsaMove("side_basic", "Foundations", "side"),
            SalsaMove("back_basic", "Foundations", "back"),
            SalsaMove("cumbia_basic", "Foundations", "cumbia"),
            SalsaMove("open_break", "Foundations", "open_break"),
            SalsaMove("guapea", "Cuban", "side", connection="double"),
            SalsaMove("closed_basic", "Foundations", connection="closed"),
        ]
        for actor, label in (("partner", "follower"), ("player", "leader")):
            for direction, turns in (("right", -1), ("left", 1)):
                self.moves.append(
                    SalsaMove(
                        f"{label}_{direction}_turn",
                        "Turns",
                        figure="turn",
                        turns=turns,
                        turning_actor=actor,
                        connection="turn",
                        loop=False,
                    )
                )
        self.moves.extend(
            [
                SalsaMove(
                    "follower_double_right_turn",
                    "Turns",
                    figure="turn",
                    counts=16,
                    turns=-2,
                    connection="turn",
                    loop=False,
                ),
                SalsaMove(
                    "cross_body_lead",
                    "Cross-body",
                    figure="cross",
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "cross_body_inside_turn",
                    "Cross-body",
                    figure="cross",
                    counts=16,
                    turns=1,
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "cross_body_outside_turn",
                    "Cross-body",
                    figure="cross",
                    counts=16,
                    turns=-1,
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "reverse_cross_body",
                    "Cross-body",
                    figure="reverse_cross",
                    counts=16,
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "copa", "Partner patterns", figure="copa", connection="release"
                ),
                SalsaMove(
                    "enchufla",
                    "Cuban",
                    figure="exchange",
                    turns=0.5,
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "dile_que_no",
                    "Cuban",
                    figure="dile",
                    pattern="back",
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "vacilala",
                    "Cuban",
                    figure="turn",
                    turns=-1,
                    connection="release",
                    loop=False,
                ),
                SalsaMove(
                    "hecho",
                    "Cuban",
                    figure="turn",
                    turns=-1,
                    connection="turn",
                    loop=False,
                ),
                SalsaMove(
                    "around_the_world",
                    "Partner patterns",
                    figure="orbit",
                    counts=16,
                    connection="double",
                    loop=False,
                ),
            ]
        )
        for name, pattern in (
            ("mambo_shine", "basic"),
            ("side_shine", "side"),
            ("suzie_q", "suzie_q"),
            ("grapevine", "grapevine"),
            ("crossover_breaks", "crossovers"),
            ("diagonal_breaks", "diagonal"),
            ("diamond_step", "diamond"),
            ("toe_taps", "taps"),
            ("heel_digs", "heels"),
            ("kick_ball_change", "kicks"),
            ("cuban_rocks", "rocks"),
            ("shoulder_shimmy", "shimmy"),
            ("body_wave", "wave"),
        ):
            self.moves.append(SalsaMove(name, "Shines", pattern, connection="solo"))


class SalsaChoreography:
    frames_per_count = 10
    tempo = 144
    fps = 24
    steps = (1, 2, 3, 5, 6, 7)

    def __init__(self, move):
        self.move = move

    def retrieve_route(self, actor, count):
        follower = actor == "partner"
        angle = math.pi if follower else 0
        x, y = (0, -0.43) if follower else (0, 0.43)
        if self.move.connection == "closed":
            y *= 0.55
        elif self.move.connection == "turn":
            y *= (
                0.60
                if self.move.turning_actor == "partner" and self.move.turns > 0
                else (0.58 if abs(self.move.turns) > 1 else 0.55)
            )
        figure = self.move.figure
        progress = ease((count - 2) / (self.move.counts - 3))
        if self.move.connection == "solo":
            x, y, angle = (0.65 if follower else -0.65), 0, 0
        elif figure == "turn":
            if actor == self.move.turning_actor:
                angle += math.tau * self.move.turns * progress
        elif figure in {"cross", "reverse_cross", "dile"}:
            sign = -1 if figure == "reverse_cross" else 1
            if follower:
                y = -0.43 + 0.86 * progress
                if figure == "dile":
                    x = 0.18 * math.sin(math.pi * progress)
                angle += (
                    sign * math.pi * progress + math.tau * self.move.turns * progress
                )
            else:
                x = (
                    -sign
                    * 0.62
                    * ease(count / 2)
                    * ease((self.move.counts - 2 - count) / 1)
                )
                y = 0.43 - 0.86 * progress
                angle += sign * math.pi * progress
        elif figure == "exchange":
            phase = math.pi * progress
            x = (0.40 if follower else -0.40) * math.sin(phase)
            y *= math.cos(phase)
            angle += math.pi * progress
        elif figure == "copa":
            progress = ease((count - 1) / 5)
            amount = math.sin(math.pi * progress) ** 2
            x += (0.32 if follower else -0.16) * amount
            y += (0.27 if follower else 0.03) * amount
            angle += (math.pi / 2 if follower else -math.pi / 4) * amount
        elif figure == "orbit":
            phase = math.tau * ease(count / self.move.counts)
            x, y, _ = rotate((x, y, 0), phase)
            angle += phase
        return (x, y, angle)

    def retrieve_step_offset(self, actor, number, side):
        pattern = self.move.pattern
        sign = 1 if side == "left" else -1
        follower = actor == "partner" and self.move.connection != "solo"
        half = number < 4
        breaking = number in (1, 5)
        x, y, height, pitch = sign * 0.115, -0.023, 0, 0
        if self.move.figure != "stationary":
            return (x, y, height, pitch)
        if pattern == "basic":
            y += (-0.18 if half != follower else 0.18) if breaking else 0
        elif pattern == "side":
            x += sign * 0.16 if breaking else 0
        elif pattern in {"back", "open_break"}:
            y += (0.19 if pattern == "back" else 0.24) if breaking else 0
        elif pattern in {"cumbia", "crossovers"}:
            if breaking:
                x -= sign * (0.18 if pattern == "cumbia" else 0.25)
                y += 0.18 if pattern == "cumbia" else -0.18
        elif pattern in {"suzie_q", "grapevine"}:
            travel = 0.13 * (1 if half else -1)
            x += travel if number in (1, 2, 5) else 0
            if breaking:
                x -= sign * 0.19
                y += -0.15 if pattern == "suzie_q" else 0.16
        elif pattern == "diagonal":
            if breaking:
                x += sign * 0.12
                y -= 0.16
        elif pattern == "diamond":
            offsets = {
                1: (0, -0.17),
                2: (-0.17, 0),
                3: (0, 0),
                5: (0, 0.17),
                6: (0, 0),
                7: (0, 0),
            }
            dx, dy = offsets[number]
            x += dx
            y += dy
        elif pattern in {"taps", "heels", "kicks"}:
            if breaking:
                y -= 0.20
                height = (
                    0.12 if pattern == "kicks" else (0.015 if pattern == "heels" else 0)
                )
                pitch = (
                    -0.3 if pattern == "heels" else (0.25 if pattern == "kicks" else 0)
                )
        elif pattern == "rocks":
            x += sign * 0.07 if breaking else 0
        return (x, y, height, pitch)

    def retrieve_footfalls(self, actor, side):
        initial = self.retrieve_route(actor, 0)
        sign = 1 if side == "left" else -1
        local = rotate((sign * 0.115, -0.023, 0), initial[2])
        events = [(0, (initial[0] + local[0], initial[1] + local[1], 0, initial[2], 0))]
        for count in range(1, self.move.counts + 1):
            number = (count - 1) % 8 + 1
            stepping = "left" if number in (1, 3, 6) else "right"
            if actor == "partner" and self.move.connection != "solo":
                stepping = "right" if stepping == "left" else "left"
            if number in self.steps and stepping == side:
                route = self.retrieve_route(actor, count)
                dx, dy, height, pitch = self.retrieve_step_offset(actor, number, side)
                offset = rotate((dx, dy, 0), route[2])
                events.append(
                    (
                        count,
                        (
                            route[0] + offset[0],
                            route[1] + offset[1],
                            height,
                            route[2],
                            pitch,
                        ),
                    )
                )
        return events

    def retrieve_foot(self, actor, side, count):
        events = self.retrieve_footfalls(actor, side)
        previous = events[0][1]
        for landing, target in events[1:]:
            if count <= landing:
                amount = max(0, min(1, (count - landing + 0.8) / 0.8))
                pose = list(blend(previous, target, ease(amount)))
                pose[2] += 0.045 * math.sin(math.pi * amount) ** 2
                return tuple(pose)
            previous = target
        return previous

    def retrieve_samples(self):
        counts = {0, self.move.counts}
        for count in range(1, self.move.counts + 1):
            if (count - 1) % 8 + 1 in self.steps:
                counts.update((count - 0.8, count - 0.4, count))
            else:
                counts.add(count)
        return sorted(round(count * self.frames_per_count) for count in counts)
