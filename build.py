import pandas as pd


def equal_operator(ds1, ds2):
    ds_equal = (ds1 == ds2)
    return ds_equal

def greater_than_operator(ds1, ds2):
    ds_greater = (ds1 > ds2)
    return ds_greater

def less_than_operator(ds1, ds2):
    ds_lesser = (ds1 < ds2)
    return ds_lesser
