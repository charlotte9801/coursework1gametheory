import matplotlib.pyplot as plt


def hawkdovebourgeois(prop_hawk, prop_dove, num, fitness,
                      value, cost):
    """
    Computes the proportion of Hawks and Doves and Bourgeois after a number of
    trials.

    Parameters
    ----------
    prop_hawk : float
        Proportion of Hawks in an infinite population,
        consisting of only Hawks, Doves and Bourgeois. Must be in the
        range [0,1]. If summed with prop_dove cannot exceed 1.

    prop_hawk : float
        Proportion of Doves in an infinite population,
        consisting of only Hawks, Doves and Bourgeois Must be in the
        range [0,1]. If summed with prop_hawk cannot exceed 1.

    num : integer
        Number of trials, or generations, that the game occurs over

    fitness : integer
        Initial fitness of Hawks, Doves and Bourgeois. In this context,
        the amount of offspring each individual will spawn

    value : integer
        The gain in fitness corresponding to winning the pairwise contest.

    cost : integer
        The loss in fitness corresponding to getting injured during the
        contest.

    Returns
    -------
    hawkdovebourgeois : figure
        A graph showing the evolution of the proportion of the 3 species
        through time.

    """
    p = prop_hawk
    q = prop_dove
    r = 1 - p - q
    w_h = fitness
    w_d = fitness
    w_b = fitness
    v = value
    c = cost
    p_new = 0
    q_new = 0
    r_new = 0
    list_h = [p]
    list_d = [q]
    list_b = [r]
    fig = plt.figure()
    if prop_hawk < 0:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_hawk}"
        )
    elif prop_dove < 0:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_dove}"
        )
    elif prop_dove > 1:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_dove}"
        )
    elif prop_hawk > 1:
        raise ValueError(
            f"Proportion must be in range [0,1], not {prop_dove}"
        )
    elif prop_hawk + prop_dove > 1:
        raise ValueError(
            "Sum of 2 proportions must be less than 1, to allow for the "
            f"Bourgeois proportion, not {p+q}."
        )
    else:
        for i in range(num):
            p_new = ((p*(w_h + p*((v-c)/2) + q*v + r*((1/4)*(3*v-c))))
                     / (p*(w_h + p*((v-c)/2) + q*v + r*(0.25*(3*v-c)))
                        + q*(w_d + q*(v/2) + r*(v/4)) +
                        r*(w_b + p*((v-c)/4) + q*((3*v)/4) + r*(v/2))))
            q_new = ((q*(w_d + q*(v/2) + r*(v/4)))
                     / (p*(w_h + p*((v-c)/2) + q*v + r*((1/4)*(3*v-c)))
                        + q*(w_d + q*(v/2) + r*(v/4)) +
                        r*(w_b + p*((v-c)/4) + q*((3*v)/4) + r*(v/2))))
            r_new = ((r*(w_b + p*((v-c)/4) + q*((3*v)/4) + r*(v/2)))
                     / (p*(w_h + p*((v-c)/2) + q*v + r*(0.25*(3*v-c)))
                        + q*(w_d + q*(v/2) + r*(v/4)) +
                         r*(w_b + p*((v-c)/4) + q*((3*v)/4) + r*(v/2))))
            w_h = w_h + p*((v-c)/2) + q*v + r*(0.25*(3*v-c))
            w_d = w_d + q*(v/2) + r*(v/4)
            w_b = w_b + p*((v-c)/4) + q*((3*v)/4) + r*(v/2)
            list_h.append(p_new)
            list_d.append(q_new)
            list_b.append(r_new)
            p = p_new
            q = q_new
            r = r_new
        plt.plot(list_h, color='r', label='Hawks')
        plt.plot(list_d, color='g', label='Doves')
        plt.plot(list_b, color='b', label='Bourgeois')
        return fig


f = hawkdovebourgeois(0.5, 0.6, 100, 2, 1, 3)
f = plt.xlabel("Number of Generations")
f = plt.ylabel("Proportion of Population")
plt.legend()
plt.show()
