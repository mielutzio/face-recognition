from scripts import nn,knn,eigenfaces,lanczos
from scripts import img_processing as ip
from scripts import create_matrices as cm
from flask import request

def run():
    db = request.form['db']
    db_config = request.form['db_config']
    alg = request.form['alg']
    norm = request.form['norm']
    test_img = ip.get_test_img(db)
    
    A = cm.create_train_matrix(db,db_config)
    if alg == 'nn':
        res_pos = nn.run_alg(A, norm, test_img)
        ip.save_result_img(A, res_pos, db)
    elif alg == 'knn':
        kn = int(request.form['kn'])
        res_pos = knn.run_alg(A, norm, test_img, kn, db_config)
        ip.save_result_img(A, res_pos, db)
    elif alg == 'eigenfaces':
        res_pos = eigenfaces.run_alg(norm, test_img)
        ip.save_result_img(A, res_pos, db)
    elif alg == 'lanczos':
        res_pos = lanczos.run_alg(norm,test_img)
        ip.save_result_img(A,res_pos,db)