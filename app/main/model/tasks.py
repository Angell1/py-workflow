from .. import db

class Task(db.Model):
    """ task Model for storing user related details """
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    taskid = db.Column(db.Integer, nullable=False)
    groupid = db.Column(db.Integer, nullable=False)
    tasks = db.Column(db.String(1000), nullable=False)
    taskstatus = db.Column(db.String(1000), nullable=False)
    creatertime = db.Column(db.DateTime, nullable=False, default=False)
    updatetime = db.Column(db.DateTime, nullable=False, default=False)