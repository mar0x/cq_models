import cadquery as cq

bridge = cq.Workplane("XY") \
    .moveTo(0, 13) \
    .hLine(73 / 2 + 10) \
    .radiusArc(((138 - 28) / 2, 5), -70) \
    .vLine(-5) \
    .hLine(-(32.5 - 14) - (73 - 60) / 2) \
    .radiusArc((0, 9), -50) \
    .mirrorY() \
    .extrude(15) \
    .edges("|Z and >Y").fillet(6) \
    .edges("|Z and (>X or <X)").fillet(2.49) \
    .cut(
        cq.Workplane("XZ") \
        .center(0, 15 / 2) \
        .rarray(73, 1, 2, 1, True) \
        .circle(6.6 / 2) \
        .extrude(-13)
    )

#    .edges("|Z and >Y").fillet(6) \
#    .edges("|Z and (>X or <X)").fillet(2.95) \
#    .line(32.5 - 12, 5 - 13) \

body_color = (133, 133, 133, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

if __name__ == '__cqgi__':
    show_object(bridge)
