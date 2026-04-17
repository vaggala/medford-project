from ase.build import fcc111
from ase.io import write

# build a Cu(111) slab
# size = (nx, ny, layers)

slab = fcc111(
    "Cu",
    size =(3, 2, 5), # pulled from feibelman experiement/paper
    a = 3.61, # lattice energy          
    vacuum = 15.0, 
    orthogonal = True
)

slab.center(axis = 2, vacuum = 15.0)

write("cu111_clean.traj", slab)

print(slab, "successfully wrote cu111_clean.traj")
