
def firstlaw (k, m, n):
    tot = k + m + n

    k_tot = k/tot
    kk = k_tot * (k-1)/(tot-1)
    km = k_tot * (m/(tot-1))
    kn = k_tot * (n/(tot-1))

    m_tot = m/tot
    mk = m_tot * (k/(tot-1))
    mm = m_tot * (m-1)/(tot-1) * 0.75
    mn = m_tot * (n/(tot-1)) * 0.5

    n_tot = n/tot
    nk = n_tot * (k/(tot-1))
    nm = n_tot * (m/(tot-1)) * 0.5
    nn = n_tot * (n-1)/(tot-1)* 0

    return kk + km + kn + mk + mm + mn + nk + nm + nn



print(firstlaw(17, 16, 25))
