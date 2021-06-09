from .animes_view import bp_animes

def init_app(app):
    app.register_blueprint(bp_animes)