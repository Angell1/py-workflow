from flask import request
from flask_restplus import Resource,marshal,reqparse

from ..serializers.workflowdto import  WorkflowDto
from ..service.workflow_service import Createworkflow,QueryworkflowsByGroupid,RemoveworkflowById,UpdateworkflowById,StartworkflowsByGroupid

Workflowapi = WorkflowDto.api
workmodel = WorkflowDto.workflow



@Workflowapi.route('/list')
class WorkflowList(Resource):
    # swgger 查询参数配置
    @Workflowapi.doc(params={'groupid': '任务组ID'})
    # 序列化输出
    @Workflowapi.marshal_with(workmodel, as_list=True)
    def get(self):
        # swgger api注解
        """ List Workflow """
        parser = reqparse.RequestParser()
        parser.add_argument('groupid')
        args = parser.parse_args()
        return QueryworkflowsByGroupid(args["groupid"])
        # return marshal(QueryworkflowsByGroupid(args["groupid"]), workmodel, envelope='data')



@Workflowapi.route('/create')
class Create(Resource):
    # 序列化输入
    @Workflowapi.expect(workmodel, validate=True)
    def post(self):
        """ Create Workflow """
        return Createworkflow(data=request.json)


@Workflowapi.route('/update')
class Update(Resource):
    # 序列化输入
    @Workflowapi.expect(workmodel, validate=True)
    def post(self):
        """ Update Workflow """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return UpdateworkflowById(id=args["id"],data=request.json)


@Workflowapi.route('/remove')
class Remove(Resource):
    # swgger 查询参数配置
    @Workflowapi.doc(params={'id': '主键ID'})
    def get(self):
        # swgger api注解
        """ Remove Workflow """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return RemoveworkflowById(args["id"])


@Workflowapi.route('/start')
class StratWorkflow(Resource):
    # swgger 查询参数配置
    @Workflowapi.doc(params={'id': '主键ID'})
    def get(self):
        # swgger api注解
        """ Start Workflow """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return StartworkflowsByGroupid(args["id"])
