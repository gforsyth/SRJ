import numpy

def SRJschedule(N, w, q):
    kmin = numpy.sin(numpy.pi/2/N)**2
    k = numpy.arange(kmin, 2., kmin)

    w = numpy.asarray(w)
    q = numpy.asarray(q)

    m = sum(q)

    wt = numpy.zeros(m)
    wt[0] = w[0]

    w = w[1:].copy()
    q = q[1:].copy()

    g = numpy.ones(k.size) * numpy.abs(1 - k*wt[0])

    for i in xrange(1,m):
        ww = 1./k[numpy.where(g == g.max())[0]]
        dis = numpy.abs(w - ww)
        ind = numpy.where(dis == dis.min())[0][0]
        wt[i] = w[ind]
        g = g * numpy.abs(1 - k*wt[i])
        if numpy.sum(wt == w[ind]) == q[ind]:
            w = numpy.delete(w,ind)
            q = numpy.delete(q,ind)

    return wt
