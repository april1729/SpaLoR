from spalor.algorithms.scpa_algorithms import *
from spalor.util.regularizers import *

class SparsePCA():
    def __init__(self):
        pass
    def fit(self, M, r=5, alpha1=0, alpha2=1):
        prox=lambda x,alpha: mcp_prox(x, alpha, 1)
        (U,V)=prox_grad_spca(M, r, alpha1, alpha2, prox)
        self.U=U
        self.V=V

    def transform(self, X):
        return X.dot(self.V)

    def inverse_transform(self, X):
        return self.U.dot(X)

    def get_params(self):
        return (self.U, self.V)
