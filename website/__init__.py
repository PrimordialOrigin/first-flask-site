from flask import Flask

def make_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='hdfhcjdkcsdchjvbfvnjdfkvnjfvfvnf' #Encrypts cookies
    
    from .views import bp_views
    from .auth import bp_auth
    
    app.register_blueprint(views.bp_views)
    app.register_blueprint(auth.bp_auth)
        
    return app  