"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
"""
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple of int
        The row and column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    # Check if X is a numpy array
    if not isinstance(X, np.ndarray):
        raise ValueError("Input is not a numpy array")

    # Check if the shape is 2D
    if X.ndim != 2:
        raise ValueError("Input array does not have a 2D shape")

    n_samples, n_features = np.shape(X)

    m = X[0, 0]
    i = 0
    j = 0

    for k in range(n_samples):
        for g in range(n_features):
            if X[k, g] > m:
                m = X[k, g]
                i = k
                j = g

    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.
    """
    if n_terms == 0:
        return 2.0

    terms = np.arange(1, n_terms + 1)
    pi_approximation = 2.0 * np.prod((2 * terms) ** 2 /
                                     ((2 * terms - 1) * (2 * terms + 1)))

    return pi_approximation
