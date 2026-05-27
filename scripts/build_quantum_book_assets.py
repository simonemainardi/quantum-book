#!/usr/bin/env python3

"""Generate the Quantum Book's deterministic SVG figures.

The script intentionally uses only the Python standard library so the figures
can be rebuilt from the repo's existing virtualenv without a plotting stack.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path


INK = "#14202e"
MUTED = "#5d6877"
TEAL = "#0f8b8d"
BLUE = "#2f6fbb"
CORAL = "#e76f51"
GOLD = "#f2b84b"
GREEN = "#3a9f6b"
PAPER = "#fbf7ef"


def wave_path(x0: float, y0: float, width: float, amp: float, cycles: float, phase: float) -> str:
    pts = []
    for i in range(180):
        t = i / 179
        x = x0 + t * width
        y = y0 + math.sin(t * cycles * 2 * math.pi + phase) * amp
        pts.append((x, y))
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def plot_points(values, x0, y0, w, h):
    pts = []
    for i, value in enumerate(values):
        x = x0 + i * (w / (len(values) - 1))
        y = y0 + (1 - value) * h
        pts.append((x, y))
    return pts


def polyline(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def arrow(x1, y1, x2, y2, color, width=4, marker="arrow"):
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{width}" stroke-linecap="round" marker-end="url(#{marker})"/>'
    )


def svg(width, height, title, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="paper" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="#fffaf1"/>
      <stop offset="0.54" stop-color="#f7efe1"/>
      <stop offset="1" stop-color="#e9f3f0"/>
    </linearGradient>
    <linearGradient id="night" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="#101927"/>
      <stop offset="0.55" stop-color="#19323f"/>
      <stop offset="1" stop-color="#2a4f50"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="44%" r="58%">
      <stop offset="0" stop-color="#f7d98c" stop-opacity="0.55"/>
      <stop offset="0.52" stop-color="#0f8b8d" stop-opacity="0.22"/>
      <stop offset="1" stop-color="#101927" stop-opacity="0"/>
    </radialGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#14202e" flood-opacity="0.18"/>
    </filter>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <path d="M 0 0 L 12 6 L 0 12 z" fill="context-stroke"/>
    </marker>
    <style>
      .title {{ font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif; font-size: 54px; font-weight: 700; fill: {INK}; }}
      .h2 {{ font-family: Avenir Next, "Noto Sans", "DejaVu Sans", "Arial Unicode MS", Segoe UI, Helvetica, Arial, sans-serif; font-size: 28px; font-weight: 700; fill: {INK}; }}
      .label {{ font-family: Avenir Next, "Noto Sans", "DejaVu Sans", "Arial Unicode MS", Segoe UI, Helvetica, Arial, sans-serif; font-size: 19px; fill: {INK}; }}
      .small {{ font-family: Avenir Next, "Noto Sans", "DejaVu Sans", "Arial Unicode MS", Segoe UI, Helvetica, Arial, sans-serif; font-size: 15px; fill: {MUTED}; }}
      .formula {{ font-family: Menlo, "DejaVu Sans Mono", "Noto Sans Mono", "SFMono-Regular", Consolas, monospace; font-size: 18px; fill: {INK}; }}
      .hair {{ stroke: rgba(20,32,46,0.16); stroke-width: 1.2; }}
      .axis {{ stroke: rgba(20,32,46,0.42); stroke-width: 2; }}
    </style>
    {extra_defs}
  </defs>
  {body}
</svg>
'''


def cover():
    waves = []
    for n, (color, phase, y) in enumerate([(TEAL, 0.1, 384), (GOLD, 1.6, 425), (CORAL, 3.1, 466), (BLUE, 4.2, 507)]):
        waves.append(
            f'<path d="{wave_path(120, y, 1360, 34 + n * 6, 4.5, phase)}" fill="none" stroke="{color}" stroke-width="{5+n}" stroke-opacity="0.52"/>'
        )
    rings = []
    for r in range(74, 242, 28):
        rings.append(f'<ellipse cx="1170" cy="430" rx="{r*1.22}" ry="{r*0.48}" fill="none" stroke="#d6f6ef" stroke-opacity="0.18" stroke-width="2"/>')
        rings.append(f'<ellipse cx="1170" cy="430" rx="{r*0.52}" ry="{r*1.02}" fill="none" stroke="#d6f6ef" stroke-opacity="0.14" stroke-width="2" transform="rotate(-28 1170 430)"/>')
    vectors = "\n".join(
        [
            arrow(1170, 430, 1170, 205, "#d6f6ef", 5),
            arrow(1170, 430, 1398, 490, GOLD, 6),
            arrow(1170, 430, 1018, 326, CORAL, 6),
            '<circle cx="1170" cy="430" r="9" fill="#fff7d1"/>',
        ]
    )
    particles = []
    for i in range(34):
        x = 88 + (i * 137) % 1410
        y = 96 + (i * 83) % 640
        r = 2 + (i % 5)
        color = [TEAL, GOLD, CORAL, BLUE, GREEN][i % 5]
        particles.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" fill-opacity="0.34"/>')
    body = f'''
  <rect width="1600" height="900" fill="url(#night)"/>
  <rect width="1600" height="900" fill="url(#glow)"/>
  <g opacity="0.9">{''.join(particles)}</g>
  <path d="{wave_path(0, 710, 1600, 90, 2.2, 0)}" fill="none" stroke="#f2b84b" stroke-width="110" stroke-opacity="0.07"/>
  {''.join(waves)}
  <g opacity="0.95">{''.join(rings)}{vectors}</g>
  <g transform="translate(112 548)" opacity="0.6">
    <path d="{wave_path(0, 0, 580, 26, 2.8, 0.4)}" fill="none" stroke="{TEAL}" stroke-width="8"/>
    <path d="{wave_path(0, 40, 580, 26, 2.8, 3.54)}" fill="none" stroke="{GOLD}" stroke-width="8"/>
    <circle cx="622" cy="20" r="18" fill="{CORAL}"/>
  </g>
'''
    return svg(1600, 900, "Quantum Computing for Engineers cover", body)


def complex_plane():
    rays = []
    cx, cy, r = 560, 360, 225
    for k in range(16):
        a = k * math.tau / 16
        x = cx + math.cos(a) * r
        y = cy - math.sin(a) * r
        rays.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" class="hair"/>')
    a = math.radians(42)
    px, py = cx + math.cos(a) * r, cy - math.sin(a) * r
    body = f'''
  <rect width="1120" height="720" fill="url(#paper)"/>
  <text x="62" y="82" class="title">Complex Numbers Are Rotations</text>
  <text x="66" y="126" class="small">The qubit's phase is an angle on this plane, not an ordinary probability weight.</text>
  <g transform="translate(0 0)" filter="url(#softShadow)">
    <rect x="60" y="166" width="1000" height="480" rx="24" fill="#ffffff" fill-opacity="0.82"/>
  </g>
  <g>
    <line x1="230" y1="{cy}" x2="900" y2="{cy}" class="axis" marker-end="url(#arrow)"/>
    <line x1="{cx}" y1="610" x2="{cx}" y2="130" class="axis" marker-end="url(#arrow)"/>
    <text x="914" y="{cy+6}" class="label">real</text>
    <text x="{cx-16}" y="116" class="label">imaginary</text>
    {''.join(rays)}
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLUE}" stroke-width="4" stroke-opacity="0.82"/>
    <path d="M {cx+86:.1f} {cy:.1f} A 86 86 0 0 0 {cx+math.cos(a)*86:.1f} {cy-math.sin(a)*86:.1f}" fill="none" stroke="{CORAL}" stroke-width="6" stroke-linecap="round"/>
    {arrow(cx, cy, px, py, TEAL, 7)}
    <line x1="{px:.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{cy}" stroke="{GOLD}" stroke-width="4" stroke-dasharray="8 8"/>
    <line x1="{cx}" y1="{py:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="{CORAL}" stroke-width="4" stroke-dasharray="8 8"/>
    <circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{TEAL}"/>
    <text x="{cx+118}" y="{cy-32}" class="label">θ</text>
    <text x="{cx+114}" y="{cy+50}" class="formula">cos θ</text>
    <text x="{px+16:.1f}" y="{py+10:.1f}" class="formula">e^(iθ)</text>
    <text x="{px+16:.1f}" y="{py+42:.1f}" class="formula">= cos θ + i sin θ</text>
    <text x="{px+16:.1f}" y="{cy-18}" class="formula">i sin θ</text>
  </g>
'''
    return svg(1120, 720, "Complex plane rotation", body)


def interference():
    body = f'''
  <rect width="1280" height="720" fill="url(#paper)"/>
  <text x="66" y="82" class="title">Interference Happens Before Measurement</text>
  <text x="70" y="126" class="small">Quantum paths carry amplitudes. Add the arrows first, then square the result.</text>
  <g filter="url(#softShadow)">
    <rect x="70" y="175" width="510" height="430" rx="24" fill="#fffdfa"/>
    <rect x="700" y="175" width="510" height="430" rx="24" fill="#fffdfa"/>
  </g>
  <text x="110" y="230" class="h2">Constructive</text>
  <text x="740" y="230" class="h2">Destructive</text>
  <g transform="translate(120 288)">
    {arrow(0, 0, 170, 0, TEAL, 9)}
    {arrow(0, 56, 170, 56, GOLD, 9)}
    {arrow(235, 28, 575, 28, CORAL, 11)}
    <text x="4" y="120" class="formula">A_total = A1 + A2</text>
    <text x="235" y="120" class="formula">P = |A_total|^2</text>
    <path d="{wave_path(0, 190, 390, 24, 3.2, 0)}" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <path d="{wave_path(0, 190, 390, 24, 3.2, 0)}" fill="none" stroke="{GOLD}" stroke-width="5" stroke-opacity="0.55" transform="translate(0 36)"/>
  </g>
  <g transform="translate(750 288)">
    {arrow(0, 0, 170, 0, TEAL, 9)}
    {arrow(172, 56, 2, 56, GOLD, 9)}
    <circle cx="280" cy="28" r="18" fill="{CORAL}"/>
    <text x="315" y="35" class="formula">0 amplitude</text>
    <text x="4" y="120" class="formula">A_total = A1 - A1 = 0</text>
    <text x="4" y="158" class="formula">P = |0|^2 = 0</text>
    <path d="{wave_path(0, 218, 390, 24, 3.2, 0)}" fill="none" stroke="{TEAL}" stroke-width="5"/>
    <path d="{wave_path(0, 218, 390, 24, 3.2, math.pi)}" fill="none" stroke="{GOLD}" stroke-width="5"/>
  </g>
'''
    return svg(1280, 720, "Amplitude interference diagram", body)


def born_rule():
    body = f'''
  <rect width="1280" height="720" fill="url(#paper)"/>
  <text x="66" y="82" class="title">The Born Rule: State to Counts</text>
  <text x="70" y="126" class="small">A qubit is not a hidden bit. It becomes a bit only when measured in a chosen basis.</text>
  <g filter="url(#softShadow)">
    <rect x="78" y="196" width="300" height="332" rx="24" fill="#fffdfa"/>
    <rect x="492" y="196" width="300" height="332" rx="24" fill="#fffdfa"/>
    <rect x="906" y="196" width="300" height="332" rx="24" fill="#fffdfa"/>
  </g>
  <text x="115" y="252" class="h2">State</text>
  <text x="529" y="252" class="h2">Square</text>
  <text x="943" y="252" class="h2">Sample</text>
  <text x="115" y="305" class="formula">|ψ&gt; =</text>
  <text x="115" y="344" class="formula">α|0&gt; + β|1&gt;</text>
  <text x="115" y="390" class="formula">α = 0.866</text>
  <text x="115" y="429" class="formula">β = 0.500 e^(iφ)</text>
  {arrow(392, 360, 466, 360, CORAL, 6)}
  {arrow(806, 360, 880, 360, CORAL, 6)}
  <text x="529" y="315" class="formula">P(0) = |α|^2</text>
  <text x="529" y="350" class="formula">= 0.75</text>
  <text x="529" y="398" class="formula">P(1) = |β|^2</text>
  <text x="529" y="433" class="formula">= 0.25</text>
  <rect x="958" y="270" width="76" height="180" fill="{TEAL}"/>
  <rect x="1076" y="390" width="76" height="60" fill="{GOLD}"/>
  <line x1="938" y1="450" x2="1178" y2="450" stroke="{INK}" stroke-width="3"/>
  <text x="981" y="487" class="label">0</text>
  <text x="1100" y="487" class="label">1</text>
  <text x="956" y="244" class="small">many repeated shots</text>
  <text x="958" y="256" class="small">75% / 25% pattern</text>
'''
    return svg(1280, 720, "Born rule from state to measured counts", body)


def project(cx, cy, scale, x, y, z):
    return cx + scale * (0.86 * x - 0.52 * y), cy + scale * (-0.94 * z + 0.22 * y)


def sphere(cx, cy, scale, vector, label, color):
    grid = []
    for k in range(-3, 4):
        grid.append(f'<ellipse cx="{cx}" cy="{cy + k * scale * 0.105:.1f}" rx="{scale:.1f}" ry="{scale * 0.32:.1f}" fill="none" stroke="{BLUE}" stroke-opacity="0.24" stroke-width="1.5"/>')
        grid.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{scale * 0.34:.1f}" ry="{scale:.1f}" fill="none" stroke="{BLUE}" stroke-opacity="0.18" stroke-width="1.5" transform="rotate({k*12} {cx} {cy})"/>')
    x2, y2 = project(cx, cy, scale * 0.9, *vector)
    return f'''
      <g>
        <circle cx="{cx}" cy="{cy}" r="{scale}" fill="#ecfbf7" stroke="{BLUE}" stroke-opacity="0.55" stroke-width="2"/>
        {''.join(grid)}
        {arrow(cx, cy, x2, y2, color, 6)}
        <circle cx="{x2:.1f}" cy="{y2:.1f}" r="7" fill="{color}"/>
        <text x="{cx - scale * 0.58:.1f}" y="{cy + scale + 34:.1f}" class="label">{label}</text>
      </g>
    '''


def bloch_sphere():
    states = [
        ((0, 0, 1), "|0&gt;", TEAL),
        ((0, 0, -1), "|1&gt;", CORAL),
        ((1, 0, 0), "|+&gt;", GOLD),
        ((-1, 0, 0), "|-&gt;", BLUE),
        ((0, 1, 0), "|+i&gt;", GREEN),
        ((0, -1, 0), "|-i&gt;", "#9b5de5"),
    ]
    panels = []
    positions = [(230, 250), (600, 250), (970, 250), (230, 520), (600, 520), (970, 520)]
    for (vec, label, color), (cx, cy) in zip(states, positions):
        panels.append(sphere(cx, cy, 108, vec, label, color))
    body = f'''
  <rect width="1200" height="760" fill="url(#paper)"/>
  <text x="62" y="74" class="title">The Bloch Sphere Reference States</text>
  <text x="66" y="116" class="small">One pure qubit is a direction. Measurement projects that direction onto an axis.</text>
  {''.join(panels)}
  <text x="80" y="704" class="formula">|ψ(θ,φ)&gt; = cos(θ/2)|0&gt; + e^(iφ) sin(θ/2)|1&gt;</text>
'''
    return svg(1200, 760, "Bloch sphere reference states", body)


def phase_probabilities():
    theta = math.radians(60)
    phis = [0, math.pi / 2, math.pi, 3 * math.pi / 2]
    series = {
        "Z basis": ([math.cos(theta / 2) ** 2 for _ in phis], [math.sin(theta / 2) ** 2 for _ in phis], "P(0)", "P(1)"),
        "X basis": ([(1 + math.sin(theta) * math.cos(p)) / 2 for p in phis], [(1 - math.sin(theta) * math.cos(p)) / 2 for p in phis], "P(+)", "P(-)"),
        "Y basis": ([(1 + math.sin(theta) * math.sin(p)) / 2 for p in phis], [(1 - math.sin(theta) * math.sin(p)) / 2 for p in phis], "P(+i)", "P(-i)"),
    }
    panels = []
    labels = ["0", "pi/2", "pi", "3pi/2"]
    for idx, (name, (a, b, la, lb)) in enumerate(series.items()):
        x0, y0, w, h = 98, 178 + idx * 170, 950, 105
        pa, pb = plot_points(a, x0, y0, w, h), plot_points(b, x0, y0, w, h)
        marks = []
        for i, lab in enumerate(labels):
            x = x0 + i * w / 3
            marks.append(f'<line x1="{x:.1f}" y1="{y0+h}" x2="{x:.1f}" y2="{y0+h+8}" stroke="{INK}" stroke-width="2"/><text x="{x-14:.1f}" y="{y0+h+31}" class="small">{lab}</text>')
        panels.append(f'''
    <text x="{x0}" y="{y0-22}" class="h2">{name}</text>
    <line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" class="axis"/>
    <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" class="axis"/>
    <polyline points="{polyline(pa)}" fill="none" stroke="{TEAL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    <polyline points="{polyline(pb)}" fill="none" stroke="{CORAL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    {"".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{TEAL}"/>' for x,y in pa)}
    {"".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{CORAL}"/>' for x,y in pb)}
    {"".join(marks)}
    <text x="{x0+w+28}" y="{y0+32}" class="label" fill="{TEAL}">{la}</text>
    <text x="{x0+w+28}" y="{y0+72}" class="label" fill="{CORAL}">{lb}</text>
''')
    body = f'''
  <rect width="1200" height="760" fill="url(#paper)"/>
  <text x="62" y="74" class="title">Same State, Three Measurement Bases</text>
  <text x="66" y="116" class="small">θ = 60 degrees. Z ignores phase; X and Y reveal it as interference.</text>
  <g filter="url(#softShadow)"><rect x="50" y="138" width="1100" height="558" rx="24" fill="#fffdfa" fill-opacity="0.88"/></g>
  {''.join(panels)}
  <text x="538" y="720" class="small">φ phase angle</text>
'''
    return svg(1200, 760, "Phase probabilities in Z X and Y bases", body)


def quantum_stack():
    rows = [
        ("Hardware", "Josephson junctions, trapped ions, spins, photons", TEAL),
        ("Control pulses", "microwave, laser, voltage, timing calibration", GOLD),
        ("Gates", "H, X, Y, Z, Rz, Rx, Ry, CNOT", CORAL),
        ("Circuits", "prepare, entangle, interfere, measure", BLUE),
        ("Algorithms", "simulation, search, phase estimation, sampling", GREEN),
        ("Applications", "chemistry, materials, optimization, sensing", "#9b5de5"),
    ]
    blocks = []
    for i, (name, desc, color) in enumerate(rows):
        y = 150 + i * 82
        blocks.append(f'''
  <g filter="url(#softShadow)">
    <rect x="{100+i*34}" y="{y}" width="{820-i*20}" height="58" rx="16" fill="#fffdfa"/>
  </g>
  <circle cx="{132+i*34}" cy="{y+29}" r="12" fill="{color}"/>
  <text x="{158+i*34}" y="{y+24}" class="label">{name}</text>
  <text x="{158+i*34}" y="{y+48}" class="small">{desc}</text>
''')
    body = f'''
  <rect width="1120" height="720" fill="url(#paper)"/>
  <text x="62" y="80" class="title">Where The Math Touches Machines</text>
  <text x="66" y="124" class="small">Quantum software is a control stack: abstract vectors become physical rotations and readout events.</text>
  {''.join(blocks)}
  <path d="M 966 164 C 1065 240, 1065 516, 928 612" fill="none" stroke="{CORAL}" stroke-width="5" stroke-linecap="round" stroke-dasharray="10 12"/>
  <text x="802" y="646" class="formula">calibrate -> compose -> measure -> learn</text>
'''
    return svg(1120, 720, "Quantum computing stack", body)


FIGURES = {
    "cover-quantum-engineering.svg": cover,
    "complex-plane-rotation.svg": complex_plane,
    "amplitude-interference.svg": interference,
    "born-rule-pipeline.svg": born_rule,
    "bloch-sphere-states.svg": bloch_sphere,
    "phase-basis-probabilities.svg": phase_probabilities,
    "quantum-stack.svg": quantum_stack,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="quantum_book/assets/figures", help="Directory for generated SVG files")
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, build in FIGURES.items():
        path = out / name
        path.write_text(build(), encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
