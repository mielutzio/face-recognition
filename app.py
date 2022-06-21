from scripts import img_processing as ip
from scripts import run_alg,run_preproc,run_stats
from flask import Flask,render_template,request
import os

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app._static_folder = 'static'
app.config['UPLOAD_FOLDER'] = 'static'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['sbtn'] == 'Select':
            ip.upload_image()
            os.remove('static/images/result.png')
        elif request.form['sbtn'] == 'Search':
            try:
                run_alg.run()
            except Exception as err:
                print(err)
                return render_template('index.html',em=True)
        elif request.form['sbtn'] == 'Preprocessing':
            run_preproc.run()
        elif request.form['sbtn'] == 'Statistics' :
            rr,aqt,preproc = run_stats.run()
            return render_template('statistics.html',
                graph_rr = rr, graph_aqt = aqt, graph_preproc = preproc)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)