from flask_restplus import Namespace, fields


class WorkflowgroupDto:
    api = Namespace('workflowgroup', description='workflow related operations')
    workflowgroup = api.model('workflowgroup', {
        'id': fields.Integer(description='主键ID'),
        'groupname': fields.String(description='流水线组'),
        'workflownum': fields.Integer(description='流水线数量'),
        'creater': fields.String(description='创建者'),
        'createtime': fields.DateTime(description='创建时间'),
        'updatetime': fields.DateTime(description='更新时间'),
        'businessline':fields.String(description='业务线'),
        'psm': fields.String(description='服务'),
        'env': fields.String(description='测试环境'),
        'bits':fields.String(description='bits链接'),
    })