from vega_datasets import data

def cars():
    return data.cars()

def iris():
    return data.iris()

def barley():
    return data.barley().head()

