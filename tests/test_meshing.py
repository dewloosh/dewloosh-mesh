# -*- coding: utf-8 -*-
import numpy as np
import unittest

from dewloosh.mesh import TriMesh, grid, Grid, PolyData
from dewloosh.mesh.primitives import circular_disk
from dewloosh.mesh.voxelize import voxelize_cylinder
from dewloosh.mesh.cells import H8, TET4
from dewloosh.mesh.topo import detach_mesh_bulk
from dewloosh.mesh.extrude import extrude_T3_TET4


class TestMeshing(unittest.TestCase):

    def test_trimesh(self):
        trimesh = TriMesh(size=(800, 600), shape=(10, 10))
        disk = circular_disk(120, 60, 5, 25)
        
    def test_grid(self):
        Grid(size=(80, 60, 20), shape=(8, 6, 2), eshape='H8')
        Grid(size=(80, 60, 20), shape=(8, 6, 2), eshape='H27')
        
    def test_voxelize(self):
        d, h, a, b = 100., 0.8, 1.5, 0.5  
        coords, topo = voxelize_cylinder(radius=[b/2, a/2], height=h, size=h/20)
        PolyData(coords=coords, topo=topo, celltype=H8)
        
    def test_extrude(self):
        n_angles = 120
        n_radii = 60
        min_radius = 5
        max_radius = 25
        h = 20
        zres = 20
        points, triangles = \
            circular_disk(n_angles, n_radii, min_radius, max_radius)        
        points, triangles = detach_mesh_bulk(points, triangles)            
        coords, topo = extrude_T3_TET4(points, triangles, h, zres)       
        tetmesh = PolyData(coords=coords, topo=topo, celltype=TET4)


if __name__ == "__main__":

    unittest.main()
