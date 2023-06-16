import cadquery as cq

m1 = cq.Workplane("XY") \
    .circle(10 / 2) \
    .extrude(4.5) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(7.7)

m2 = cq.Workplane("XY") \
    .circle(10 / 2) \
    .extrude(5.5) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(7.7) \
    .translate((12, 0, 0))

if __name__ == '__cqgi__':
    show_object(m1)
    show_object(m2)
