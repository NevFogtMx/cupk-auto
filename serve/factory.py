from flask import Flask
from flask_cors import CORS
from blueprints.jwxt import jwxt_bp
from settings import UserConfig, jwxtUrlConfig, SessionConfig

def create_app():
    app = Flask(__name__)
    # 加载配置类
    app.config.from_object(UserConfig)
    app.config.from_object(jwxtUrlConfig)
    app.config.from_object(SessionConfig)
    # 注册蓝图
    app.register_blueprint(jwxt_bp, url_prefix='/jwxt')
    CORS(app)
    return app
