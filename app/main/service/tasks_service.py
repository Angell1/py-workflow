
from datetime import datetime
from app.main import db
from app.main.model.tasks import Task
from scheduler.schedulerctl.processor import Scheduler


def Createtask(data):
    new_task = Task(
        taskid=data["taskid"],
        groupid=data["groupid"],
        tasks=data["tasks"],
        taskstatus=data["taskstatus"],
        creatertime= datetime.now(),
        updatetime =  datetime.now()
        )
    id = save_changes(new_task)
    response = {
            'RetCode': '000000',
            'RetMsg': 'Insert Successfully.'
    }
    Scheduler(id).start()
    return response



def UpdatetaskById(id,data):
    task = Task.query.filter_by(id=id).first()
    if task == None:
        response = {
            'RetCode': '000002',
            'RetMsg': 'data not exist.'
        }
    else:
        print("old taskstatus",task.taskstatus,type(task.taskstatus))
        print("new taskstatus", data["taskstatus"],type(data["taskstatus"]))
        task.taskstatus = data["taskstatus"]
        task.updatetime = datetime.now()
        id = update_changes(task)
        response = {
            'RetCode': '000000',
            'RetMsg': 'Update Successfully.',
        }
    return response



def QueryworkflowsById(id):
    return Task.query.filter_by(id=id).first()


#
#
#
# def RemoveworkflowById(id):
#     workflow = Workflow.query.filter_by(id=id).first()
#     if workflow == None:
#         response = {
#             'RetCode': '000002',
#             'RetMsg': 'data not exist.',
#         }
#     else:
#         response = {
#             'RetCode': '000000',
#             'RetMsg': 'Delete Successfully.',
#         }
#         delete_changes(workflow)
#     return   response
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
    db.session.commit()
    return data.id

def update_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()