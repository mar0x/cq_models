import cadquery as cq

c = cq.Workplane("XY") \
    .rect(0.5, 10) \
    .extrude(58) \
    .translate((0.5 / 5 - 5, 0, 0))

c2 = c.rotate((0, 0, 0), (0, 0, 1), 90)

c = c.union(c2).rotate((0, 0, 0), (0, 0, 1), 45)

h = cq.Workplane("XY") \
    .circle(5 / 2) \
    .extrude(58) \
    .translate((0, 19/2 + 7/2, 0))

ba = cq.Workplane("XY") \
    .circle(33/2) \
    .extrude(58) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(19) \
    .faces(">Z").fillet(0.5) \
    .faces("<Z").fillet(0.5) \
    .cut(c.translate((19/2 + 7/2, 0, 0))) \
    .cut(c.rotate((0, 0, 0), (0, 0, 1), 180).translate((-19/2 - 7/2, 0, 0))) \
    .cut(h) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), 25)) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), 50)) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), -25)) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), -50)) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), -75)) \
    .cut(h.rotate((0, 0, 0), (0, 0, 1), -100)) \

if __name__ == '__cqgi__':
    show_object(ba)

