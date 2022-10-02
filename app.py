from flask import Flask
from exts import db, redis_captcha, mail
from flask_migrate import Migrate
from blueprints.UserBlueprint import login_bp
from flask_cors import CORS

import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
redis_captcha.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# 注册蓝图
app.register_blueprint(login_bp)


if __name__ == '__main__':
    app.run(port=667)
