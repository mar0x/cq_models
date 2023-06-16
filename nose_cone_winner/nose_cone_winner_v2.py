# This is a CadQuery script template
# Add your script code below
import cadquery as cq
import math

Rout = 34.5 / 2
Rin = 31 / 2
#Rout = 93 / 2
#Rin = 90.6 / 2
h = 120
x0 = (h ** 2 - Rout ** 2) / (2 * Rout)
th = 1.6
cam_rotate_angle = -45
base_height = 40 + 3
base_width = 2.5

# make the cone
cone = cq.Workplane("YZ") \
      .vLine(h) \
      .radiusArc((Rout, 0), x0 + Rout) \
      .hLine(-Rout) \
      .close() \
      .revolve()

inner_cone = cq.Workplane("YZ") \
      .vLine(h - th) \
      .radiusArc((Rout - th, 0), x0 + Rout) \
      .hLine(-Rout + th) \
      .close() \
      .revolve()

base = cq.Workplane("YZ") \
      .vLine(-base_height) \
      .hLine(Rin) \
      .vLine(base_height) \
      .close() \
      .revolve()
base = base.faces("<Z").fillet(2)

inner_base = cq.Workplane("YZ") \
      .vLine(-base_height + base_width) \
      .hLine(Rin - base_width) \
      .vLine(base_height - base_width) \
      .close() \
      .revolve()

insight = cq.Workplane("XY") \
      .rect(2, 23) \
      .extrude(101) \
      .translate((0, 0, -37))

insight_shell_cut = cq.Workplane("XY") \
      .rect(2 + 2*2, 23 - 2*2) \
      .extrude(101 - 2*2) \
      .edges("|X").fillet(2) \
      .translate((0, 0, -37 + 2))

insight_shell = cq.Workplane("XY") \
      .rect(2 + 2*1.6, 23 + 2*2) \
      .extrude(101 + 2*2) \
      .edges("|X").fillet(4) \
      .translate((0, 0, -37 - 2)) \
      .cut(insight_shell_cut) \
      .cut(insight)

sd_module = cq.Workplane("XY") \
      .rect(2, 25) \
      .extrude(42) \
      .translate((0, 0, -37 + 12))

screw_pad = cq.Workplane("XY") \
      .circle(6 / 2) \
      .extrude(6) \
      .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
      .circle(6 / 2) \
      .workplane(offset=6) \
      .center(-3, 0) \
      .circle(0.1) \
      .loft(combine=True) \
      .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
      .hole(2)

cone_screw_pad = cq.Workplane("XY") \
      .circle(6 / 2) \
      .extrude(10) \
      .faces(">Z").workplane(centerOption="CenterOfBoundBox") \
      .hole(2)

#bat_shell = bat.translate((0, 0, 0)).faces(">Z").shell(th)

#inner_cone = inner_cone.cut(inner_edge) \
#      .cut(inner_edge.rotate((0, 0, 0), (0, 0, 1), 60 * 2)) \
#      .cut(inner_edge.rotate((0, 0, 0), (0, 0, 1), -60 * 2))


# inner_cone = inner_cone.cut(bat_shell)
#inner_cone = inner_cone.cut(insight_shell)
#inner_cone = inner_cone.cut(bat_shell.translate((9, 0, 16)))
#inner_cone = inner_cone.cut(bat_shell.translate((-9, 0, -16)))
#inner_cone = inner_cone.cut(screw_pad.translate((8, 0, -32)))
#inner_cone = inner_cone.cut(screw_pad.translate((-8, 0, -32)))
#inner_cone = inner_cone.cut(screw_pad.translate((0, 0, 72)))

#bat = bat.faces("|Z").fillet(3)


#cone = cone.cut(cam).cut(bat)
#cone = cone.cut(bat.translate((-8, 0, -16)))
cone = cone.cut(inner_cone)
cone = cone.union(cone_screw_pad.translate((Rin - 2.5, 0, 0)))
cone = cone.union(cone_screw_pad.translate((-Rin + 2.5, 0, 0)))

b0 = base.translate((0, 0, 3))

base = base.faces("<Z").workplane(centerOption="CenterOfBoundBox") \
        .rarray(2 * Rin - 5, 1, 2, 1, True) \
        .hole(2)
base = base.cut(inner_base)
base = base.union(screw_pad.rotate((0,0,0), (0,0,1), 180).translate((Rin - 2.5, 0, -6 -3)))
base = base.union(screw_pad.translate((-Rin + 2.5, 0, -6 -3)))
base = base.translate((0, 0, 3))
base = base.intersect(b0)
base = base.cut(cone)
base = base.union(insight_shell.intersect(b0))
base = base.cut(sd_module.translate((-4.2, 0, 0)))
base = base.cut(sd_module.translate((4.2, 0, 0)))
#cone = cone.cut(bat)


#cone1 = cone.translate((0, 0, 0))
#cone1 = cone1.cut(
#          cq.Workplane("YZ") \
#          .rect(2 * Rout + 50, 2 * h) \
#          .extrude(-Rout - 50) \
#          .rotate((0, 0, 0), (0, 0, 1), 90)
#        ) \
#        .translate((0, 5, 0))

#cone = cone.cut(
#          cq.Workplane("YZ") \
#          .rect(2 * Rout + 50, 2 * h) \
#          .extrude(Rout + 50) \
#          .rotate((0, 0, 0), (0, 0, 1), 90)
#        )

#      .line(Rout, 0) \

if __name__ == '__cqgi__':
#    show_object(bat_shell)
    show_object(cone)
    show_object(base)
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
