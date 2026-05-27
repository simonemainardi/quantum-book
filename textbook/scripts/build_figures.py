#!/usr/bin/env python3
"""Generate textbook SVG figures with only the Python standard library."""

from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape


OUT = Path(__file__).resolve().parents[1] / "figures"

INK = "#1f2937"
MUTED = "#64748b"
GRID = "#d7dde8"
BLUE = "#2563eb"
CYAN = "#0891b2"
TEAL = "#0f766e"
GREEN = "#16a34a"
AMBER = "#d97706"
RED = "#dc2626"
PURPLE = "#7c3aed"
PINK = "#be185d"
BG = "#fbfcff"
TEXT_FONT = 'Inter, "Noto Sans", "DejaVu Sans", "Arial Unicode MS", Arial, sans-serif'


def fmt(value: float) -> str:
    if isinstance(value, int):
        return str(value)
    text = f"{value:.3f}".rstrip("0").rstrip(".")
    return text or "0"


def attrs(**kwargs: object) -> str:
    parts = []
    for key, value in kwargs.items():
        if value is None:
            continue
        key = key.replace("_", "-")
        safe = escape(str(value), {'"': "&quot;"})
        parts.append(f'{key}="{safe}"')
    return " ".join(parts)


def tag(name: str, content: str = "", **kwargs: object) -> str:
    a = attrs(**kwargs)
    if content:
        return f"<{name} {a}>{content}</{name}>"
    return f"<{name} {a}/>"


def text(x: float, y: float, value: str, size: int = 20, fill: str = INK,
         weight: int | str = 500, anchor: str = "middle", family: str = TEXT_FONT) -> str:
    return tag("text", escape(value), x=fmt(x), y=fmt(y), fill=fill, **{
        "font-size": size,
        "font-weight": weight,
        "font-family": family,
        "text-anchor": anchor,
        "dominant-baseline": "middle",
    })


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = INK,
         width: float = 2, dash: str | None = None, arrow: bool = False) -> str:
    return tag("line", x1=fmt(x1), y1=fmt(y1), x2=fmt(x2), y2=fmt(y2),
               stroke=stroke, **{"stroke-width": width, "stroke-dasharray": dash,
                                  "stroke-linecap": "round",
                                  "marker-end": "url(#arrow)" if arrow else None})


def circle(cx: float, cy: float, r: float, fill: str = "none", stroke: str = INK,
           width: float = 2, opacity: float | None = None) -> str:
    return tag("circle", cx=fmt(cx), cy=fmt(cy), r=fmt(r), fill=fill,
               stroke=stroke, **{"stroke-width": width, "fill-opacity": opacity})


def rect(x: float, y: float, w: float, h: float, fill: str = "white", stroke: str = INK,
         width: float = 2, rx: float = 8, opacity: float | None = None) -> str:
    return tag("rect", x=fmt(x), y=fmt(y), width=fmt(w), height=fmt(h), fill=fill,
               stroke=stroke, **{"stroke-width": width, "rx": rx, "fill-opacity": opacity})


def path(d: str, fill: str = "none", stroke: str = INK, width: float = 2,
         dash: str | None = None, opacity: float | None = None, arrow: bool = False) -> str:
    return tag("path", d=d, fill=fill, stroke=stroke, **{
        "stroke-width": width,
        "stroke-linecap": "round",
        "stroke-linejoin": "round",
        "stroke-dasharray": dash,
        "stroke-opacity": opacity,
        "marker-end": "url(#arrow)" if arrow else None,
    })


def poly(points: list[tuple[float, float]], fill: str = "none", stroke: str = INK,
         width: float = 2, opacity: float | None = None) -> str:
    pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in points)
    return tag("polyline", points=pts, fill=fill, stroke=stroke,
               **{"stroke-width": width, "stroke-linecap": "round",
                  "stroke-linejoin": "round", "stroke-opacity": opacity})


def svg(width: int, height: int, body: list[str]) -> str:
    defs = """
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1f2937"/>
  </marker>
  <linearGradient id="screenGlow" x1="0" x2="0" y1="0" y2="1">
    <stop offset="0%" stop-color="#dbeafe"/>
    <stop offset="50%" stop-color="#fef3c7"/>
    <stop offset="100%" stop-color="#dbeafe"/>
  </linearGradient>
</defs>
"""
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        rect(0, 0, width, height, fill=BG, stroke="none", rx=0),
        defs,
        *body,
        "</svg>",
        "",
    ])


