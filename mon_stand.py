import cadquery as cq

cb1 = cq.Workplane("XY") \
    .rect(20, 14) \
    .extrude(10) \
    .translate((0, 0, 20))

s = cq.Workplane("XY") \
    .rect(20, 18) \
    .extrude(27) \
    .edges("|Z").fillet(2) \

cb2 = cq.Workplane("XY") \
    .rect(20, 13) \
    .extrude(10) \

s2 = s.translate((0, 0, -20)) \
    .cut(cb2) \
    .cut(cb2.translate((0, 0, 4.5)).rotate((0, 0, 0), (0, 0, 1), 90)) \


s = s.cut(cb1) \
      .cut(cb1.translate((0, 0, 5)).rotate((0, 0, 0), (0, 0, 1), 90)) \
      .cut(s2) \


if __name__ == '__cqgi__':
    show_object(s)

