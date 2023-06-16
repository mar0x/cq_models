import cadquery as cq

box = cq.Workplane("YZ") \
    .moveTo(0, 0) \
    .vLine(8).line(45 - 27, 44 - 8) \
    .hLine(27).vLine(-44) \
    .hLine(-45) \
    .close() \
    .extrude(56)

#box = box.faces("not(|Z or |Y or |X)").fillet(4)

#s = box

#box2 = box.translate((0, 0, 0))

s = box \
    .faces(">Y").shell(-2) \
#    .union(
#        box2.faces("<Z").shell(-2)
#    )

body_color = (133, 133, 133, 0)
body_options = {"rgba": body_color}

metal_color = (200, 200, 200, 0)
metal_options = {"rgba": metal_color}

if __name__ == '__cqgi__':
    show_object(s, options=body_options)
