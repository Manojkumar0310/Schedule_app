from flask import Flask

from .extensions import mongo

from .main.routes import main

def create_app():
    
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = 'mongodb+srv://MANOJRAMUK:JONAMRAMUK@cluster0.wc9vnx5.mongodb.net/MYDB?retryWrites=true&w=majority'
    
    mongo.init_app(app)
    
    app.register_blueprint(main)
    
    return app