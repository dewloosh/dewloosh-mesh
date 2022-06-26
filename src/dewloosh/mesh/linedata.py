# -*- coding: utf-8 -*-
import numpy as np

from .polydata import PolyData
from .cells import L2, L3


__all__ = ['LineData']

 
class LineData(PolyData):
    
    _cell_classes_ = {
        2: L2,
        3: L3,
    }

    def __init__(self, *args, areas=None, **kwargs):          
        super().__init__(*args, **kwargs)
        if self.celldata is not None:
            nE = len(self.celldata)
            if areas is None:
                areas = np.ones(nE)
            else:
                assert len(areas.shape) == 1, \
                    "'areas' must be a 1d float or integer numpy array!"
            self.celldata.db['areas'] = areas
            
    def _init_config_(self):
        super()._init_config_()
        key = self.__class__._pv_config_key_
        self.config[key]['color'] = 'k'
        self.config[key]['line_width'] = 10
        self.config[key]['render_lines_as_tubes'] = True 
        #self.config[key]['style'] = 'wireframe'   
               