## Staged Decomposition

This repository is a numerical exploration of the following question.

If I have a set of points in _n_ dimensions, and decide to do some reduction algorithm to _m_ dimensions, where _n_ >> _m_, under what circumstances do my results differ it matter if I do the reduction all at once (from _n_ to _m_ dimension), or by reducing the set of points one dimension at a time (from _n_ to _n-1_ to _n-2_ and so on...)?

For the exploration, I use the PCA (Principal Component Analysis) implemention provided by [Scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).

A full write-up is hopefully coming on the blog shortly.

