import pycalculix as pyc

#model name
project_name = 'Hole_model'
a = pyc.FeaModel(project_name)

#unit of model
a.set_units('m')

#Definition of variables
hole_diameter = 2.000
plate_width = 4.444
ratio = hole_diameter/plate_width
plate_length = 2*plate_width
hole_radius = hole_diameter/2
plate_length_quarter = plate_length/2
plate_width_quarter = plate_width/2

#Draw the part > must be clockwise
#Coordinates are x, y -> radial, axial (inverse of normal coordinate system)
b = pyc.Part(a)
b.goto(0.0, hole_radius)
b.draw_arc_angle(90, 0.0, 0.0)
b.draw_line_to(plate_length_quarter, 0.0)
b.draw_line_ax(plate_width_quarter)
b.draw_line_rad(-plate_length_quarter*0.5)
b.draw_line_rad(-plate_length_quarter*0.5)
b.draw_line_to(0.0, hole_radius)
a.plot_geometry(project_name+'_prechunked')

#cut part into mesh
b.chunk()
a.plot_geometry(project_name+'_chunked')

#loads and constraints > positive = push, negative = pull
a.set_load('press',b.top,-1000000)
a.set_load('press',b.right,-1000000)
a.set_constr('fix',b.left,'y')
a.set_constr('fix',b.bottom,'x')

#set kind of material
material = pyc.Material('steel')
material.set_mech_props(7800, 210*(10**9), 0.3)
a.set_matl(material, b)

#Mesh the part
a.set_eshape('tri', 2)
a.set_etype('plstress', b, 0.1)
a.set_ediv('L0', 100)
a.mesh(1.0, 'gmsh')
#plot elements
a.plot_elements(project_name+'_elem')
a.plot_pressures(project_name+'_press')
a.plot_constraints(project_name+'_constr')

#make model
model = pyc.Problem(a, 'struct')
model.solve()

#view and query results
sx = model.rfile.get_nmax('Sx')
print('Sx_max: %f' %sx)
[fx, fy, fz] = model.rfile.get_fsum(a.get_item('L5'))
print('Reaction forces (fx,fy,fz) = (%12.10f, %12.10f, %12.10f)' %(fx, fy, fz))

#plot results
fields = 'Sx,Sy,S1,S2,S3,Seqv,ux,uy,utot,ex'
fields = fields.split(',')
for field in fields:
    fname = project_name+'_'+field
    model.rfile.nplot(field, fname, display=False)