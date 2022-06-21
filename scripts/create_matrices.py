import numpy as np
import cv2

def create_train_matrix(db, db_config):
    rootdir = 'databases/' + db.upper()
    nrpp = int(db_config[0])
    if db == 'orl':
        k = 0
        A = np.zeros(shape=(10304,(40*nrpp)))
        for i in range(40):
            subdir = '/s'+str(i+1)
            for j in range(nrpp):
                path = rootdir+subdir+'/'+str(j+1)+'.pgm'
                A[:,k] = np.array(cv2.imread(path, 0)).reshape(10304,)
                k+=1
        return A
