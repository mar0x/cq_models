import cadquery as cq

d = 27

tube_ring = cq.Workplane("XY") \
    .circle(d / 2 + 2) \
    .circle(d / 2) \
    .extrude(5)

if __name__ == '__cqgi__':
    show_object(tube_ring)
