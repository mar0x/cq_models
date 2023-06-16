import cadquery as cq

spool = cq.Workplane("XY") \
    .rect(60, 28) \
    .extrude(2) \
    .edges("|Z").fillet(3) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .rect(50, 18) \
        .extrude(6) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .rect(46, 14) \
        .cutBlind(-6) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(5) \

if __name__ == '__cqgi__':
    show_object(spool)
