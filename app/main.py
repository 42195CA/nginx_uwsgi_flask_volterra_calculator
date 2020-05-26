from model import InputForm
from flask import Flask, render_template, request,json
from compute import compute
import sys

app = Flask(__name__)

template_name = 'view_flask_bootstrap'
from flask_bootstrap import Bootstrap
Bootstrap(app)

print (template_name)
@app.route('/', methods=['GET', 'POST'])
# @app.route('/weibull', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.k.data, form.l.data,
                         form.t.data)
        result = json.loads(result)
    else:
        # result = None
        # {'answer':w[-1],'curve':plotfile}
        result = {'data':None,'image':None}
    print('flask_app_display')
    print(result)
    # print (form, dir(form))
    #print form.keys()
    # for f in form:
    #     print (f.id)
    #     print (f.name)
    #     print (f.label)

    
    return render_template(template_name + '.html',
                           form=form, image=result['image'], data=result['data'])

if __name__ == '__main__':
    app.run(debug=True)
