from .. import db

class Workflow(db.Model):
    """ Workflow Model for storing user related details """
    __tablename__ = "workflow"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupid = db.Column(db.Integer,autoincrement=True)
    workflowname = db.Column(db.String(100), unique=True,nullable=False)
    description = db.Column(db.String(100))
    version = db.Column(db.String(50), nullable=False)
    creater = db.Column(db.String(50), nullable=False)
    creatertime = db.Column(db.DateTime, nullable=False, default=False)
    updatetime = db.Column(db.DateTime, nullable=False, default=False)
    tasks = db.Column(db.String(100), nullable=False, default=False)

