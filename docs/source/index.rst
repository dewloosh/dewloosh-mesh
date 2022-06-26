==================================================================
**DewLoosh.Mesh** - A Python Library for Compound Polygonal Meshes
==================================================================

This library is part of `DewLoosh`, a rapid prototyping platform focused on numerical calculations 
mainly corcerned with simulations of natural phenomena.

The current namespace is responsible to handle the gometry and the topolgy related
to `DewLoosh` projects. We basically only use it directly for testing and core developments,
but considering the popularity of similar projects like `PyVista`, we decided to
create a separate namespace. However, we try not to reinvent the weel, but to fill
the gaps where necessary for domain specific applications. 


Features
--------

* ``dewloosh.mesh.space`` provides the batteries to handle linear algebra in 
  Euclidean Space. All the classes are array types and can be the argument
  of numpy universal functions. The implentations rely on the application
  of operations to bulk data using the built-in vectorization solutions 
  of `NumPy`, extended by `Numba`-compiled routines, wherever necessary. 
  As a result, computations are fast and perform well for large datasets.
  The class architecture allows for an arbitrary level of nested frames 
  embedded into one another, as well as the transformation of any number of
  vectors between any two of these frames. 

* The library includes a class architecture for the object oriented imlementation
  of geometrical objects, with an attempt to follow the best practices and domain 
  specific terminology. 

* A set of classes and routines to handle jagged topologies. In a general situation,
  a mesh is thought of as something being composed of several kinds of cells.
  This includes cells in 1, 2 and 3 dimensions, with basically arbitrary shape node 
  configurations. The topology of such a mesh can not be handled by a casual
  ``numpy.ndarray`` array anymore, it has to be a sparse one. These kind of arrays 
  are often called 'jagged-arrays' or 'ragged-arrays'. ``dewloosh.mesh`` is able to
  handle these scenarios with managing an ``awkward.Array`` in the background. 
  The class ``dewloosh.mesh.TopologyArray`` is numba-jittable 
  and numpy-compliant, and extends the behaviour of ``numpy.unique`` for the aformentioned 
  cases.

* A facility for plotting over flat traingulations in 2d, and another one to turn
  any flat mesh into a triangulation. Here we use `matplotlib`, which is capable
  of translating its stuff to `tikz` or other popular formats.

* A small set of recipes for mesh generation. It's not much, but just enough to 
  showcase the full potential of the library. It includes a grid generator that
  generates all kinds of grids suitable for the **Finite Element Method**, as it
  is capable of using a wide range of linear and nonlinear base classes. 
  As always, all of these imlementations are fast and run on numba-jitted code.

* A set of utility routines for various operations on meshes. Voxelization, 
  extrusion, tiling, etc.


Requirements
------------

The implementations in this module are created on top of 

* | `NumPy`, `SciPy` and `Numba` to speed up computationally sensitive parts,

* | `SymPy` for symbolic operations and some vector algebra,

* | the `awkward` library for its high performance data structures, gpu support
  | and general `Numba` compliance.


Gallery
-------

.. nbgallery::
    :caption: Gallery
    :name: rst-gallery
    :glob:
    :reversed:

    _notebooks/*
    
        
Contents
--------

.. toctree::
    :caption: Contents
    :maxdepth: 2
   
    user_guide
    notebooks

API
---

.. toctree::
    :caption: API
    :maxdepth: 3
   
    api
   
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`