import cadquery as cq

sp_hole = cq.Workplane("XY") \
    .rect(70, 70) \
    .extrude(50) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(52)

spindle = cq.Workplane("XZ") \
    .circle(52 / 2) \
    .extrude(80) \
    .translate((0, 80/2, 52 / 2 + 10))

sunk1 = cq.Workplane("YZ") \
    .rarray(30, 52 + 6, 2, 2) \
    .rect(12, 12) \
    .extrude(4) \
    .edges("|X").fillet(3) \
    .translate((-35, 0, (10 + 52 + 5) / 2 + 2.5))

sunk2 = cq.Workplane("YZ") \
    .rarray(30, 52 + 6, 2, 2) \
    .circle(19 / 2) \
    .extrude(2) \
    .translate((-35, 0, (10 + 52 + 5) / 2 + 2.5))

sunk = cq.Workplane("YZ") \
    .rarray(30, 52 + 6, 2, 2) \
    .polygon(6, 10.1 * 2 / (3 ** 0.5)) \
    .extrude(4) \
    .edges("|X").fillet(0.5) \
    .translate((-35, 0, (10 + 52 + 5) / 2 + 2.5))

handle = cq.Workplane("XY") \
    .rect(70, 52) \
    .extrude(10 + 52 + 5 + 40) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .hole(52 - 4 - 4, 30) \
    .cut(
        sp_hole.translate((0, 0, 10 + 52 + 5))
    ) \
    .edges("|Y").fillet(3) \
    .faces("<X").workplane(centerOption="CenterOfBoundBox") \
        .center(0, 2.5) \
        .rarray(30, 52 + 6, 2, 2) \
        .hole(6) \
    .cut(spindle) \
    .cut(
        cq.Workplane("XY") \
        .rect(0.5, 60) \
        .extrude(10 + 52 + 5 + 40)
    ) \
    .cut(sunk) \
    .cut(sunk2.rotate((0, 0, 0), (0, 0, 1), 180)) \

hc = cq.Workplane("YZ") \
    .rect(52, 10 + 52 + 5 + 40) \
    .extrude(70 / 2) \
    .translate((0, 0, (10 + 52 + 5 + 40) / 2))

handle1 = handle.translate((0, 0, 0)).cut(hc)

handle2 = handle.translate((0, 0, 0)).cut(hc.translate((-70 / 2, 0, 0)))

body_color = (133, 133, 133, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

chrome_color = {
    "ambient": (89, 89, 89, 0),
    "diffuse": (233, 233, 233, 0),
    "emissive": (0, 0, 0, 0),
    "specular": (248, 248, 248, 0),
    "shininess": 10,
}

shiny_plastic = {
    "ambient": (22, 22, 22, 0),
    "diffuse": (179, 179, 179, 0),
    "emissive": (0, 0, 0, 0),
    "specular": (255, 255, 255, 0),
    "shininess": 99,
}

if __name__ == '__cqgi__':
    show_object(handle1)
    show_object(handle2)
