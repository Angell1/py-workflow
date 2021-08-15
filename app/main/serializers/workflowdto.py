from flask_restplus import Namespace, fields


class WorkflowDto:
    api = Namespace('workflow', description='workflow related operations')
    workflow = api.model('workflow', {
        'id': fields.Integer(description='主键ID'),
        'groupid': fields.Integer(required=True, description='任务组ID'),
        'workflowname': fields.String(required=True, description='流水线'),
        'description': fields.String(required=True, description='流水线描述'),
        'version': fields.String(description='版本'),
        'creater': fields.String(description='创建者'),
        'creatertime': fields.DateTime(description='创建时间'),
        'updatetime': fields.DateTime(description='更新时间'),
        'tasks': fields.String(description='流水线任务'),
    })