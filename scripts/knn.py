from numpy import linalg as la
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def run_alg(A, norm, test_img, k, db_config):
    z = np.zeros(shape=(1, len(A[0])))
    for i in range(len(A[0])):
        if norm == 'n1':
            z[0, i] = la.norm(test_img-A[:, i], 1)
        elif norm == 'n2':
            z[0, i] = la.norm(test_img-A[:, i])
        elif norm == 'ninf':
            z[0, i] = la.norm(test_img-A[:, i], np.inf)
        elif norm == 'ncos':
            z[0, i] = 1 - np.dot(test_img, A[:, i]) / \
                (la.norm(test_img) * la.norm(A[:, i]))
    pos = np.argsort(z)
    neighbs_class = np.zeros(shape=(1, k))
    for i in range(k):
        neighbs_class[0, i] = int(pos[0, i]/int(db_config[0]))
    uniq, counts = np.unique(neighbs_class, return_counts=True)

    return uniq[np.argmax(counts)]*int(db_config[0])


def run_stats(A, db, db_config):
    k = [3, 5, 7]
    norm = ['n1', 'n2', 'ninf', 'ncos']
    rr = np.zeros(shape=(len(k), len(norm)))
    aqt = np.zeros(shape=(len(k), len(norm)))
    for m in range(len(k)):
        for n in range(len(norm)):
            counter = 0
            tm = 0
            for i in range(40):
                subdir = '/s'+str(i+1)
                for j in range(int(db_config[3])):
                    path = "databases/ORL"+subdir+'/' + \
                        str(j+(int(db_config[0])+1))+'.pgm'
                    test_img = np.array(cv2.imread(path, 0)).reshape(-1,)
                    t = time.time()
                    res = run_alg(A, norm[n], test_img, k[m], db_config)
                    tm += time.time()-t
                    if int(res/int(db_config[0])) == i:
                        counter += 1
            rr[m, n] = counter/(int(db_config[3])*40)
            aqt[m, n] = tm/(int(db_config[3])*40)

    # plot results
    fig, axs = plt.subplots(1, len(k), constrained_layout=True)
    fig.suptitle('kNN-Recognition Rate')
    c = 0
    for i in range(len(k)):
        axs[i].plot(norm, rr[c], 'o:r')
        axs[i].set_title('k= '+str(k[c]))
        axs[i].set_xlabel('Norm')
        axs[i].set_ylabel('RR')
        c += 1
    plot_rr = db.upper()+'_'+db_config+'_'+'knn'+'_'+'rr.png'
    plt.savefig('static/images/statistics/'+plot_rr)
    plt.clf()

    fig, axs = plt.subplots(1, len(k), constrained_layout=True)
    fig.suptitle('kNN-Average Query Time')
    c = 0
    for i in range(len(k)):
        axs[i].plot(norm, aqt[c], 'o:r')
        axs[i].set_title('k= '+str(k[c]))
        axs[i].set_xlabel('Norm')
        axs[i].set_ylabel('AQT')
        c += 1
    plot_aqt = db.upper()+'_'+db_config+'_'+'knn'+'_'+'aqt.png'
    plt.savefig('static/images/statistics/'+plot_aqt)
    plt.clf()
