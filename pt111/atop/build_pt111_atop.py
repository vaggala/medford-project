from ase.io import read, write
from ase import Atoms

slab = read("../clean/pt111_clean.traj")

# top surface height
z_levels = sorted({round(atom.position[2], 8) for atom in slab})
z_top = z_levels[-1]
# print(z_top)


top_atom = None
for atom in slab:
    if abs(atom.position[2] - z_top) < 1e-6:
        top_atom = atom
        break

if top_atom is None:
    raise ValueError("Could not find a Pt atom in the top layer.")

x_top = top_atom.position[0]
y_top = top_atom.position[1]

# typical c-pt bond distance is 1.85 - 2.1 A.
# according to https://pubs.aip.org/aip/jcp/article/117/5/2264/453406/CO-on-Pt-111-puzzle-A-possible-solution
# same paper references that CO bond length is ~1.12 - 1.19 A
z_C = z_top + 1.85
z_O = z_C + 1.12

# place CO directly above pt atom top tayer at (0, 0)
co = Atoms(
    "CO",
    positions = [
        (x_top, y_top, z_C), # carbon
        (x_top, y_top, z_O)  # oxygen above carbon :)
    ]
)

slab += co # add CO to slab :)

# DEBUG
write("pt111_atop.traj", slab)
print(slab, "wrote pt111_atop.traj")
print(f"Using atop x,y = ({x_top}, {y_top})")
