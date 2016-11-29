import dask.array as da
import numpy as np

from multipledispatch import dispatch

@dispatch(np.ndarray,np.ndarray)
def dot(A,B):
    return np.dot(A,B)

@dispatch(da.Array,da.Array)
def dot(A,B):
    return da.dot(A,B)

@dispatch(np.ndarray)
def diag(A):
    return np.diag(np.diag(A))

@dispatch(da.Array)
def diag(A):
    return da.diag(da.diag(A))

@dispatch(np.ndarray)
def inv_diag(A):
    return np.diag(1/np.diag(A))

@dispatch(da.Array)
def inv_diag(A):
    return da.diag(1/da.diag(A))

@dispatch(np.ndarray)
def absolute(A):
    return np.absolute(A)

@dispatch(da.Array)
def absolute(A):
    return da.absolute(A)

@dispatch(da.Array)
def sigmoid(x):
    '''Sigmoid function of x.'''
    return 1/(1+da.exp(-x))

@dispatch(np.ndarray)
def sigmoid(x):
    '''Sigmoid function of x.'''
    return 1/(1+np.exp(-x))

def log_likelihood(p, y):
    '''Computes the log-likelihood'''
    
    return np.sum(y*np.log(p) + (1-y)*np.log(1-p)).values[0]

def data_create(seed, N, chunks):
    da.random.seed(seed)
    X = da.random.random((N,2), chunks=chunks)
    y = (X.dot(np.array([[1.5,-3]]).T)).map_blocks(sigmoid) + .001*da.random.normal(size=(N,1), chunks=chunks)
    return X,y
