from flask import request
from scripts import nn, knn, eigenfaces, lanczos
from scripts import create_matrices as cm
import os

def run():
    db = request.form['db']
    db_config = request.form['db_config']
    alg = request.form['alg']
    file = db.upper()+'_'+db_config+'_'+alg+'_'+'rr.png'
    if not os.path.exists("static/images/statistics/"+file):
        if alg == 'nn':
            A = cm.create_train_matrix(db,db_config)
            nn.run_stats(A, db, db_config)
        elif alg == 'knn':
            A = cm.create_train_matrix(db,db_config)
            knn.run_stats(A,db,db_config)
        elif alg == 'eigenfaces':
            A = cm.create_train_matrix(db,db_config)
            eigenfaces.run_stats(A,db,db_config)
        elif alg == 'lanczos':
            A = cm.create_train_matrix(db,db_config)
            lanczos.run_stats(A,db,db_config)
    rr = db.upper()+'_'+db_config+'_'+alg+'_'+'rr.png'
    aqt = db.upper()+'_'+db_config+'_'+alg+'_'+'aqt.png'
    if alg == 'eigenfaces' or alg == 'lanczos':
        preproc = db.upper()+'_'+db_config+'_'+alg+'_'+'preproc.png'
    else:
        preproc = None

    return rr, aqt, preproc
