from scripts import create_matrices as cm
from scripts import eigenfaces,lanczos
from flask import request

def run():
    db = request.form['db']
    db_config = request.form['db_config']
    alg = request.form['alg']
    if alg == 'eigenfaces':
        A = cm.create_train_matrix(db,db_config)
        k = int(request.form['ke'])
        eigenfaces.run_preproc(A,k)
    elif alg == 'lanczos':
        A = cm.create_train_matrix(db,db_config)
        k = int(request.form['kl'])
        lanczos.run_preproc(A,k)