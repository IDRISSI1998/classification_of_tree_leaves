#!/usr/bin/python
#-*- coding: utf-8 -*-
import pandas as pd
from src.DataManagement.Preprocessing import PreprocessingStrategy
from sklearn.decomposition import PCA as _PCA 

class PCA(PreprocessingStrategy):
    def __init__(self,**kwargs):
        super().__init__()
        self._method = _PCA(**kwargs)
        self.hyperparams = self._method.get_params
        
    def preprocess(self, data):
        """ Return the transformed data """
        data_transformed = self._method.fit_transform(data)
        return pd.DataFrame(data_transformed,columns=['PCA_axis%d'%i for i in range(len(self._method.singular_values_))], index = data.index)

    def jsonify(self):
        out = super().jsonify()
        out.update(**{'hyperparams':self.hyperparams})
        return out
