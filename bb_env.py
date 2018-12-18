class setup():

    def imports():
        import pandas as pd 
        import numpy as np 
        import random 
        from scipy import stats
        from matplotlib import pyplot as plt
        from bb_plot import plot_fig as bb_plot
        from sklearn.utils import resample
        from sklearn.ensemble import RandomForestClassifier as RFC 
        from sklearn.ensemble import RandomForestRegressor  as RFR
        from sklearn import metrics
        from imblearn.ensemble import BalancedRandomForestClassifier as BRF
        from sklearn import model_selection as mdl_slc 

        print('Set these variables to the imports function output')
        print('pd, np, resample, random, stats, plt, bb_plot, RFC, BRF, RFR, metrics, mdl_slc')
        return pd, np, resample, random, stats, plt, bb_plot, RFC, BRF, RFR, metrics, mdl_slc