def save(name: str, width: int, height: int, body: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(svg(width, height, body), encoding="utf-8")


def amplitude_vs_probability() -> None:
    def filled_arrow(x1: float, y: float, x2: float, color: str, width: float = 7) -> str:
        direction = 1 if x2 >= x1 else -1
        head = 13
        body_end = x2 - direction * head
        points = [
            (x2, y),
            (body_end, y - 7),
            (body_end, y + 7),
        ]
        return "\n".join([
            line(x1, y, body_end, y, color, width),
            tag("polygon", points=" ".join(f"{fmt(x)},{fmt(py)}" for x, py in points),
                fill=color, stroke="none"),
        ])

    def probability_bar(x: float, base: float, height: float, color: str,
                        label: str, value: str) -> list[str]:
        return [
            rect(x, base - height, 70, height, fill=color, stroke="none", rx=5, opacity=0.9),
            text(x + 35, base + 24, label, 16, INK, 700),
            text(x + 35, base - height - 20, value, 17, color, 700),
        ]

    body: list[str] = [
        text(500, 42, "Classical Probabilities vs Quantum Amplitudes", 28, weight=700),
        text(500, 75, "Classical adds nonnegative probabilities. Quantum adds directed amplitudes, then squares.", 17, MUTED),
        rect(44, 106, 428, 426, fill="#ffffff", stroke="#cbd5e1"),
        rect(528, 106, 428, 426, fill="#ffffff", stroke="#cbd5e1"),
        text(258, 138, "Classical probability", 24, BLUE, 700),
        text(258, 168, "numbers are already probabilities", 16, MUTED),
        text(742, 138, "Quantum amplitude", 24, PURPLE, 700),
        text(742, 168, "arrows can reinforce or cancel", 16, MUTED),
    ]

    base = 408
    body += probability_bar(112, base, 82, BLUE, "P1", "0.25")
    body += probability_bar(216, base, 82, CYAN, "P2", "0.25")
    body += probability_bar(340, base, 164, GREEN, "P total", "0.50")
    body += [
        line(90, base, 434, base, GRID, 2),
        text(199, 344, "+", 30, MUTED, 700),
        text(306, 344, "=", 30, MUTED, 700),
        text(258, 474, "P total = P1 + P2", 22, GREEN, 700),
        text(258, 500, "Distinguish the alternatives first:", 15, MUTED),
        text(258, 520, "then probabilities add as positive weights.", 15, MUTED),
    ]

    # Same amplitude magnitudes, two different relative phases.
    for y, label, label_color in [(254, "In phase", GREEN), (384, "Opposite phase", RED)]:
        body += [
            text(562, y - 44, label, 18, label_color, 700, anchor="start"),
            line(618, y, 858, y, GRID, 2),
        ]

    body += [
        filled_arrow(628, 254, 714, BLUE),
        filled_arrow(714, 254, 800, CYAN),
        filled_arrow(628, 287, 800, GREEN, 8),
        text(850, 246, "0.5 + 0.5 = 1.0", 17, INK, 700, anchor="end"),
        text(850, 277, "P = |1.0|^2 = 1.0", 17, GREEN, 700, anchor="end"),
        text(620, 318, "add amplitudes first", 15, MUTED, anchor="start"),
        filled_arrow(628, 384, 714, BLUE),
        filled_arrow(714, 384, 628, RED),
        circle(628, 417, 8, fill=PURPLE, stroke="none"),
        text(850, 376, "0.5 + (-0.5) = 0", 17, INK, 700, anchor="end"),
        text(850, 407, "P = |0|^2 = 0", 17, PURPLE, 700, anchor="end"),
        text(620, 448, "cancellation happens before squaring", 15, MUTED, anchor="start"),
        rect(94, 560, 812, 42, fill="#f8fafc", stroke="#cbd5e1", rx=7),
        text(500, 581, "Real takeaway: phase lets equal-strength paths reinforce or cancel.", 17, INK, 700),
    ]
    save("01_amplitudes_vs_probabilities.svg", 1000, 620, body)


def double_slit() -> None:
    def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> str:
        t = max(0.0, min(1.0, t))
        return "#" + "".join(f"{round(a[i] * (1 - t) + b[i] * t):02x}" for i in range(3))

    body: list[str] = [
        text(500, 38, "Double slit interference", 28, weight=700),
        text(500, 70, "Path amplitudes recombine at the screen; bright and dark bands are probability after interference.", 15, MUTED),
        rect(48, 158, 128, 268, fill="#ffffff", stroke="#d7dde8", rx=8),
        circle(112, 285, 18, fill="#fef3c7", stroke=AMBER, width=3),
        circle(112, 285, 5, fill=AMBER, stroke="none"),
        text(112, 337, "single-photon", 15, AMBER, 700),
        text(112, 361, "source", 15, AMBER, 700),
    ]

    # Incoming wavefronts.
    for radius in [42, 74, 106]:
        body.append(path(
            f"M {112 + radius} {285 - radius * 0.55} "
            f"A {radius} {radius * 0.55} 0 0 1 {112 + radius} {285 + radius * 0.55}",
            stroke="#93c5fd",
            width=2,
            opacity=0.58,
        ))

    barrier_x, top, bottom = 285, 128, 470
    slit_l, slit_r = 246, 354
    body += [
        rect(barrier_x, top, 30, bottom - top, fill="#111827", stroke="none", rx=4),
        rect(barrier_x + 1, slit_l - 22, 28, 44, fill=BG, stroke="none", rx=3),
        rect(barrier_x + 1, slit_r - 22, 28, 44, fill=BG, stroke="none", rx=3),
        text(barrier_x + 15, 92, "barrier", 15, MUTED, 700),
        text(barrier_x + 55, slit_l, "L", 18, BLUE, 700, anchor="start"),
        text(barrier_x + 55, slit_r, "R", 18, PURPLE, 700, anchor="start"),
    ]

    # Outgoing wavefronts from each slit. The two colors deliberately overlap
    # gently rather than forming a dense mesh.
    for sx, sy, color in [(barrier_x + 30, slit_l, BLUE), (barrier_x + 30, slit_r, PURPLE)]:
        for radius in [58, 104, 150, 196, 242, 288]:
            body.append(path(
                f"M {sx} {sy - radius} A {radius} {radius} 0 0 1 {sx} {sy + radius}",
                stroke=color,
                width=1.8,
                opacity=0.22,
            ))

    screen_x, screen_y, screen_w, screen_h = 770, 128, 58, 342
    body.append(rect(screen_x - 18, screen_y - 10, screen_w + 118, screen_h + 20, fill="#ffffff", stroke="#d7dde8", rx=8))
    body.append(rect(screen_x, screen_y, screen_w, screen_h, fill="#eff6ff", stroke="#94a3b8", width=2, rx=5))

    # Smooth-ish interference fringe field drawn as narrow horizontal bands.
    cold = (219, 234, 254)
    warm = (245, 158, 11)
    samples: list[tuple[float, float]] = []
    for i in range(120):
        y = screen_y + screen_h * i / 119
        rel = (y - (screen_y + screen_h / 2)) / (screen_h / 2)
        envelope = math.exp(-0.52 * rel * rel)
        fringes = 0.5 + 0.5 * math.cos(8.5 * math.pi * rel)
        intensity = (0.12 + 0.88 * fringes) * envelope
        samples.append((y, intensity))
        body.append(rect(
            screen_x + 2,
            y - 1.9,
            screen_w - 4,
            3.8,
            fill=mix(cold, warm, intensity),
            stroke="none",
            rx=0,
            opacity=0.96,
        ))

    axis_x = screen_x + 82
    body.append(line(axis_x, screen_y, axis_x, screen_y + screen_h, "#cbd5e1", 1.4))
    points = []
    for y, intensity in samples:
        points.append((axis_x + 8 + 68 * intensity, y))
    body.append(poly(points, stroke=AMBER, width=3.1))
    body.append(text(axis_x + 48, screen_y - 22, "intensity", 14, AMBER, 700))
    body.append(text(screen_x + 24, screen_y + screen_h + 26, "screen", 15, MUTED, 700))

    # Two representative paths to one bright and one dark region.
    bright_y = screen_y + screen_h * 0.5
    dark_y = screen_y + screen_h * 0.36
    for target_y, opacity in [(bright_y, 0.88), (dark_y, 0.42)]:
        body.append(path(f"M {barrier_x + 30} {slit_l} C 470 {slit_l - 36}, 650 {target_y - 58}, {screen_x} {target_y}", stroke=BLUE, width=2.4, opacity=opacity))
        body.append(path(f"M {barrier_x + 30} {slit_r} C 470 {slit_r + 36}, 650 {target_y + 58}, {screen_x} {target_y}", stroke=PURPLE, width=2.4, opacity=opacity))

    body += [
        rect(260, 494, 560, 82, fill="#ffffff", stroke="#d7dde8", rx=8),
        text(540, 518, "screen basis: amplitudes add at each pixel", 16, INK, 700),
        text(540, 545, "P(x) = 1/2 |<x|L> + <x|R>|^2", 20, PURPLE, 700),
        text(540, 570, "dark fringe: <x|L> + <x|R> approx 0", 14, RED, 700),
        text(492, 130, "which-path basis keeps L and R distinct", 16, INK, 700),
        text(492, 156, "no amplitude sum, so no fringe pattern", 14, MUTED),
        circle(screen_x + screen_w / 2, bright_y, 6, fill=AMBER, stroke="white", width=2),
        text(screen_x - 20, bright_y + 24, "bright", 13, AMBER, 700, anchor="end"),
        circle(screen_x + screen_w / 2, dark_y, 5, fill="#1e3a8a", stroke="white", width=2),
        text(screen_x - 20, dark_y - 22, "dark", 13, RED, 700, anchor="end"),
    ]
    save("02_double_slit_interference.svg", 1000, 620, body)


def complex_phase_clock() -> None:
    cx, cy, r = 325, 295, 145
    phi = math.radians(42)
    x = cx + r * math.cos(phi)
    y = cy - r * math.sin(phi)
    body: list[str] = [
        text(500, 42, "Complex phase is rotation on the unit circle", 26, weight=700),
        circle(cx, cy, r, fill="#ffffff", stroke="#cbd5e1", width=3),
        line(cx - r - 32, cy, cx + r + 42, cy, GRID, 2, arrow=True),
        line(cx, cy + r + 32, cx, cy - r - 42, GRID, 2, arrow=True),
        text(cx + r + 70, cy, "real", 16, MUTED),
        text(cx, cy - r - 66, "imaginary", 16, MUTED),
        line(cx, cy, x, y, PURPLE, 4, arrow=True),
        line(x, y, x, cy, BLUE, 2, dash="6 6"),
        line(cx, cy, x, cy, BLUE, 3),
        line(x, cy, x, y, CYAN, 3),
        path(f"M {cx+55} {cy} A 55 55 0 0 0 {cx+55*math.cos(phi)} {cy-55*math.sin(phi)}", stroke=AMBER, width=3),
        text(cx + 80, cy - 30, "φ", 17, AMBER, 700),
        text((cx + x) / 2, cy + 24, "cos(φ)", 17, BLUE, 700),
        text(x + 52, (cy + y) / 2, "sin(φ)", 17, CYAN, 700),
        rect(570, 170, 340, 230, fill="#ffffff", stroke="#cbd5e1"),
        text(740, 214, "Euler formula", 25, PURPLE, 700),
        text(740, 265, "e^(iφ) = cos(φ) + i sin(φ)", 23, INK, 700),
        text(740, 322, "Changing φ changes direction,", 17, MUTED),
        text(740, 350, "not the length of the vector.", 17, MUTED),
        text(740, 386, "That direction is quantum phase.", 17, INK, 700),
    ]
    save("03_complex_phase_clock.svg", 1000, 540, body)


def path_vs_screen_basis() -> None:
    body: list[str] = [
        text(500, 42, "The same state gives different probabilities in different bases", 26, weight=700),
        rect(52, 92, 416, 386, fill="#ffffff", stroke="#cbd5e1"),
        rect(532, 92, 416, 386, fill="#ffffff", stroke="#cbd5e1"),
        text(260, 126, "Path / Z basis", 22, BLUE, 700),
        text(740, 126, "Screen / X-like basis", 22, PURPLE, 700),
        text(260, 160, "alternatives stay distinct", 16, MUTED),
        text(740, 160, "alternatives recombine", 16, MUTED),
        circle(178, 260, 42, fill="#dbeafe", stroke=BLUE, width=3),
        circle(342, 260, 42, fill="#dbeafe", stroke=BLUE, width=3),
        text(178, 260, "|L>", 22, BLUE, 700),
        text(342, 260, "|R>", 22, BLUE, 700),
        line(178, 310, 178, 380, BLUE, 3, arrow=True),
        line(342, 310, 342, 380, BLUE, 3, arrow=True),
        text(178, 410, "P(L)=1/2", 19, INK, 700),
        text(342, 410, "P(R)=1/2", 19, INK, 700),
        text(260, 452, "No amplitude sum, no cross term.", 16, MUTED),
        circle(612, 250, 38, fill="#f3e8ff", stroke=PURPLE, width=3),
        circle(612, 350, 38, fill="#f3e8ff", stroke=PURPLE, width=3),
        text(612, 250, "|L>", 21, PURPLE, 700),
        text(612, 350, "|R>", 21, PURPLE, 700),
        circle(820, 300, 46, fill="#fef3c7", stroke=AMBER, width=3),
        text(820, 300, "|x>", 22, AMBER, 700),
        line(650, 250, 774, 292, PURPLE, 3, arrow=True),
        line(650, 350, 774, 308, PURPLE, 3, arrow=True),
        text(744, 400, "<x|ψ> = (<x|L> + <x|R>)/sqrt(2)", 19, INK, 700),
        text(744, 434, "The square of a sum contains interference.", 16, MUTED),
    ]
    save("04_path_vs_screen_basis.svg", 1000, 540, body)


def qubit_state_vector() -> None:
    body: list[str] = [
        text(500, 42, "A qubit stores amplitudes; measurement returns one classical bit", 26, weight=700),
        rect(70, 110, 390, 330, fill="#ffffff", stroke="#cbd5e1"),
        rect(540, 110, 390, 330, fill="#ffffff", stroke="#cbd5e1"),
        text(265, 150, "State vector", 23, BLUE, 700),
        text(735, 150, "Born rule", 23, GREEN, 700),
        text(265, 220, "|ψ> = α |0> + β |1>", 26, INK, 700),
        text(265, 276, "α, β are complex amplitudes", 17, MUTED),
        text(265, 310, "|α|^2 + |β|^2 = 1", 22, BLUE, 700),
        text(265, 360, "phase is stored in the relation", 16, MUTED),
        text(265, 386, "between α and β", 16, MUTED),
        rect(615, 230, 70, 130, fill=BLUE, stroke="none", rx=5, opacity=0.9),
        rect(785, 285, 70, 75, fill=CYAN, stroke="none", rx=5, opacity=0.9),
        line(590, 360, 880, 360, GRID, 2),
        text(650, 388, "P(0)=|α|^2", 17, BLUE, 700),
        text(820, 388, "P(1)=|β|^2", 17, CYAN, 700),
        text(735, 440, "Measurement converts amplitudes into probabilities.", 16, MUTED),
    ]
    save("05_qubit_state_vector.svg", 1000, 540, body)


def sphere_project(cx: float, cy: float, r: float, x: float, y: float, z: float) -> tuple[float, float]:
    return cx + r * (0.82 * x - 0.35 * y), cy + r * (0.28 * x + 0.58 * y - 0.78 * z)


def bloch_reference_states() -> None:
    cx, cy, r = 620, 325, 160

    axes = [
        ("Z basis", "|0>", "|1>", (0, 0, 1), (0, 0, -1), BLUE, RED),
        ("X basis", "|+>", "|->", (1, 0, 0), (-1, 0, 0), GREEN, AMBER),
        ("Y basis", "|+i>", "|-i>", (0, 1, 0), (0, -1, 0), PURPLE, PINK),
    ]

    labels = {
        "|0>": (-26, -36, "end"),
        "|1>": (26, 38, "start"),
        "|+>": (26, 6, "start"),
        "|->": (-26, -10, "end"),
        "|+i>": (-30, 44, "end"),
        "|-i>": (30, -42, "start"),
    }

    body: list[str] = [
        text(500, 38, "Bloch sphere reference states", 26, weight=700),
        text(500, 68, "Opposite endpoints are orthogonal states.", 16, MUTED),
        text(500, 94, "X, Y, and Z are perpendicular measurement axes.", 16, MUTED),
        rect(35, 118, 340, 390, fill="#ffffff", stroke="#cbd5e1"),
        text(205, 154, "How to read it", 22, INK, 700),
        text(205, 202, "One basis = one axis", 17, INK, 700),
        text(205, 234, "opposite endpoints are", 15, MUTED),
        text(205, 258, "orthogonal measurement answers", 15, MUTED),
        text(205, 304, "Basis pairs", 17, INK, 700),
        text(205, 338, "Z: |0>, |1>", 18, BLUE, 700),
        text(205, 372, "X: |+>, |->", 18, GREEN, 700),
        text(205, 406, "Y: |+i>, |-i>", 18, PURPLE, 700),
        text(205, 456, "<0|1> = <+|-> = <+i|-i> = 0", 15, INK, 700),
        text(205, 482, "Axes X, Y, Z are perpendicular.", 15, MUTED),
        circle(cx, cy, r, fill="#ffffff", stroke="#cbd5e1", width=3),
        tag("ellipse", cx=fmt(cx), cy=fmt(cy), rx=fmt(r), ry=fmt(r * 0.37), fill="none", stroke=GRID, **{"stroke-width": 2}),
        tag("ellipse", cx=fmt(cx), cy=fmt(cy), rx=fmt(r * 0.37), ry=fmt(r), fill="none", stroke=GRID, **{"stroke-width": 2, "transform": f"rotate(-27 {cx} {cy})"}),
        tag("ellipse", cx=fmt(cx), cy=fmt(cy), rx=fmt(r * 0.37), ry=fmt(r), fill="none", stroke=GRID, **{"stroke-width": 1.5, "transform": f"rotate(63 {cx} {cy})"}),
    ]

    # Draw axes first and state dots second so arrowheads cannot cover endpoints.
    for basis, pos_label, neg_label, pos_vec, neg_vec, pos_color, neg_color in axes:
        x1, y1 = sphere_project(cx, cy, r, *neg_vec)
        x2, y2 = sphere_project(cx, cy, r, *pos_vec)
        axis_color = pos_color if basis != "Z basis" else BLUE
        body.append(line(x1, y1, x2, y2, axis_color, 5))

    body.append(circle(cx, cy, 5, fill=INK, stroke="white", width=1.5))

    for _, pos_label, neg_label, pos_vec, neg_vec, pos_color, neg_color in axes:
        for label, vec, color in [(pos_label, pos_vec, pos_color), (neg_label, neg_vec, neg_color)]:
            px, py = sphere_project(cx, cy, r, *vec)
            dx, dy, anchor = labels[label]
            lx, ly = px + dx, py + dy
            leader_end_x = lx - 8 if anchor == "start" else lx + 8
            body.append(line(px, py, leader_end_x, ly, "#94a3b8", 1.5))
            body.append(circle(px, py, 10, fill=color, stroke="white", width=3))
            body.append(text(lx, ly, label, 18, color, 700, anchor=anchor))

    body += [
        text(500, 552, "The dots are the basis states; the colored lines are the measurement axes.", 15, INK, 700),
        text(500, 580, "States on different axes are not generally orthogonal.", 15, MUTED),
        text(500, 604, "For example, |0> and |+> have 50/50 overlap.", 15, MUTED),
    ]
    save("06_bloch_reference_states.svg", 1000, 620, body)


def same_theta_phase_ring() -> None:
    cx, cy, r = 500, 295, 170
    theta = math.radians(60)
    body: list[str] = [
        text(500, 40, "Same θ, different phase: same Z probabilities, different states", 25, weight=700),
        circle(cx, cy, r, fill="#ffffff", stroke="#cbd5e1", width=3),
        tag("ellipse", cx=fmt(cx), cy=fmt(cy), rx=fmt(r * math.sin(theta)), ry=fmt(r * math.sin(theta) * 0.37),
            fill="none", stroke=PURPLE, **{"stroke-width": 3, "stroke-dasharray": "7 6"}),
        line(cx, cy, *sphere_project(cx, cy, r, 0, 0, 1), stroke="#94a3b8", width=2, arrow=True),
        line(cx, cy, *sphere_project(cx, cy, r, 0, 0, -1), stroke="#94a3b8", width=2, arrow=True),
        text(500, 107, "|0>", 17, BLUE, 700),
        text(500, 485, "|1>", 17, RED, 700),
    ]
    colors = [GREEN, PURPLE, AMBER, PINK]
    labels = ["φ = 0", "φ = π/2", "φ = π", "φ = 3π/2"]
    for i, phi in enumerate([0, math.pi / 2, math.pi, 3 * math.pi / 2]):
        x = math.sin(theta) * math.cos(phi)
        y = math.sin(theta) * math.sin(phi)
        z = math.cos(theta)
        px, py = sphere_project(cx, cy, r, x, y, z)
        body.append(line(cx, cy, px, py, colors[i], 2.5, arrow=True))
        body.append(circle(px, py, 9, fill=colors[i], stroke="white", width=2))
        anchor = "start" if px > cx else "end"
        body.append(text(px + (18 if px > cx else -18), py - 12, labels[i], 15, colors[i], 700, anchor=anchor))
    body += [
        rect(70, 154, 255, 250, fill="#ffffff", stroke="#cbd5e1"),
        text(198, 188, "For θ = 60 deg", 21, INK, 700),
        text(198, 238, "cos(θ/2) = sqrt(3)/2", 16, MUTED),
        text(198, 270, "sin(θ/2) = 1/2", 16, MUTED),
        text(198, 326, "P(Z=0) = 0.75", 20, BLUE, 700),
        text(198, 360, "P(Z=1) = 0.25", 20, CYAN, 700),
        rect(695, 160, 235, 225, fill="#ffffff", stroke="#cbd5e1"),
        text(812, 196, "Why it matters", 21, INK, 700),
        text(812, 250, "Z cannot see φ", 17, MUTED),
        text(812, 286, "X reads cos(φ)", 17, GREEN, 700),
        text(812, 322, "Y reads sin(φ)", 17, PURPLE, 700),
    ]
    save("07_same_theta_phase_ring.svg", 1000, 540, body)


def probabilities_zxy() -> None:
    width, height = 1000, 620
    body: list[str] = [
        text(500, 38, "For θ = 60 deg, Z is flat while X and Y reveal phase", 25, weight=700),
    ]
    panels = [
        (70, 95, "Z basis", "P(Z=0)", lambda p: 0.75, BLUE),
        (370, 95, "X basis", "P(X=+)", lambda p: (1 + math.sin(math.radians(60)) * math.cos(p)) / 2, GREEN),
        (670, 95, "Y basis", "P(Y=+i)", lambda p: (1 + math.sin(math.radians(60)) * math.sin(p)) / 2, PURPLE),
    ]
    for x0, y0, title, ylabel, func, color in panels:
        w, h = 250, 360
        body.append(rect(x0, y0, w, h, fill="#ffffff", stroke="#cbd5e1"))
        body.append(text(x0 + w / 2, y0 + 32, title, 21, color, 700))
        gx, gy, gw, gh = x0 + 38, y0 + 74, w - 58, h - 130
        body.append(line(gx, gy + gh, gx + gw, gy + gh, GRID, 2))
        body.append(line(gx, gy, gx, gy + gh, GRID, 2))
        for frac in [0, 0.5, 1.0]:
            yy = gy + gh * (1 - frac)
            body.append(line(gx - 5, yy, gx + gw, yy, "#e5e7eb", 1))
            body.append(text(gx - 12, yy, f"{frac:.1f}", 12, MUTED, anchor="end"))
        points = []
        for i in range(181):
            phi = 2 * math.pi * i / 180
            val = func(phi)
            px = gx + gw * i / 180
            py = gy + gh * (1 - val)
            points.append((px, py))
        body.append(poly(points, stroke=color, width=3.2))
        for phi, label in [(0, "0"), (math.pi / 2, "π/2"), (math.pi, "π"), (3 * math.pi / 2, "3π/2"), (2 * math.pi, "2π")]:
            px = gx + gw * phi / (2 * math.pi)
            body.append(line(px, gy + gh, px, gy + gh + 5, MUTED, 1.5))
            if label in ("0", "π", "2π"):
                body.append(text(px, gy + gh + 24, label, 12, MUTED))
        body.append(text(x0 + w / 2, y0 + h - 34, ylabel, 16, color, 700))
    body += [
        rect(170, 505, 660, 70, fill="#ffffff", stroke="#cbd5e1"),
        text(500, 528, "Interpretation: a basis is a choice of which Bloch-vector component becomes a 0/1 bias.", 17, INK, 700),
        text(500, 558, "Z reads r_z, X reads r_x, and Y reads r_y.", 17, MUTED),
    ]
    save("08_zxy_measurement_probabilities.svg", width, height, body)


def basis_recombination() -> None:
    body: list[str] = [
        text(500, 40, "Where interference enters the algebra", 26, weight=700),
        text(500, 70, "A measurement basis either selects one component or recombines components.", 16, MUTED),
    ]
    cards = [
        (60, 125, "Z measurement", "<0|ψ> = α", "selects one component", BLUE),
        (365, 125, "X measurement", "<+|ψ> = (α + β)/sqrt(2)", "adds amplitudes", GREEN),
        (670, 125, "Y measurement", "<+i|ψ> = (α - iβ)/sqrt(2)", "adds with a phase shift", PURPLE),
    ]
    for x, y, title, formula, note, color in cards:
        body += [
            rect(x, y, 270, 265, fill="#ffffff", stroke="#cbd5e1"),
            text(x + 135, y + 36, title, 20, color, 700),
            text(x + 135, y + 92, formula, 17, INK, 700),
            text(x + 135, y + 140, note, 16, MUTED),
            line(x + 70, y + 192, x + 200, y + 192, color, 3, arrow=True),
            text(x + 135, y + 228, "then square magnitude", 15, MUTED),
        ]
    body += [
        rect(170, 435, 660, 62, fill="#f8fafc", stroke="#cbd5e1"),
        text(500, 466, "If the amplitude is a sum, |sum|^2 contains cross terms: interference.", 20, INK, 700),
    ]
    save("09_basis_recombination_algebra.svg", 1000, 540, body)


def hadamard_columns() -> None:
    body: list[str] = [
        text(500, 40, "A gate matrix is built from what the gate does to basis vectors", 25, weight=700),
        rect(62, 110, 260, 310, fill="#ffffff", stroke="#cbd5e1"),
        rect(370, 110, 260, 310, fill="#ffffff", stroke="#cbd5e1"),
        rect(678, 110, 260, 310, fill="#ffffff", stroke="#cbd5e1"),
        text(192, 150, "Input basis", 21, BLUE, 700),
        text(500, 150, "Hadamard action", 21, GREEN, 700),
        text(808, 150, "Matrix columns", 21, PURPLE, 700),
        text(192, 225, "|0> = (1,0)^T", 21, INK, 700),
        text(192, 305, "|1> = (0,1)^T", 21, INK, 700),
        text(500, 225, "H|0> = (|0> + |1>)/sqrt(2)", 18, INK, 700),
        text(500, 305, "H|1> = (|0> - |1>)/sqrt(2)", 18, INK, 700),
        text(808, 240, "H = 1/sqrt(2)", 19, PURPLE, 700),
        text(808, 285, "[ 1   1 ]", 27, INK, 700, family="Menlo, Consolas, monospace"),
        text(808, 326, "[ 1  -1 ]", 27, INK, 700, family="Menlo, Consolas, monospace"),
        line(322, 230, 370, 230, INK, 2.4, arrow=True),
        line(630, 230, 678, 230, INK, 2.4, arrow=True),
        line(322, 310, 370, 310, INK, 2.4, arrow=True),
        line(630, 310, 678, 310, INK, 2.4, arrow=True),
        rect(190, 452, 620, 55, fill="#f8fafc", stroke="#cbd5e1"),
        text(500, 480, "First output becomes column 1; second output becomes column 2.", 19, INK, 700),
    ]
    save("10_hadamard_matrix_columns.svg", 1000, 540, body)


def rotation_readout_circuit() -> None:
    body: list[str] = [
        text(500, 40, "Real devices usually read Z; circuits rotate first to read X or Y", 25, weight=700),
        text(500, 70, "This is how phase information becomes a classical 0/1 bias.", 16, MUTED),
    ]
    rows = [
        (145, "Measure Z", [], BLUE, "native readout"),
        (275, "Measure X", ["H"], GREEN, "H maps |+> to |0>"),
        (405, "Measure Y", ["S^dagger", "H"], PURPLE, "S^dagger then H maps |+i> to |0>"),
    ]
    for y, label, gates, color, note in rows:
        body.append(text(130, y, label, 20, color, 700, anchor="end"))
        body.append(line(170, y, 780, y, INK, 2))
        x = 300
        for gate in gates:
            body.append(rect(x - 38, y - 28, 76, 56, fill="#ffffff", stroke=color, width=2.5, rx=6))
            body.append(text(x, y, gate, 18, color, 700))
            x += 120
        body.append(rect(795, y - 34, 78, 68, fill="#fef3c7", stroke=AMBER, width=2.5, rx=8))
        body.append(path(f"M 817 {y+15} A 18 18 0 0 1 851 {y+15}", stroke=INK, width=2.2))
        body.append(line(834, y + 15, 855, y - 10, INK, 2.2))
        body.append(text(834, y + 48, "Z", 14, AMBER, 700))
        body.append(text(500, y + 55, note, 15, MUTED))
    body.append(rect(148, 488, 704, 36, fill="#ffffff", stroke="#cbd5e1"))
    body.append(text(500, 506, "The detector is unchanged; only the pre-measurement rotation changes the basis.", 17, INK, 700))
    save("11_rotation_before_readout.svg", 1000, 560, body)


def technology_examples() -> None:
    body: list[str] = [
        text(500, 40, "Practical quantum technologies use the same amplitude-and-phase logic", 25, weight=700),
    ]
    items = [
        (105, 145, "Algorithms", "Amplify useful amplitudes;\ncancel wrong branches.", BLUE),
        (365, 145, "Sensing", "Tiny phase shifts become\nmeasurable probability shifts.", GREEN),
        (625, 145, "Cryptography", "Measurement disturbance\nbecomes a security signal.", PURPLE),
        (105, 345, "Hardware", "Pulses implement rotations;\nreadout is often Z-like.", AMBER),
        (365, 345, "Feature maps", "Data can be encoded as\nphases before interference.", PINK),
        (625, 345, "Circuits", "Gates arrange recombination\nbefore the final measurement.", CYAN),
    ]
    for x, y, title, desc, color in items:
        body.append(rect(x, y, 230, 132, fill="#ffffff", stroke="#cbd5e1"))
        body.append(circle(x + 34, y + 38, 18, fill=color, stroke="none", opacity=0.9))
        body.append(text(x + 68, y + 38, title, 20, color, 700, anchor="start"))
        lines = desc.split("\n")
        body.append(text(x + 115, y + 83, lines[0], 15, MUTED))
        body.append(text(x + 115, y + 108, lines[1], 15, MUTED))
    body += [
        line(850, 180, 910, 270, INK, 2.5, arrow=True),
        line(850, 410, 910, 320, INK, 2.5, arrow=True),
        circle(920, 295, 50, fill="#ecfeff", stroke=CYAN, width=3),
        text(920, 284, "same", 16, CYAN, 700),
        text(920, 310, "math", 16, CYAN, 700),
    ]
    save("12_practical_quantum_technology.svg", 1000, 540, body)


def main() -> None:
    amplitude_vs_probability()
    double_slit()
    complex_phase_clock()
    path_vs_screen_basis()
    qubit_state_vector()
    bloch_reference_states()
    same_theta_phase_ring()
    probabilities_zxy()
    basis_recombination()
    hadamard_columns()
    rotation_readout_circuit()
    technology_examples()
    print(f"Wrote SVG figures to {OUT}")


if __name__ == "__main__":
    main()
