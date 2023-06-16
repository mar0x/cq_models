# This is a CadQuery script template
# Add your script code below
import cadquery as cq
import math

Rout = 35 / 2
Rin = 31 / 2
#Rout = 93 / 2
#Rin = 90.6 / 2
h = 120
x0 = (h ** 2 - Rout ** 2) / (2 * Rout)
th = 1.6
cam_rotate_angle = -45
base_height = 40
base_width = 3

shield_r = 18
shield_h = 25
shield_x0 = (shield_h ** 2 - shield_r ** 2) / (2 * shield_r)

# make the shield cone
shield_cone = cq.Workplane("YZ") \
      .vLine(shield_h) \
      .radiusArc((shield_r, 0), shield_x0 + shield_r) \
      .close() \
      .revolve() \
      .faces("<Z") \
      .shell(3)

# make the cone
cone = cq.Workplane("YZ") \
      .vLine(h) \
      .radiusArc((Rout, 0), x0 + Rout) \
      .line(Rin - Rout, Rin - Rout) \
      .vLine(-base_height + Rout - Rin) \
      .hLine(-Rin) \
      .close() \
      .revolve()

inner_cone = cq.Workplane("YZ") \
      .vLine(h - th) \
      .radiusArc((Rout - th, th), x0 + Rout - th) \
      .hLine(Rin - Rout - base_width + th) \
      .vLine(-base_height + 1) \
      .hLine(-Rin + base_width) \
      .close() \
      .revolve()

inner_edge = cq.Workplane("XY") \
      .rect(th, Rout).extrude(h + 20) \
      .translate((0, Rout / 2, -20))

#cone = cone.union(shield_cone.translate((0, Rout - 8, 10)))

#cone = cone.faces("<Z") \
#      .workplane(centerOption="CenterOfBoundBox") \
#      .hole(Rin * 2 - 10, 3)

cone = cone.faces("<Z").fillet(2)

cam = cq.Workplane("XY") \
      .rect(16, 30) \
      .extrude(16)

cam_shell = cam.translate((0, 0, 0)).faces(">Z").shell(th)

cam = cam.rotate((0, 0, 0), (1, 0, 0), cam_rotate_angle)
cam_shell = cam_shell.rotate((0, 0, 0), (1, 0, 0), cam_rotate_angle)

cam = cam.translate((0, Rout - 10, 5))
cam_shell = cam_shell.translate((0, Rout - 10, 5)) \
      .intersect(inner_cone)

insight = cq.Workplane("XY") \
      .rect(2, 22) \
      .extrude(101) \
      .translate((0, 0, -37))

insight_shell_cut = cq.Workplane("XY") \
      .rect(2 + 2*2, 22 - 2*2) \
      .extrude(101 - 2*2) \
      .edges("|X").fillet(2) \
      .translate((0, 0, -37 + 2))

insight_shell = cq.Workplane("XY") \
      .rect(2 + 2*2, 22 + 2*2) \
      .extrude(101 + 2*2) \
      .edges("|X").fillet(4) \
      .translate((0, 0, -37 - 2)) \
      .cut(insight_shell_cut) \
      .cut(insight) \
      .intersect(cone)

bat = cq.Workplane("XY") \
      .rect(4.5, 13) \
      .extrude(31) \
      .translate((0, 0, 2))

bat_shell_cut = cq.Workplane("XY") \
      .rect(4.5 + 2*1, 13 - 2*2) \
      .extrude(31 - 2*2) \
      .edges("|X").fillet(2) \
      .translate((0, 0, 2 + 2))

bat_shell = cq.Workplane("XY") \
      .rect(4.5 + 2*1, 13 + 2*4) \
      .extrude(31 + 2*2) \
      .translate((0, 0, 2 - 2)) \
      .cut(bat_shell_cut) \
      .cut(bat)

screw_pad = cq.Workplane("XZ") \
      .circle(6 / 2) \
      .extrude(50) \
      .translate((0, 25, 0)) \
      .faces("<X").hole(2)

#bat_shell = bat.translate((0, 0, 0)).faces(">Z").shell(th)

#inner_cone = inner_cone.cut(inner_edge) \
#      .cut(inner_edge.rotate((0, 0, 0), (0, 0, 1), 60 * 2)) \
#      .cut(inner_edge.rotate((0, 0, 0), (0, 0, 1), -60 * 2))


# inner_cone = inner_cone.cut(bat_shell)
inner_cone = inner_cone.cut(insight_shell)
inner_cone = inner_cone.cut(bat_shell.translate((9, 0, 16)))
inner_cone = inner_cone.cut(bat_shell.translate((-9, 0, -16)))
inner_cone = inner_cone.cut(screw_pad.translate((8, 0, -32)))
inner_cone = inner_cone.cut(screw_pad.translate((-8, 0, -32)))
inner_cone = inner_cone.cut(screw_pad.translate((0, 0, 72)))

bat = bat.faces("|Z").fillet(3)


#cone = cone.cut(cam).cut(bat)
#cone = cone.cut(bat.translate((-8, 0, -16)))
cone = cone.cut(inner_cone)

#cone = cone.cut(bat)


cone1 = cone.translate((0, 0, 0))
cone1 = cone1.cut(
          cq.Workplane("YZ") \
          .rect(2 * Rout + 50, 2 * h) \
          .extrude(-Rout - 50) \
          .rotate((0, 0, 0), (0, 0, 1), 90)
        ) \
        .translate((0, 5, 0))

cone = cone.cut(
          cq.Workplane("YZ") \
          .rect(2 * Rout + 50, 2 * h) \
          .extrude(Rout + 50) \
          .rotate((0, 0, 0), (0, 0, 1), 90)
        )

#      .line(Rout, 0) \

if __name__ == '__cqgi__':
#    show_object(bat_shell)
    show_object(cone)
    show_object(cone1)
#    show_object(inner_cone)
#    show_object(x)
#    show_object(logo)
else:
    from cadquery import exporters

    box = cover.union(base)

    name = 'box_%dx%d' % (midi_sock_count, midi_sock_count)
    exporters.export(box, name + '.step')
    exporters.export(box, name + '.stl')
    exporters.export(box, name + '.vrml')
