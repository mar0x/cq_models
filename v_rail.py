import cadquery as cq

w = 21.21 - 0.5
w2 = 15.67 - 0.5
h = 2.74
h2 = 2 * 4.17 - h - 0.5
h3 = 9.32 - h2 - 0.5

w4 = 19
h4 = 15

v_rail = cq.Workplane("XY") \
    .rect(w, h2) \
    .extrude(100) \
    .edges("|Z") \
    .chamfer(2.5) \
    .union(
        cq.Workplane("XY") \
        .center(0, h2 / 2 + h3 / 2) \
        .rect(w2, h3) \
        .extrude(100)
    ) \
    .union(
        cq.Workplane("XY") \
        .center(0, h2 / 2 + h3 + h4 / 2) \
        .rect(w4 + 4, h4) \
        .extrude(100) \
        .edges("|Z") \
        .chamfer(1) \
    ) \
    .cut(
        cq.Workplane("XY") \
        .center(0, h2 / 2 + h3 + h4 / 2 + 2) \
        .rect(w4, h4) \
        .extrude(100) \
        .edges("|Z") \
        .chamfer(0.5) \
    ) \
    .cut(
        cq.Workplane("XY") \
        .center(0, -h2 / 2 + 1) \
        .rect(9, 2) \
        .extrude(100) \
    )

if __name__ == '__cqgi__':
    show_object(v_rail)
