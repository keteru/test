from testapp import app
from flask import render_template, request, redirect, url_for
from testapp import session
from testapp.models.uriage import Uriage
from sqlalchemy import desc, distinct
import os
import datetime
from testapp.uriage_load import UriageLoad
import requests

@app.route('/')
def top():
    return render_template('testapp/top.html')

@app.route('/sample')
def sample():
    # data = 'views.pyのinsert_something部分です'
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です',
        'insert_something2': 'views.pyのinsert_something2部分です',
        'test_titles': ['title1', 'title2', 'title3']
        }
    return render_template('testapp/sample.html', my_dict=my_dict)

@app.route('/uriage', methods=["GET", "POST"])
def uriage_list():
    uriages = session.query(Uriage).order_by(desc(Uriage.id)).all()
    return render_template('testapp/uriage_list.html', uriages=uriages)

@app.route('/uriage_edit', methods=["POST"])
def uriage_edit():
    return render_template('testapp/uriage_edit.html')

@app.route('/upload', methods=["GET", "POST"])
def upload():

    upload_error = ''
    if request.method == 'POST' and request.files.get('file') is not None:
        upload_error = upload_exec(request)
    elif request.method == 'POST' and request.form.get('loadfilename') is not None:
        upload_error = load(request.form.get('loadfilename'))
    elif request.method == 'POST' and request.form.get('delfilename') is not None:
        upload_error = delete(request.form.get('delfilename'))

    excelfiles, registfiles = get_fileinfo()

    return render_template('testapp/uriage_upload.html', excelfiles=excelfiles, registfiles=registfiles, upload_error=upload_error)

def upload_exec(request):

    dt_now = datetime.datetime.now()
    file = request.files.get('file')
    file_name = dt_now.strftime('%Y%m%d%H%M%S') + '_' + file.filename
    file_path = os.path.join('files', file_name)
    file.save(file_path)

    uriage_load = UriageLoad()
    upload_error = uriage_load.check([file_name])

    if upload_error != '':
        os.remove(file_path)

    return upload_error

def delete(file_name):
    file_path = os.path.join('files', file_name)
    os.remove(file_path)
    return ''

def load(file_name):
    uriage_load = UriageLoad()
    file_path = os.path.join('files', file_name)

    return uriage_load.load([file_name])

def get_fileinfo():
    excelfiles = [file for file in os.listdir('files') if file.endswith('.xlsx')]
    excelfiles.sort()

    results = session.query(distinct(Uriage.filename)).all()
    registfiles = [file[0] for file in results]
    registfiles.sort()

    return excelfiles, registfiles
