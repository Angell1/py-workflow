
from datetime import datetime
from app.main import db
from app.main.model.workflow import Workflow



def Createworkflow(data):
    workflow = Workflow.query.filter_by(workflowname=data['workflowname']).first()
    if workflow == None:
        new_workflow = Workflow(
            groupid=data["groupid"],
            workflowname=data["workflowname"],
            description=data["description"],
            version=data["version"],
            creater=data["creater"],
            createtime= datetime.now(),
            updatetime =  datetime.now()
        )
        id = save_changes(new_workflow)
        response = {
            'RetCode': '000000',
            'RetMsg': 'Insert Successfully.'
        }
    else:
        response = {
            'RetCode': '000001',
            'RetMsg': 'workflowname is exist.',
        }
    return response



def UpdateworkflowById(id,data):
    workflow = Workflow.query.filter_by(id=id).first()
    if workflow == None:
        response = {
            'RetCode': '000002',
            'RetMsg': 'data not exist.'
        }
    else:
        workflow.groupid=data["groupid"],
        workflow.workflowname = data["workflowname"],
        workflow.description = data["description"],
        workflow.version = data["version"],
        workflow.creater = data["creater"],
        workflow.updatetime = datetime.now()
        save_changes(workflow)
        response = {
            'RetCode': '000000',
            'RetMsg': 'Update Successfully.',
        }
    return response

def QueryworkflowsByGroupid(groupid):
    return Workflow.query.filter_by(groupid=groupid).all()



def RemoveworkflowById(id):
    workflow = Workflow.query.filter_by(id=id).first()
    if workflow == None:
        response = {
            'RetCode': '000002',
            'RetMsg': 'data not exist.',
        }
    else:
        response = {
            'RetCode': '000000',
            'RetMsg': 'Delete Successfully.',
        }
        delete_changes(workflow)
    return   response



def StartworkflowsByGroupid(id):
    workflow = Workflow.query.filter_by(id=id).first()
    if workflow == None:
        response = {
            'RetCode': '000002',
            'RetMsg': 'data not exist.',
        }
    else:
        response = {
            'RetCode': '000000',
            'RetMsg': 'Start Successfully.',
        }
    return response






def save_changes(data):
    db.session.add(data)
    db.session.commit()
    return data.id

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()