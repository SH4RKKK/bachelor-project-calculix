import sys

import pycalculix as pyc

proj_name = 'eukaryotic_cell'
model = pyc.FeaModel(proj_name)
model.set_units('m')

# Define variables we'll use to draw part geometry
diam = 2.0 # hole diam

# Draw part geometry, you must draw the part CLOCKWISE,
# x, y = radial, axial
part = pyc.Part(model)
part.draw_circle(1.0, 1.0, 0.5*diam, 4)
part.draw_hole(1.0, 1.0, 0.75*0.5*diam, 4, filled=True)
part.chunk()

# view the geometry
model.plot_geometry(proj_name+'_geom')

# set loads and constraints
pressure = -1000
model.set_load('pressure', ['L0', 'L1'], pressure)
model.set_constr('fix', 'P4', 'x')

# set part material
mat = pyc.Material('cytoplasm')
mat.set_mech_props(1000, 210*(10**9), 0.3)
model.set_matl(mat, 'A1')

mat2 = pyc.Material('cell_membrane')
mat2.set_mech_props(100, 120*(10**9), 0.5)
model.set_matl(mat2, ['A0','A2','A3','A4'])

# set the element type and mesh database
model.set_eshape('tri', 2)
model.set_etype('plstress', part, 0.1)
model.set_ediv('L0', 10)
model.mesh(1.0, 'gmsh') # mesh 1.0 fineness, smaller is finer
model.plot_elements(proj_name+'_elem')
model.plot_pressures(proj_name+'_press')
model.plot_constraints(proj_name+'_constr')

# make and solve the model
prob = pyc.Problem(model, 'struct')
prob.solve()

# view and query results
sx = prob.rfile.get_nmax('Sx')
print('Sx_max: %f' % sx)

# Plot results
# store the fields to plot
fields = 'Sx,Sy,S1,S2,S3,Seqv,ux,uy,utot,ex'
fields = fields.split(',')
for field in fields:
    fname = proj_name+'_'+field
    prob.rfile.nplot(field, fname, display=False)