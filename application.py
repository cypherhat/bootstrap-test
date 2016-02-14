from flask.templating import render_template
from flask_api import FlaskAPI
from flask_api.decorators import set_renderers
from flask_api.renderers import HTMLRenderer
application = FlaskAPI(__name__)


@application.route("/", methods=['GET'])
@application.route("/home", methods=['GET'])
@set_renderers(HTMLRenderer)
def home():
    params_tpl = {}
    return render_template('index.html', params_tpl=params_tpl)


@application.route("/login", methods=['GET'])
@set_renderers(HTMLRenderer)
def login():
    params_tpl = {}
    return render_template('login.html', params_tpl=params_tpl)


@application.route("/panels_wells", methods=['GET'])
@set_renderers(HTMLRenderer)
def panels_wells():
    params_tpl = {}
    return render_template('panels-wells.html', params_tpl=params_tpl)


@application.route("/buttons", methods=['GET'])
@set_renderers(HTMLRenderer)
def buttons():
    params_tpl = {}
    return render_template('buttons.html', params_tpl=params_tpl)


@application.route("/flot", methods=['GET'])
@set_renderers(HTMLRenderer)
def flot():
    params_tpl = {}
    return render_template('flot.html', params_tpl=params_tpl)


@application.route("/forms", methods=['GET'])
@set_renderers(HTMLRenderer)
def forms():
    params_tpl = {}
    return render_template('forms.html', params_tpl=params_tpl)


@application.route("/grid", methods=['GET'])
@set_renderers(HTMLRenderer)
def grid():
    params_tpl = {}
    return render_template('grid.html', params_tpl=params_tpl)


@application.route("/icons", methods=['GET'])
@set_renderers(HTMLRenderer)
def icons():
    params_tpl = {}
    return render_template('icons.html', params_tpl=params_tpl)


@application.route("/morris", methods=['GET'])
@set_renderers(HTMLRenderer)
def morris():
    params_tpl = {}
    return render_template('morris.html', params_tpl=params_tpl)


@application.route("/notifications", methods=['GET'])
@set_renderers(HTMLRenderer)
def notifications():
    params_tpl = {}
    return render_template('notifications.html', params_tpl=params_tpl)


@application.route("/tables", methods=['GET'])
@set_renderers(HTMLRenderer)
def tables():
    params_tpl = {}
    return render_template('tables.html', params_tpl=params_tpl)


@application.route("/typography", methods=['GET'])
@set_renderers(HTMLRenderer)
def typography():
    params_tpl = {}
    return render_template('typography.html', params_tpl=params_tpl)


@application.route("/blank", methods=['GET'])
@set_renderers(HTMLRenderer)
def blank():
    params_tpl = {}
    return render_template('blank.html', params_tpl=params_tpl)

if __name__ == "__main__":
    application.run(debug=True, use_reloader=False)