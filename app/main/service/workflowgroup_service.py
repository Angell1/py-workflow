
from datetime import datetime
from app.main import db
from app.main.model.workflowgroup import Workflowgroup

def Createworkflowgroup(data):
    workflowgroup = Workflowgroup.query.filter_by(groupname=data['groupname']).first()
    if workflowgroup == None:
        new_workflowgroup = Workflowgroup(
            groupname=data["groupname"],
            workflownum=0,
            creater=data["creater"],
            createtime= datetime.now(),
            updatetime =  datetime.now(),
            businessline = data["businessline"],
            psm=data["psm"],
            env=data["env"],
            bits=data["bits"],
        )
        save_changes(new_workflowgroup)
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



# def UpdateworkflowById(id,data):
#     workflow = Workflow.query.filter_by(id=id).first()
#     if workflow == None:
#         response = {
#             'RetCode': '000002',
#             'RetMsg': 'data not exist.'
#         }
#     else:
#         workflow.groupid=data["groupid"],
#         workflow.workflowname = data["workflowname"],
#         workflow.description = data["description"],
#         workflow.version = data["version"],
#         workflow.creater = data["creater"],
#         workflow.updatetime = datetime.now()
#         save_changes(workflow)
#         response = {
#             'RetCode': '000000',
#             'RetMsg': 'Update Successfully.',
#         }
#     return response


def QueryworkflowgroupById(id):
    return Workflowgroup.query.filter_by(id=id).all()



def Queryworkflowgroup():
    return Workflowgroup.query.all()


def RemoveById(id):
    workflowgroup = Workflowgroup.query.filter_by(id=id).first()
    if workflowgroup == None:
        response = {
            'RetCode': '000002',
            'RetMsg': 'data not exist.',
        }
    else:
        response = {
            'RetCode': '000000',
            'RetMsg': 'Delete Successfully.',
        }
        delete_changes(workflowgroup)
    return   response
#
#
#
# def StartworkflowsByGroupid(id):
#     workflow = Workflow.query.filter_by(id=id).first()
#     if workflow == None:
#         response = {
#             'RetCode': '000002',
#             'RetMsg': 'data not exist.',
#         }
#     else:
#         response = {
#             'RetCode': '000000',
#             'RetMsg': 'Start Successfully.',
#         }
#     return response


def save_changes(data):
    db.session.add(data)
    id = db.session.flush()    # ????????????????????????????????? id
    db.session.commit()
    return id


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()