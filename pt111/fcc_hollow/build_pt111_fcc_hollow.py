from ase.io import read, write
from ase import Atoms

slab = read("../clean/pt111_clean.xyz")

# z_levels = layer heights
z_levels = sorted({round(atom.position[2], 8) for atom in slab})
z_top = z_levels[-1] # height

# fcc hollow (x, y) location for this slab
# this aligns with the 3rd layer from pt111_clean.xyz
# fcc hollow deals with the 3rd layer from the top
z_third_from_top = z_levels[-3]

# find one Pt atom in the third layer; idt it matters which but script isn't random.
# x,y position corresponds to an fcc hollow site relative to the top layer.
fcc_atom = None
for atom in slab:
    if abs(atom.position[2] - z_third_from_top) < 1e-6: # ignores maginally different heights
        fcc_atom = atom
        break

if fcc_atom is None:
    raise ValueError("could not find a pt atom in the third layer :(")

x_fcc = fcc_atom.position[0]
y_fcc = fcc_atom.position[1]

# same logic from ../atop/build_pt111_atop.py
z_C = z_top + 1.85
z_O = z_C + 1.12

co = Atoms(
    "CO",
    positions=[
        (x_fcc, y_fcc, z_C),  # Carbon
        (x_fcc, y_fcc, z_O)   # Oxygen
    ]
)

slab += co

write("pt111_fcc_hollow.traj", slab)

print(slab, "Wrote pt111_fcc_hollow.traj")