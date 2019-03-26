from . import index_bule

@index_bule.route("/")
def index():
    return "welcome flask"