import cadquery as cq

th = 7

mm = cq.Workplane("XY") \
    .rect(60, 85) \
    .extrude(th) \
    .edges("|Z").fillet(7) \
    .faces(">Z").fillet(1) \
    .faces("<Z").fillet(1) \
    .translate((0, 7.5, 0)) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .center(0, -7.5) \
        .rect(28, 22) \
        .workplane(offset = 9) \
        .circle(20 / 2) \
        .loft(combine=True) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(16, 5) \
    .faces(">Z").fillet(0.5) \
    .cut(
        cq.Workplane("XY") \
          .rect(11, 11) \
          .extrude(2) \
        .edges("|Z").fillet(0.6) \
        .translate((0, 0, th + 2))
    ) \
    .union(
        cq.Workplane("XY") \
          .rect(7, 7) \
          .extrude(5) \
        .edges("|Z").fillet(1) \
        .translate((0, 0, th + 2))
    ) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .center(0, 7.5) \
        .hole(3.5) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .center(0, 7.5) \
        .hole(10, 3) \
    .union(
        cq.Workplane("XY") \
          .rarray(16, 1, 2, 1) \
          .circle(1) \
          .extrude(5) \
        .translate((0, 0, th + 2))
    )

if __name__ == '__cqgi__':
    show_object(mm)

