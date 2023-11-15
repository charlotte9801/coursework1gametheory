import matplotlib.pyplot as plt


def hawksdoves(prop_hawk, num, fitness, value, cost):
    """
    Computes the proportion of Hawks and Doves after a number of trials.

    Parameters
    ----------
    prop_hawk : float
        Proportion of Hawks in an infinite population,
        consisting of only Hawks and Doves. Must be in the range [0,1]

    num : integer
        Number of trials, or generations, that the game occurs over

    fitness : integer
        Initial fitness of both Hawks and Doves. In this context,
        the amount of offspring each individual will spawn

    value : integer
        The gain in fitness corresponding to winning the pairwise contest.

    cost : integer
        The loss in fitness corresponding to getting injured during the
        contest.

    Returns
    -------
    hawksdove : figure
        A graph showing the evolution of the proportion of the 2 species
        through time.

    """
    if prop_hawk > 1:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_hawk}"
        )
    elif prop_hawk < 0:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_hawk}"
        )
    else:
        p = prop_hawk
        w_h = fitness
        w_d = fitness
        v = value
        c = cost
        p_new = 0
        list_h = [p]
        list_d = [(1-p)]
        fig = plt.figure()
        for i in range(num):
            p_new = (p * w_h-(v * p**2)/2-(c * p**2)/2+v*p)/(p*w_h
                                                             - p*w_d+w_d+v/2 -
                                                             (c*p**2/2))
            w_h = w_h + p*((v-c)/2) + (1-p)*v
            w_d = w_d + (1-p)*(v/2)
            list_h.append(p_new)
            list_d.append(1-p_new)
            p = p_new
        plt.plot(list_h, color='r', label='Hawks')
        plt.plot(list_d, color='g', label='Doves')
        return fig


f = hawksdoves(1/3, 100000, 3, 1, 3)
f = plt.xlabel("Number of Generations")
f = plt.ylabel("Proportion of Population")
plt.legend()
plt.show()
