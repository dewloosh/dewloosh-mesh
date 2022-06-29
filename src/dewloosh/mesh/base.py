# -*- coding: utf-8 -*-
"""
These base classes meant to resolve circular references
while providing static hints.

This module must not have references from other parts of the library,
to make sure circular refrerences are all avoided.

"""
from abc import abstractmethod, abstractproperty

from numpy import ndarray

from dewloosh.core import DeepDict

from .akwrap import AkWrapper


class PointDataBase(AkWrapper):
    
    @abstractproperty
    def id(self) -> ndarray:
        ...
    
    @abstractproperty
    def frame(self) -> ndarray:
        """Ought to return a frame of reference."""
        ...
        
    @abstractproperty
    def x(self) -> ndarray:
        """Ought to return the coordinates of the associated pointcloud."""
        ...
        

class CellDataBase(AkWrapper):
    
    @abstractproperty
    def id(self) -> ndarray:
        ...
    
    @abstractmethod
    def coords(self, *args, **kwargs) -> ndarray:
        """Ought to return the coordiantes associated with the object."""
        ...
    
    @abstractmethod
    def topology(self, *args, **kwargs) -> ndarray:
        """Ought to return the topology associated with the object."""
        ...
    
    @abstractmethod
    def measures(self, *args, **kwargs) -> ndarray:
        """Ought to return meaninful measures for each cell."""
        ...
    
    @abstractmethod
    def measure(self, *args, **kwargs) -> ndarray:
        """Ought to return a single measure for a collection of cells."""
        ...


class PolyDataBase(DeepDict):
    
    @abstractmethod
    def coords(self, *args, **kwargs) -> ndarray:
        """Ought to return the coordiantes associated with the object."""
        ...
    
    @abstractmethod
    def topology(self, *args, **kwargs) -> ndarray:
        """Ought to return the topology associated with the object."""
        ...
