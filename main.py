from flask import Flask, render_template, request, abort, session
import utils

app = Flask(__name__)
app.secret_key = "aze"

plurals = ["plans", "planrequests", "states", "providers", "cluster-providers", "module-template", "cluster-module-template", "modules"]

namespaces = ["default", "kube-node-lease", "kube-public", "kube-system", "nsx-system", "pks-system"]

@app.route('/')
def hello():
    return render_template('index.html', plural="plans", namespace=None, namespaces=namespaces)

@app.route('/<plural>')
@app.route('/<plural>/')
def plural(plural):
    if plural not in plurals:
        abort(404)
    else:
        pluralToPrint = utils.pluralsTranslation(plural)
        return render_template("index.html", plural=plural, pluralToPrint=pluralToPrint, namespace=None, namespaces=namespaces)

@app.route('/<plural>/<namespace>', methods=['GET', 'POST'])
@app.route('/<plural>/<namespace>/', methods=['GET', 'POST'])
def pluralNamespaced(plural, namespace):
    if plural not in plurals or namespace not in namespaces:
        abort(404)
    else:
        if plural.startswith('cluster'):
            disable="disable"
        else:
            disable=None
        pluralToPrint = utils.pluralsTranslation(plural)
        return render_template("index.html", plural=plural, pluralToPrint=pluralToPrint, disable=disable, namespace=namespace, namespaces=namespaces)

@app.route('/edit')
def cluster():
    return render_template('edit.html')

    from flask import Flask