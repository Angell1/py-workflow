from flask import request
from flask_restplus import Resource,marshal,reqparse

from ..serializers.workflowgroupdto import  WorkflowgroupDto
from ..service.workflowgroup_service import QueryworkflowgroupById,Queryworkflowgroup,Createworkflowgroup,RemoveById


Workflowgroupapi = WorkflowgroupDto.api
workflowgroupmodel = WorkflowgroupDto.workflowgroup



@Workflowgroupapi.route('/QueryById')
class WorkflowList(Resource):
    # swgger 查询参数配置
    @Workflowgroupapi.doc(params={'id': '主键ID'})
    # 序列化输出
    @Workflowgroupapi.marshal_with(workflowgroupmodel, as_list=True)
    def get(self):
        # swgger api注解
        """ QueryById Workflowgroup """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return QueryworkflowgroupById(args["id"])
        # return marshal(QueryworkflowsByGroupid(args["groupid"]), workmodel, envelope='data')


@Workflowgroupapi.route('/QueryAll')
class WorkflowList(Resource):
    # 序列化输出
    @Workflowgroupapi.marshal_with(workflowgroupmodel, as_list=True)
    def get(self):
        # swgger api注解
        """ QueryAll Workflowgroup """
        return Queryworkflowgroup()
        # return marshal(QueryworkflowsByGroupid(args["groupid"]), workmodel, envelope='data')

@Workflowgroupapi.route('/RemoveById')
class WorkflowList(Resource):
    # swgger 查询参数配置
    @Workflowgroupapi.doc(params={'id': '主键ID'})
    # 序列化输出
    # @Workflowgroupapi.marshal_with(workflowgroupmodel, as_list=True)
    def get(self):
        # swgger api注解
        """ RemoveById Workflowgroup """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return RemoveById(args["id"])



@Workflowgroupapi.route('/Create')
class Create(Resource):
    # 序列化输入
    @Workflowgroupapi.expect(workflowgroupmodel, validate=True)
    def post(self):
        """ Create Workflowgroup """
        return Createworkflowgroup(data=request.json)