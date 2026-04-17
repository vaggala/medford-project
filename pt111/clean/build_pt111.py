from ase.build import fcc111
from ase.io import write

# build a Pt(111) slab
# size = (nx, ny, layers)

slab = fcc111(
    "Pt",
    size =(3, 2, 5), # pulled from feibelman experiement/paper
    a = 3.92,          
    vacuum = 15.0, 
    orthogonal = True
)

slab.center(axis = 2, vacuum = 15.0)

write("pt111_clean.traj", slab)

print(slab, "successfully wrote pt111_clean.traj")

# psp path is /home/hice1/vaggala3/packages/SPARC/psps