import cadquery as cq

class servo:
    body_length = 23.5
    ear_length = 4.8
    total_length = body_length + 2 * ear_length
    width = 12
    shaft_offset = body_length / 2 - 6
    clearance = 0.2

class servo_arm2:
    clearance = 0.1
    thickness = 2.5 + 0.2
    r1 = 11.2 / 2
    r2 = 2.5
    length = 39.2
    width = 7.9
    wlen = 18.5

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .circle(c.r1 + c.clearance) \
            .extrude(c.thickness) \
            .union(
                cq.Workplane("XY") \
                .moveTo(c.width / 2 + c.clearance, 0) \
                .lineTo(c.width / 2 + c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(c.r2 + c.clearance, - c.length / 2 + c.r2 - c.clearance) \
                .radiusArc((-c.r2 - c.clearance, -c.length / 2 + c.r2 - c.clearance), c.r2 + c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, - c.wlen / 2 - c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, 0) \
                .mirrorX() \
                .extrude(c.thickness)
            ) \
            .union(
                cq.Workplane("XY") \
                .circle(8.6 / 2 + c.clearance) \
                .extrude(6) \
                .translate((0, 0, -0.5)) \
                .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
                .hole(5.8 - c.clearance, 1.5)
            )

class servo_one_arm:
    clearance = 0.1
    thickness = 1.3 + 0.2
    r1 = 7 / 2
    r2 = 4.2 / 2
    length = 19.7
    width = 6.3

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .circle(c.r1 + c.clearance) \
            .extrude(3.8 + c.clearance) \
            .union(
                cq.Workplane("XY") \
                .moveTo(c.width / 2 + c.clearance, 0) \
                .lineTo(c.r2 + c.clearance, - c.length + c.r1 + c.r2 - c.clearance) \
                .radiusArc((-c.r2 - c.clearance, -c.length + c.r1 + c.r2 - c.clearance), c.r2 + c.clearance) \
                .lineTo(-c.width / 2 - c.clearance, 0) \
                .close() \
                .extrude(c.thickness)
            )

class servo_arm:
    clearance = 0.1
    thickness = 2.4 + 0.2
    r1 = 7 / 2
    r2 = 4.2 / 2
    r3 = 4 / 2
    length1 = 20
    length2 = 22
    length3 = 16.7 / 2
    width1 = 6
    width2 = 7
    width3 = 4

    @classmethod
    def create(c, cq):
        return cq.Workplane("XY") \
            .circle(c.r1 + c.clearance) \
            .extrude(6 + c.clearance) \
            .union(
                cq.Workplane("XY") \
                .moveTo(c.width1 / 2 + c.clearance, -c.width3 / 2 - c.clearance) \
                .lineTo(c.r2 + c.clearance, - c.length1 + c.r1 + c.r2 - c.clearance) \
                .radiusArc((-c.r2 - c.clearance, -c.length1 + c.r1 + c.r2 - c.clearance), c.r2 + c.clearance) \
                .lineTo(-c.width1 / 2 - c.clearance, -c.width3 / 2 - c.clearance) \
                .lineTo(-c.length3 + c.r3 - c.clearance, -c.width3 / 2 - c.clearance) \
                .radiusArc((-c.length3 + c.r3 - c.clearance, c.width3 / 2 + c.clearance), c.r3 + c.clearance) \
                .lineTo(-c.width2 / 2 - c.clearance, c.width3 / 2 + c.clearance) \
                .lineTo(-c.r2 - c.clearance, c.length2 - c.r1 - c.r2 + c.clearance) \
                .radiusArc((c.r2 + c.clearance, c.length2 - c.r1 - c.r2 + c.clearance), c.r2 + c.clearance) \
                .lineTo(c.width2 / 2 + c.clearance, c.width3 / 2 + c.clearance) \
                .lineTo(c.length3 - c.r3 + c.clearance, c.width3 / 2 + c.clearance) \
                .radiusArc((c.length3 - c.r3 + c.clearance, -c.width3 / 2 - c.clearance), c.r3 + c.clearance) \
                .close() \
                .extrude(c.thickness)
            ) \
            .rotate((0, 0, 0), (0, 0, 1), -90)

base_r = 30

base = cq.Workplane("XY") \
    .circle(base_r) \
    .extrude(1) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
    .circle(base_r) \
    .workplane(offset=4.4) \
    .circle(10) \
    .loft(combine=True) \
    .cut(servo_arm.create(cq))

pan_length = 2 * (servo.total_length / 2 + servo.shaft_offset + 4)
pan_width = 2 * 4 + servo.width
pan_thickness = 4

pan_stand = cq.Workplane("XY") \
    .rect(pan_length, pan_width) \
    .extrude(pan_thickness) \
    .edges("|Z").fillet(2) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .center(servo.shaft_offset, 0) \
        .rect(servo.total_length + 2 * servo.clearance, servo.width + 2 * servo.clearance) \
        .cutBlind(-2) \
    .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
        .center(servo.shaft_offset, 0) \
        .rect(servo.body_length + 2 * servo.clearance, servo.width + 2 * servo.clearance) \
        .cutBlind(-2) \

tilt_arm_width = pan_width - 2
tilt_arm_thickness = 3

tilt_arm = cq.Workplane("YZ") \
    .moveTo(-tilt_arm_width / 2, pan_thickness) \
    .radiusArc((25 + servo.width / 2, 18 + tilt_arm_width / 2), 25 + servo.width / 2 + tilt_arm_width / 2) \
    .radiusArc((25 + servo.width / 2, 18 - tilt_arm_width / 2), tilt_arm_width / 2 + 0.1) \
    .radiusArc((tilt_arm_width / 2, pan_thickness), -(25 + servo.width / 2 - tilt_arm_width / 2)) \
    .hLine(-6) \
    .line(2, -pan_thickness) \
    .hLine(-tilt_arm_width + 2 * 4) \
    .line(2, pan_thickness) \
    .close() \
    .extrude(tilt_arm_thickness) \

arm_bounds_width = 25 + servo.width / 2 + tilt_arm_width
arm_bounds_height = 18 + tilt_arm_width / 2
arm_hole_x = arm_bounds_width / 2 - tilt_arm_width / 2 + 0.8
arm_hole_y = arm_bounds_height / 2 - tilt_arm_width / 2

tilt_left_arm = tilt_arm.translate((-pan_length / 2, 0, 0)) \
    .faces(">X").workplane(centerOption="CenterOfBoundBox") \
        .center(arm_hole_x, arm_hole_y) \
        .hole(3.5) \
    .faces("<X").workplane(centerOption="CenterOfBoundBox") \
        .center(-arm_hole_x, arm_hole_y) \
        .hole(10.2, 2) \
    .faces("<X").workplane(centerOption="CenterOfBoundBox") \
        .center(9, -2) \
        .hole(tilt_arm_width - 6, 2) \
    .faces("<X").workplane(centerOption="CenterOfBoundBox") \
        .center(-3, 4) \
        .hole(tilt_arm_width - 6, 2) \

tilt_right_arm = tilt_arm.translate((pan_length / 2 - tilt_arm_thickness, 0, 0)) \
    .faces(">X").workplane(centerOption="CenterOfBoundBox") \
        .center(-9, -2) \
        .hole(tilt_arm_width - 6, 2) \
    .cut(
        servo_one_arm.create(cq) \
            .rotate((0, 0, 0), (0, 1, 0), -90) \
            .translate((pan_length / 2, 25 + servo.width / 2, 18))
    )

pan_stand = pan_stand.cut(tilt_left_arm).cut(tilt_right_arm)

tilt_pad_length = pan_length - 2 * (tilt_arm_thickness + 2)
tilt_pad_height = servo.total_length + 2 * 2
tilt_ear_mount_height = (tilt_pad_height - servo.body_length - 0.1) / 2

tilt_pad = cq.Workplane("XZ") \
    .rect(tilt_pad_length, tilt_pad_height) \
    .extrude(-2) \
    .edges("|Y").fillet(2) \
    .translate((0, servo.width / 2, -servo.shaft_offset)) \
    .faces(">Y").workplane(centerOption="CenterOfBoundBox") \
        .rarray(11 * 2.54, 11 * 2.54, 2, 2) \
        .hole(1.5) \
    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
        .center(tilt_pad_length / 2 - 8.4 - 2.6 / 2, 0) \
        .rarray(3 + 3, servo.body_length + tilt_ear_mount_height + 0.1, 2, 2) \
        .rect(3, tilt_ear_mount_height) \
        .extrude(servo.width) \
    .faces(">Y[-1]").workplane(centerOption="CenterOfBoundBox") \
        .center(tilt_pad_length / 2 - 3 / 2, 0) \
        .rect(3, servo.shaft_offset * 2 + 2 * 4) \
        .extrude(-servo.width - 2) \
    .faces("<X").workplane(centerOption="CenterOfBoundBox") \
        .center(1, 0) \
        .rarray(1, servo.shaft_offset * 2, 1, 2) \
        .hole(3.1, 3) \
    .edges("<Y and |X").fillet(3) \

#    .rotate((0, 0, 0), (1, 0, 0), -65) \

#    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
#        .rarray(13, 23, 4, 2) \
#        .hole(12, 1) \
#    .faces("<Y").workplane(centerOption="CenterOfBoundBox") \
#        .rarray(13, 23, 5, 3) \
#        .hole(12, 1) \

pan_z = 5 + 10.65

if __name__ == '__cqgi__':
    show_object(base)
    show_object(pan_stand.translate((0, 0, pan_z)))
    show_object(tilt_right_arm.translate((4, 0, pan_z)))
    show_object(tilt_left_arm.translate((-4, 0, pan_z)))
    show_object(tilt_pad.translate((0, servo.width / 2 + 25, pan_z + 18)))
