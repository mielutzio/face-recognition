from scripts import nn
import numpy as np
import numpy.linalg as la
import time
import matplotlib.pyplot as plt
import cv2


def run_preproc(A, k):
    global projections
    global L
    q = np.zeros(shape=(len(A[:, 0]), k+2))
    L = np.zeros(shape=(len(A[:, 0]), k))
    beta = 0
    q[:, 1] = 1
    q[:, 1] = q[:, 1]/la.norm(q[:, 1])
    for i in range(1, k+1, 1):
        omega = np.dot(A, np.dot(A.T, q[:, i]))-np.dot(beta, q[:, i-1])
        alfa = np.dot(omega, q[:, i])
        omega = omega-np.dot(alfa, q[:, i])
        beta = la.norm(omega)
        q[:, i+1] = omega/beta
    L = q[:, 2:]
    projections = np.dot(A.T, L)


def run_alg(norm, test_img):
    test_img = np.dot(test_img.T, L)
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
    fig.suptitle('Lanczos-Recognition Rate')
    c = 0
    for i in range(2):
        for j in range(2):
            axs[i, j].plot(k, rr[c], 'o:r')
            axs[i, j].set_title(norm[c])
            axs[i, j].set_xlabel('k')
            axs[i, j].set_ylabel('RR')
            c += 1
    plot_rr = db.upper()+'_'+db_config+'_'+'lanczos'+'_'+'rr.png'
    plt.savefig('static/images/statistics/'+plot_rr)
    plt.clf()

    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    fig.suptitle('Lanczos-Average Query Time')
    c = 0
    for i in range(2):
        for j in range(2):
            axs[i, j].plot(k, aqt[c], 'o:r')
            axs[i, j].set_title(norm[c])
            axs[i, j].set_xlabel('k')
            axs[i, j].set_ylabel('AQT')
            c += 1
    plot_aqt = db.upper()+'_'+db_config+'_'+'lanczos'+'_'+'aqt.png'
    plt.savefig('static/images/statistics/'+plot_aqt)
    plt.clf()

    plt.plot(k, preproc[0], 'o:r')
    plt.title('Lanczos-Preprocessing Time')
    plt.xlabel('k')
    plt.ylabel('t')
    plot_preproc = db.upper()+'_'+db_config+'_'+'lanczos'+'_'+'preproc.png'
    plt.savefig('static/images/statistics/'+plot_preproc)
    plt.clf()
