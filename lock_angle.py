import cadquery as cq

la = cq.Workplane("XY") \
    .rect(20, 20) \
    .extrude(6) \
    .edges("|Z").fillet(2) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .rarray(10, 10, 2, 2) \
        .cskHole(4, 7, 82) \
    .cut(
        cq.Workplane("XY") \
            .rect(10, 10) \
            .extrude(6) \
            .translate((5, 5, 0))
    )

if __name__ == '__cqgi__':
    show_object(la)

