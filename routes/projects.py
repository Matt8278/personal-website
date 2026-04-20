from flask import Blueprint, render_template
from models.project import Project

bp = Blueprint("projects", __name__, url_prefix="/projects")

@bp.route("/")
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template("projects.html", title="作品集", projects=projects)

@bp.route("/<int:project_id>")
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template("project_detail.html", title=project.title, project=project)