import cadquery as cq

sd_card_width = 10 + 0.1
sd_holder_width = 14 + 0.1
sd_holder_thickness = 2 + 0.1

lock_width = 24
lock_height = 7
lock_thickness = 1.5 + sd_holder_thickness + 1

hole_distance = 20
hole_d = 2.5


lock = cq.Workplane("XY") \
    .rect(lock_width, lock_height) \
    .extrude(lock_thickness) \
    .edges("|Z").fillet(1) \
    .cut(
        cq.Workplane("XY") \
        .rect(lock_width, lock_height) \
        .extrude(1.5) \
        .edges("|Z").fillet(1) \
        .translate((0, -1.5, 0))
    ) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
    .rarray(hole_distance, 1, 2, 1) \
    .hole(hole_d) \
    .cut(
        cq.Workplane("XY") \
        .rect(sd_holder_width, lock_height) \
        .extrude(sd_holder_thickness) \
        .translate((0, -1.5, 1.5))
    )

if __name__ == '__cqgi__':
    show_object(lock)
