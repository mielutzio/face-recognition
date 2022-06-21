import numpy as np
from numpy import linalg as la
from matplotlib import pyplot as plt
import time
import cv2
import matplotlib
matplotlib.use('Agg')


def run_alg(A, norm, test_img):
    z = np.zeros(shape=(1, len(A[0])))
    for i in range(len(A[0])):
        if norm == 'n1':
            z[0, i] = la.norm(test_img-A[:, i], 1)
        elif norm == 'n2':
            z[0, i] = la.norm(test_img-A[:, i])
        elif norm == 'ninf':
            z[0, i] = la.norm(test_img-A[:, i], np.inf)
        elif norm == 'ncos':
            z[0, i] = 1-(np.dot(test_img, A[:, i])) / \
                (la.norm(test_img)*la.norm(A[:, i]))
    return np.argmin(z)


def run_stats(A, db, db_config):
    norm = ['n1', 'n2', 'ninf', 'ncos']
    rr = np.zeros(shape=(len(norm)))
    aqt = np.zeros(shape=(len(norm)))
    for n in range(len(norm)):
        counter = 0
        tm = 0
        for i in range(40):
            subdir = '/s'+str(i+1)
            for j in range(int(db_config[3])):
                path = 'databases/ORL/'+subdir+'/' + \
                    str(j+(int(db_config[0])+1))+'.pgm'
                test_img = np.array(cv2.imread(path, 0)).reshape(-1,)
                t = time.time()
                res = run_alg(A, norm[n], test_img)
                tm += time.time()-t
                if int(res/int(db_config[0])) == i:
                    counter += 1
        rr[n] = counter/(int(db_config[3])*40)
        aqt[n] = tm/(int(db_config[3])*40)

    # plot results
    plt.plot(norm, rr, 'o:r')
    plt.title('NN-Recognition Rate')
    plt.xlabel('Norm')
    plt.ylabel('RR')
    plot_rr = db.upper()+'_'+db_config+'_'+'nn'+'_'+'rr.png'
    plt.savefig('static/images/statistics/'+plot_rr)
    plt.clf()

    plt.plot(norm, aqt, 'o:r')
    plt.title('NN-Average Query Time')
    plt.xlabel('Norm')
    plt.ylabel('AQT')
    plot_aqt = db.upper()+'_'+db_config+'_'+'nn'+'_'+'aqt.png'
    plt.savefig('static/images/statistics/'+plot_aqt)
    plt.clf()
