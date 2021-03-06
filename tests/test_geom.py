# -*- coding: utf-8 -*-
import numpy as np
import unittest

from dewloosh.math.linalg import Vector

from dewloosh.mesh import TriMesh, PolyData, grid, PointCloud, CartesianFrame
from dewloosh.mesh.rgrid import grid
from dewloosh.mesh.cells import T3


class TestCoords(unittest.TestCase):

    def test_coords_1(self):
        def test_coord_tr_1(i, a):
            A = CartesianFrame(dim=3)
            coords = PointCloud([
                [1., 0., 0.],
                [0., 1., 0.],
                [0., 0., 1.]
            ], frame=A)
            amounts = [0, 0, 0]
            amounts[i] = a * np.pi / 180
            B = A.orient_new('Body', amounts, 'XYZ')
            arr_new = Vector(coords.array, frame=A).view(B)
            coords_new = Vector(arr_new, frame=B)
            return np.max(np.abs(coords_new.view() - coords.view())) < 1e-8
        assert test_coord_tr_1(1, 120.)


class TestPolyData(unittest.TestCase):

    def test_pd_1(self):
        size = 800, 600, 20
        shape = 8, 6, 2
        coords1, topo1 = grid(size=size, shape=shape, eshape='H27')
        coords2, topo2 = grid(size=size, shape=shape,
                              eshape='H27', origo=(0, 0, 100))
        coords = np.vstack([coords1, coords2])
        topo2 += coords1.shape[0]
        A = CartesianFrame(dim=3)
        pd = PolyData(coords=coords, frame=A)
        pd['group1']['mesh1'] = PolyData(topo=topo1, vtkCellType=29)
        pd['group2', 'mesh2'] = PolyData(topo=topo2, vtkCellType=29)
        pd.center()
        pd.move(np.array([1.0, 0.0, 0.0]))
        pd.centralize()
        pd.center()
        
    def test_pd_2(self):
        size = 100, 100, 100
        shape = 10, 10, 10
        coords, topo = grid(size=size, shape=shape, eshape='H27')
        A = CartesianFrame(dim=3)
        pd = PolyData(coords=coords, frame=A)
        pd['A']['Part1'] = PolyData(topo=topo[:10])
        pd['B']['Part2'] = PolyData(topo=topo[10:-10])
        pd['C']['Part3'] = PolyData(topo=topo[-10:])


    def test_grid_origo_1(self):
        d = np.array([10., -10., 0.])
        size = Lx, Ly, Lz = 10, 10, 20
        shape = nx, ny, nz = 8, 6, 10
        o1 = np.array([0., 0., 0.])
        coords1, topo1 = grid(size=size, shape=shape, eshape='H8', shift=o1)
        o2 = o1 + d
        coords2, topo2 = grid(size=size, shape=shape, eshape='H8', shift=o2)
        topo2 += coords1.shape[0]
        A = CartesianFrame(dim=3)
        pd1 = PolyData(coords=coords1, topo=topo1, frame=A)
        pd2 = PolyData(coords=coords2, topo=topo2, frame=A)
        assert np.max(np.abs(pd2.center() - pd1.center() - d)) < 1e-8
        return True


    def test_volume_H8_1(self):
        size = Lx, Ly, Lz = 10, 10, 20
        shape = nx, ny, nz = 8, 6, 10
        coords, topo = grid(size=size, shape=shape, eshape='H8')
        A = CartesianFrame(dim=3)
        pd = PolyData(coords=coords, topo=topo, frame=A)
        Lx, Ly, Lz = size
        V = Lx * Ly * Lz
        if not np.max(np.abs(V - pd.volume())) < 1e-8:
            return False
        return True


    def test_volume_H8_2(self):
        size = Lx, Ly, Lz = 10, 10, 20
        shape = nx, ny, nz = 8, 6, 10
        coords1, topo1 = grid(size=size, shape=shape, eshape='H8')
        coords2, topo2 = grid(size=size, shape=shape, eshape='H8')
        coords = np.vstack([coords1, coords2])
        topo2 += coords1.shape[0]

        A = CartesianFrame(dim=3)
        pd = PolyData(coords=coords, frame=A)
        pd['group1']['mesh1'] = PolyData(topo=topo1)
        pd['group2', 'mesh2'] = PolyData(topo=topo2)
        Lx, Ly, Lz = size
        V = Lx * Ly * Lz * 2
        if not np.max(np.abs(V - pd.volume())) < 1e-8:
            return False
        return True


    def test_volume_TET4_1(self):
        Lx, Ly, Lz = 10., 10., 20.
        nx, ny, nz = 80, 60, 10
        A = CartesianFrame(dim=3)
        mesh2d = TriMesh(size=(Lx, Ly), shape=(nx, ny), frame=A, celltype=T3)
        mesh3d = mesh2d.extrude(h=Lz, N=nz)        
        V = Lx * Ly * Lz
        if not np.max(np.abs(V - mesh3d.volume())) < 1e-8:
            return False
        return True


if __name__ == "__main__":

    unittest.main()
