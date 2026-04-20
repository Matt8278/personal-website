from flask import Flask
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 导入模型（让迁移能发现表）
    from models.project import Project  # noqa: F401

    # 注册蓝图
    from routes.main import bp as main_bp
    from routes.about import bp as about_bp
    from routes.contact import bp as contact_bp
    from routes.projects import bp as projects_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(projects_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)