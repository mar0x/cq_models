import cadquery as cq
import math

rg = 184.2
cy = (rg ** 2 - (60 / 2) ** 2) ** 0.5
py = ((rg + 10) ** 2 - (20 / 2) ** 2) ** 0.5
tk = (rg + 10) / rg

py2 = ((rg + 10) ** 2 - (50 / 2) ** 2) ** 0.5

r = cq.Workplane("XY") \
        .moveTo(-50 / 2, py2 - cy) \
        .radiusArc((0, py - cy + 9 + 10), 26) \
        .radiusArc((50 / 2, py2 - cy), 26) \
        .close() \
        .extrude(5)

t = cq.Workplane("XY") \
    .moveTo(-60 / 2, 0) \
    .radiusArc((-tk * 60 / 2, cy * (tk - 1)), 5.01) \
    .radiusArc((-20 / 2, py - cy), rg + 10) \
    .vLine(20).hLine(20).vLine(-20) \
    .radiusArc((tk * 60 / 2, cy * (tk - 1)), rg + 10) \
    .radiusArc((60 / 2, 0), 5.01) \
    .radiusArc((-60 / 2, 0), -rg) \
    .close() \
    .extrude(150 + 5) \
    .union(
        r.translate((0, 0, 0))
    ) \
    .union(
        r.translate((0, 0, 50))
    ) \
    .union(
        r.translate((0, 0, 100))
    ) \
    .union(
        r.translate((0, 0, 150))
    ) \

t2 = cq.Workplane("XY") \
    .moveTo(-60 / 2, 0) \
    .radiusArc((-tk * 60 / 2, cy * (tk - 1)), 5.01) \
    .radiusArc((-20 / 2, py - cy), rg + 10) \
    .vLine(20).hLine(20).vLine(-20) \
    .radiusArc((tk * 60 / 2, cy * (tk - 1)), rg + 10) \
    .radiusArc((60 / 2, 0), 5.01) \
    .radiusArc((-60 / 2, 0), -rg) \
    .close() \
    .extrude(2) \
    .translate((0, 0, -10))

tk2 = (rg - 0.1) / rg
tk3 = (rg + 10.1) / rg

py3 = ((rg + 10.1) ** 2 - (52 / 2) ** 2) ** 0.5
tk4 = (rg + 10.1 + 5) / (rg + 10.1)
tk5 = (rg - 5 - 0.1) / rg

a = math.asin(60 / 2 / rg) * 180 / math.pi
h = cq.Workplane("YZ") \
    .circle(4 / 2) \
    .extrude(20) \
    .translate((-20 / 2, -cy + rg + 10 / 2, 0)) \
    .translate((0, cy, 0)) \
    .rotate((0, 0, 0), (0, 0, 1), -a) \
    .translate((0, -cy, 0)) \

t3 = cq.Workplane("XY") \
    .moveTo(tk2 * 60 / 2, cy * (tk2 - 1)) \
    .radiusArc((tk3 * 60 / 2, cy * (tk3 - 1)), -5.1 - 0.01) \
    .radiusArc((52 / 2, py3 - cy), rg + 10.1) \
    .lineTo(tk4 * 52 / 2, tk4 * py3 - cy) \
    .radiusArc((tk4 * tk3 * 60 / 2, cy * (tk4 * tk3 - 1)), rg + 10.1 + 5) \
    .radiusArc((tk5 * 60 / 2, cy * (tk5 - 1)), 5.1 + 5 + 0.01) \
    .close() \
    .extrude(150 + 5) \
    .cut(
        cq.Workplane("XY") \
        .rect(5, 12) \
        .extrude(150 + 5) \
        .translate((-5 / 2, -12 / 2, 0)) \
        .rotate((0, 0, 0), (0, 0, 1), 35) \
        .translate((tk2 * 60 / 2, cy * (tk2 - 1), 0))
    ) \
    .union(
        cq.Workplane("XY") \
        .rect(5, 12 - 3) \
        .extrude(150 + 5) \
        .edges("|Z").fillet(1) \
        .translate((5 / 2, -(12 + 3)/ 2, 0)) \
        .rotate((0, 0, 0), (0, 0, 1), 35) \
        .translate((tk2 * 60 / 2, cy * (tk2 - 1), 0))
    ) \
    .cut(
        h.translate((0, 0, 5))
    ) \
    .cut(
        h.translate((0, 0, 50 + 5 / 2))
    ) \
    .cut(
        h.translate((0, 0, 100 + 5 / 2))
    ) \
    .cut(
        h.translate((0, 0, 150))
    )

if __name__ == '__cqgi__':
    show_object(t)
    show_object(t2)
    show_object(t3)
