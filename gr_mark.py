import cadquery as cq

m = cq.Workplane("XY") \
    .circle(6.2 / 2) \
    .extrude(40) \
    .faces("<Z").chamfer(0.2)

if __name__ == '__cqgi__':
    show_object(m)
