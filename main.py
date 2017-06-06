import matplotlib.pyplot as plt 
import numpy as np 
from numpy import linalg as LA
import pandas as pd 
from sklearn.decomposition import PCA 
import time

def decompose(array, n_components=2, reduce_criteria="one-shot"):
    '''
    Run a decomposition algorithm (PCA, etc) either sequentially or "one-shot"

    Parameters:
        array -> the array of points to determine the singular value 
                    decomposition from 
        n_components -> the final number of components to reduce to 
        reduce_criteria -> 
            - "one-shot": reduce once, to final number of components
            - "sequential": reduce (point dimensions) - n_components times, 
                            from n to n-1 dimensions each time.

    '''
    if reduce_criteria == "one-shot":
        pca = PCA(n_components=n_components)
        result = pca.fit_transform(array)
        return result 

    elif reduce_criteria == "sequential":

        i = array.shape[1] - 1
        result = array 

        while i >= 2:
            pca = PCA(n_components=i)
            result = pca.fit_transform(array)
            i -= 1

        return result 

    else:

        raise ValueError("unknown reduction criteria {}".format(reduce_criteria))

        return 

def compare_decompositions(result1, result2):

    if result1.shape != result2.shape:
        raise ValueError("Shapes {} and {} are not alignable".format(
            result1.shape, result2.shape))

    else:
        difference = np.abs(result1 - result2)
        d2 = LA.norm(difference, axis=1).sum()
        return np.allclose(result1, result2), d2 



if __name__ == "__main__":

    reduction_min = 5
    reduction_max = 50
    log_min = 1
    log_max = 8
    log_base = 4

    mesh = np.dstack(np.meshgrid(np.array(list(range(log_min,log_max))), np.array(list(range(reduction_min,reduction_max))))).reshape(-1, 2)

    results = np.empty((log_max - log_min, reduction_max - reduction_min))

    for i in range(log_min, log_max):
        for j in range(reduction_min, reduction_max):
            print(log_base**i, j)
            np.random.seed(int(time.time()))
            array = np.random.rand(log_base**i, j)
            single_decomposition = decompose(array.copy())
            sequential_decomposition = decompose(array.copy(), 
                                            reduce_criteria="sequential")
            res = compare_decompositions(single_decomposition, sequential_decomposition)
            results[i-log_min][j-reduction_min] = res[0]

    cmap = plt.jet()

    fig, ax = plt.subplots(1,1)
    ax.scatter(mesh[:, 0], mesh[:, 1], c=results.T.ravel(), cmap=plt.get_cmap("jet"), vmin=-0.1, vmax=1.1)
    ax.set_xlabel(r"$\log(|{points}|)$")
    ax.set_ylabel(r"Starting Dimensions")
    ax.set_title("Difference in sequential versus single decompositions")
    plt.savefig("images/fig3")

    # fig, (ax1, ax2) = plt.subplots(2,1)
    # ax1.scatter(single_decomposition[:, 0], single_decomposition[:, 1])
    # ax1.set_title("One shot decomposition")
    # ax2.scatter(sequential_decomposition[:, 0], sequential_decomposition[:, 1])
    # ax2.set_title("Sequential decomposition")
    # plt.show()