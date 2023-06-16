import cadquery as cq

bridge = cq.Workplane("XY") \
    .moveTo(0, 9) \
    .hLine(73.5 / 2 + 6.5) \
    .radiusArc((110 / 2, 4), -40) \
    .vLine(-4) \
    .hLine((60 - 110) / 2) \
    .radiusArc((0, 5), -92.5) \
    .mirrorY() \
    .extrude(15) \
    .edges("|Z and >Y").fillet(6) \
    .edges("|Z and (>X or <X)").fillet(2.19) \
    .cut(
        cq.Workplane("XZ") \
        .center(0, 15 / 2) \
        .rarray(73.5, 1, 2, 1, True) \
        .circle(3.5 / 2) \
        .extrude(-9)
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
