import cadquery as cq

t = cq.Workplane("YZ") \
    .sphere(37 / 2, angle3=180) \
    .faces("<Z").workplane(centerOption="CenterOfBoundBox") \
      .hole(4.2, 10)

if __name__ == '__cqgi__':
    show_object(t)
