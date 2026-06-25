# bachelor-project-calculix

Finite-element (FEM) structural analysis from my bachelor's in Medical Natural
Sciences (VU Amsterdam, 2022) — modelling stress and deformation in simple and
layered structures, including biological tissue, to study mechanical response and
estimate properties such as Young's modulus.

## What's here

- **`bachelor_project_calculix.py`** — a "plate with a hole" stress-concentration
  model built with [pycalculix](https://github.com/spacether/pycalculix) (a Python
  front end to the open-source CalculiX solver). It draws the geometry, meshes it
  with gmsh, applies pressure loads and constraints to a steel plate
  (E = 210 GPa, ν = 0.3), solves the plane-stress problem, and reports peak stress
  and reaction forces — a classic FEM validation case.
- **`Circle.py`** — a two-material "eukaryotic cell" model (cytoplasm + membrane
  with different stiffness), solved the same way, as a step toward modelling
  layered biological structures.
- **`FEM_Two_Layer.txt`, `double_layer.txt`, `layered_cell_xample.txt`** — ANSYS
  APDL input decks for two-layer tissue models, parameterised by layer geometry
  and per-layer material properties (Young's modulus in kPa, Poisson's ratio).

## Stack

Python · pycalculix / CalculiX · gmsh · ANSYS APDL · numerical methods / FEM

## Notes

Bachelor-level computational-mechanics work (2022). The focus is the modelling and
numerical approach; the scripts run directly against a local CalculiX/gmsh install
(and ANSYS for the `.txt` decks).
