import cadquery as cq

base_width = 37.7
base_length = 89.9
base_r = 6
base_height = 1

sensor_base_width = 28.9
sensor_base_length = 74.7
sensor_base_r = 5

sensor_width = 28.1
sensor_length = 72.1
sensor_r = 5
sensor_height = 13

sensor_hole_width = 5
sensor_hole_length = 58

clearance = 0.2
cover_thickness = 2
cover_width = base_width + 2 * (cover_thickness + clearance)
cover_length = base_length + 2 * (cover_thickness + clearance)
cover_r = base_r + cover_thickness + clearance
cover_height = 12

hole_step_x = 85.9 - 3.5
hole_step_y = 15.7 - 3.5

sensor = cq.Workplane("XY") \
    .moveTo(0, base_width / 2) \
    .hLine(base_length / 2 - base_r) \
    .radiusArc((base_length / 2, base_width / 2 - base_r), base_r) \
    .vLine(-base_width + base_r * 2) \
    .radiusArc((base_length / 2 - base_r, -base_width / 2), base_r) \
    .hLine(-base_length / 2 + base_r) \
    .mirrorY() \
    .extrude(base_height) \
    .union(
        cq.Workplane("XY") \
            .moveTo(0, sensor_base_width / 2) \
            .hLine(sensor_base_length / 2 - sensor_base_r) \
            .radiusArc((sensor_base_length / 2, sensor_base_width / 2 - sensor_base_r), sensor_base_r) \
            .vLine(-sensor_base_width + sensor_base_r * 2) \
            .radiusArc((sensor_base_length / 2 - sensor_base_r, -sensor_base_width / 2), sensor_base_r) \
            .hLine(-sensor_base_length / 2 + sensor_base_r) \
            .hLine(-sensor_base_length / 2 + sensor_base_r) \
            .radiusArc((-sensor_base_length / 2, -sensor_base_width / 2 + sensor_base_r), sensor_base_r) \
            .vLine(sensor_base_width - sensor_base_r * 2) \
            .radiusArc((-sensor_base_length / 2 + sensor_base_r, sensor_base_width / 2), sensor_base_r) \
            .close() \
            .workplane(offset=sensor_height) \
                .moveTo(0, sensor_width / 2) \
                .hLine(sensor_length / 2 - sensor_r) \
                .radiusArc((sensor_length / 2, sensor_width / 2 - sensor_r), sensor_r) \
                .vLine(-sensor_width + sensor_r * 2) \
                .radiusArc((sensor_length / 2 - sensor_r, -sensor_width / 2), sensor_r) \
                .hLine(-sensor_length / 2 + sensor_r) \
                .hLine(-sensor_length / 2 + sensor_r) \
                .radiusArc((-sensor_length / 2, -sensor_width / 2 + sensor_r), sensor_r) \
                .vLine(sensor_width - sensor_r * 2) \
                .radiusArc((-sensor_length / 2 + sensor_r, sensor_width / 2), sensor_r) \
                .close() \
            .loft(combine=True) \
            .translate((0, 0, base_height)) \
            .faces(">Z").fillet(2)
    )

cover = cq.Workplane("XY") \
    .rect(cover_length, cover_width) \
    .extrude(cover_height) \
    .edges("|Z").fillet(cover_r) \
    .faces("<Z").shell(-cover_thickness) \
    .faces(">Z").fillet(1) \
    .faces("<Z[-2]").workplane(centerOption="CenterOfBoundBox") \
        .rarray(hole_step_x, 1, 2, 1) \
        .circle(4) \
        .extrude(3) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .rarray(hole_step_x, 1, 2, 1) \
        .hole(2) \
    .translate((0, 0, -4)) \
    .cut(sensor) \
    .cut(
        sensor \
        .translate((0, 0, 0)) \
        .faces("<Z").shell(clearance - 0.01)
    )

sensor_hole = cq.Workplane("XY") \
    .rect(sensor_hole_length, sensor_hole_width) \
    .extrude(10) \
    .edges("|Z").fillet(2.495) \
    .translate((0, 0, sensor_height + base_height - 2))

sensor_shim = cq.Workplane("XY") \
    .rect(sensor_hole_length + 1, 21) \
    .extrude(1) \
    .translate((0, 0, sensor_height + base_height - 2))

sensor = sensor \
    .cut( sensor_hole.translate((0, (10 + sensor_hole_width) / 2, 0)) ) \
    .cut( sensor_hole.translate((0, -(10 + sensor_hole_width) / 2, 0)) ) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .rarray(hole_step_x, hole_step_y, 2, 3) \
        .hole(3.5) \


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
    show_object(sensor)
    show_object(sensor_shim)
    show_object(cover)
