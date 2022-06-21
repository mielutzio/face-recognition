from scripts import nn
import numpy as np
import numpy.linalg as la
import time
import cv2
import matplotlib.pyplot as plt


def run_preproc(A, k):
    global medium
    global L
    global projections
    medium = np.mean(A, axis=1)
    A = (A.T-medium).T
    cov_matrix = np.matmul(A.T, A)
    # d = vector of eigenvalues, L = matrix w/ eigenvectors
    d, L = la.eig(cov_matrix)
    L = np.matmul(A, L)
    L = L[:, np.argsort(d)[-k:]]
    projections = np.matmul(A.T, L)


def run_alg(norm, test_img):
    test_img = test_img - medium
    test_img = np.matmul(test_img.T, L)
    test_img = test_img.T
    return nn.run_alg(projections.T, norm, test_img)


def run_stats(A, db, db_config):
    k = [20, 40, 60, 80, 100]
    norm = ['n1', 'n2', 'ninf', 'ncos']
    rr = np.zeros(shape=(len(norm), len(k)))
    aqt = np.zeros(shape=(len(norm), len(k)))
    preproc = np.zeros(shape=(len(norm), len(k)))

    for n in range(len(norm)):
        for m in range(len(k)):
            counter = 0
            tm = 0
            pp_time = 0
            t = time.time()
            run_preproc(A, k[m])
            pp_time += time.time()-t
            for i in range(40):
                subdir = '/s'+str(i+1)
                for j in range(int(db_config[3])):
                    path = "databases/ORL/"+subdir+'/' + \
                        str(j+(int(db_config[0])+1))+'.pgm'
                    test_img = np.array(cv2.imread(path, 0)).reshape(-1,)
                    t = time.time()
                    res = run_alg(norm[n], test_img)
                    tm += time.time()-t
                    if int(res/int(db_config[0])) == i:
                        counter += 1
            rr[n, m] = counter/(int(db_config[3])*40)
            aqt[n, m] = tm/(int(db_config[3])*40)
            preproc[n, m] = pp_time

    # plot results
    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    fig.suptitle('Eigenfaces-Recognition Rate')
    c = 0
    for i in range(2):
        for j in range(2):
            axs[i, j].plot(k, rr[c], 'o:r')
            axs[i, j].set_title(norm[c])
            axs[i, j].set_xlabel('k')
            axs[i, j].set_ylabel('RR')
            c += 1
    plot_rr = db.upper()+'_'+db_config+'_'+'eigenfaces'+'_'+'rr.png'
    plt.savefig('static/images/statistics/'+plot_rr)
    plt.clf()

    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    fig.suptitle('Eigenfaces-Average Query Time')
    c = 0
    for i in range(2):
        for j in range(2):
            axs[i, j].plot(k, aqt[c], 'o:r')
            axs[i, j].set_title(norm[c])
            axs[i, j].set_xlabel('k')
            axs[i, j].set_ylabel('AQT')
            c += 1
    plot_aqt = db.upper()+'_'+db_config+'_'+'eigenfaces'+'_'+'aqt.png'
    plt.savefig('static/images/statistics/'+plot_aqt)
    plt.clf()

    plt.plot(k, preproc[0], 'o:r')
    plt.title('Eigenfaces-Preprocessing Time')
    plt.xlabel('k')
    plt.ylabel('t')
    plot_preproc = db.upper()+'_'+db_config+'_'+'eigenfaces'+'_'+'preproc.png'
    plt.savefig('static/images/statistics/'+plot_preproc)
    plt.clf()
