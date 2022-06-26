# -*- coding: utf-8 -*-
__version__ = "0.0.1a"
__description__ = "A Python package to build, manipulate and analyze polygonal meshes."

from dewloosh.mesh.space import PointCloud
from dewloosh.mesh.space import CartesianFrame
from dewloosh.mesh.tri.triang import triangulate
from dewloosh.mesh.rgrid import grid, Grid
from dewloosh.mesh.tri.trimesh import TriMesh
from dewloosh.mesh.tet.tetmesh import TetMesh
from dewloosh.mesh.polydata import PolyData
from dewloosh.mesh.linedata import LineData