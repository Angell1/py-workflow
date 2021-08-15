from flask_restplus import Namespace, fields


class TasksDto:
    api = Namespace('tasks', description='tasks related operations')
    tasks = api.model('tasks', {
        'id': fields.Integer(description='主键ID'),
        'taskid': fields.Integer(required=True, description='流水线ID'),
        'groupid': fields.Integer(required=True, description='任务组ID'),
        'tasks': fields.String(description='流水线任务'),
        'taskstatus':fields.String(description='流水线状态'),
        'creatertime': fields.DateTime(description='创建时间'),
        'updatetime': fields.DateTime(description='更新时间'),
    })