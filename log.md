### Process notes, in lieu of writeup (for now)

Update 1 (1:18 am):

Maybe this is true? I haven't looked into this, but it seems to be true up to a certain number of points and dimensions, after which it permanently dissolves, which could just be the result of persistent rounding errors in the PCA algorithm.

Update 2 (1:38 am):

Testing up to 4^6 at a starting dimension of 25 suggests that this rounding concern is not the case. For reasons unknown, np.allclose is satisfied at some natural numbers (greater than 30), and then is satisfied at some arbitrary points in (30, 50). These results seem too consistent, however (see fig2 - points that satisfy are larger, although this isn't particularly visually satisfying). It's possible that 

Update 3 (1:44 am):

Not using np.ravel() correctly

