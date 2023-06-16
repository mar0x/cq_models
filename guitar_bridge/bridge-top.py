import cadquery as cq

r = ((86 / 2) ** 2 + (9 - 5.4) ** 2) / (2 * (9 - 5.4))

bridge_top = cq.Workplane("XY") \
    .moveTo(-86 / 2, 0) \
    .vLine(5.4) \
    .radiusArc((86 / 2, 5.4), r) \
    .vLine(-5.4) \
    .close() \
    .extrude(15) \
    .edges("|Y").fillet(7.499) \
    .translate((0, 0, -15 / 2)) \
    .cut(
        cq.Workplane("XZ") \
        .rarray(1, 3.4, 1, 4) \
        .rect(62, 2) \
        .extrude(-5) \
        .translate((0, 4, 0))
    ) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .rarray(73.5, 1, 2, 1) \
        .hole(3.5)

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
    ) \
    .translate((0, -10, -15 / 2)) \


#    .cut(
#        cq.Workplane("XZ") \
#        .center(0, 15 / 2) \
#        .rarray(73.5, 1, 2, 1, True) \
#        .circle(3.5 / 2) \
#        .extrude(-9)
#    )

#    .edges("|Z and >Y").fillet(6) \
#    .edges("|Z and (>X or <X)").fillet(2.95) \
#    .line(32.5 - 12, 5 - 13) \

body_color = (133, 133, 133, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

if __name__ == '__cqgi__':
    show_object(bridge)
    show_object(bridge_top)
