from .. import db

class Workflowgroup(db.Model):
    """ workflowgroup Model for storing user related details """
    __tablename__ = "workflowgroup"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupname = db.Column(db.String(100), unique=True,nullable=False)
    creater = db.Column(db.String(50), nullable=False)
    createtime = db.Column(db.DateTime, nullable=False, default=False)
    updatetime = db.Column(db.DateTime, nullable=False, default=False)
    workflownum = db.Column(db.Integer)
    businessline = db.Column(db.String(50), nullable=False, default="")
    psm = db.Column(db.String(50), nullable=False, default="")
    env = db.Column(db.String(50), nullable=False, default="")
    bits = db.Column(db.String(100), nullable=False, default="")