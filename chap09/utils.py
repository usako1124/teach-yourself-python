
def who(vardict=None):
    """
    Print the NumPy arrays in the given dictionary
    
    Parameters
    ----------
    vardict : dict, optional
        A dictionary possibly contaning ndarrays. Default is globals().
    
    Returns
    ----------
    out : None
        Returns 'None'

    Notes
    ----------
    Prints out the name, shape, bytes and type of all of the ndarrays
    present in `vardict`.

    Examples
    ----------
    >>> a = np.arange(10)
    >>> b = np.ones(20)
    >>> np.who()
    """
    if vardict is None:
        print(who())