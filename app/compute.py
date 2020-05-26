import numpy as np
import matplotlib.pyplot as plt
import os, time, glob
from flask import json
from io import BytesIO
import base64

def weibull_f(x,k,l):
    return 1.0-np.exp(-np.power((x/l),k))

def volterra_calculation(k,l,t):
    d=1
    m=int(t/d+1)

    F=[0.0]
    A=[0.0]
    N=[0.0]

    for i in np.arange(m)[1:]:
        fi=weibull_f((i-0.5)*d,k,l)
        ai=weibull_f(i*d,k,l)
        F.append(fi)
        A.append(ai)

    for i in np.arange(m)[1:]:
        sum=0
        for j in np.arange(i)[1:]:
            sum = sum + (N[j]-N[j-1])*F[i-j+1]
        ni=(A[i]+sum-N[i-1]*F[1])/(1.0-F[1])    
        N.append(ni)    

    return N

def compute(k,l,t):
    """Return filename of plot of the damped_vibration function."""
    w = volterra_calculation(k,l,t)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(w)
    # # plt.title('A=%g, b=%g, w=%g' % (A, b, w))
    # if not os.path.isdir('static'):
    #     os.mkdir('static')
    # else:
    #     # Remove old plot files
    #     for filename in glob.glob(os.path.join('static', '*.png')):
    #         os.remove(filename)
    # # Use time since Jan 1, 1970 in filename in order make
    # # a unique filename that the browser has not chached
    # #plotfile = os.path.join('static', str(time.time()) + '.png')
    # #plt.savefig(plotfile)
    # #print('compute_display')
    # #print(plotfile)
    # #print(w)

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    data = {'data':w[-1],'image':figdata_png.decode('ascii')}
    return json.dumps(data)

if __name__ == '__main__':
    print (compute(1.37,1228,60))
