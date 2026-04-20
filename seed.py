from app import app
from extensions import db
from models.project import Project

with app.app_context():
    db.create_all()

    projects = [
        Project(
            title="个人网站系统",
            description="使用 Flask + Bootstrap 构建的响应式个人网站。",
            tags="Flask,Python,Web",
            image_url="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=60"
        ),
        Project(
            title="合规风险分析模型",
            description="基于数据分析的企业合规风险预警系统（Demo）。",
            tags="Compliance,Risk,Analytics",
            image_url="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=60"
        ),
    ]

    db.session.add_all(projects)
    db.session.commit()
    print("Seed done!")