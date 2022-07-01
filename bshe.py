from flask import Flask
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
from apps.ueditor import bp as ueditor_bp
import config
from apps.cms.models import CMSUser
from exts import db



# def create_app():
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
    # db.create_all()
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(common_bp)
app.register_blueprint(ueditor_bp)
    #
    # return app



if __name__ == '__main__':
    # app=create_app()
    app.run(port=8080)
