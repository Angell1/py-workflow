from flask import request
from flask_restplus import Resource,marshal,reqparse
from ..serializers.tasksdto import  TasksDto
from ..service.tasks_service import QueryworkflowsById,Createtask


TasksDtoapi = TasksDto.api
TasksDtomodel = TasksDto.tasks


@TasksDtoapi.route('/list')
class TaskList(Resource):
    # swgger 查询参数配置
    @TasksDtoapi.doc(params={'id': '主键ID'})
    # 序列化输出
    @TasksDtoapi.marshal_with(TasksDtomodel, as_list=True)
    def get(self):
        # swgger api注解
        """ List Task """
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        return QueryworkflowsById(args["id"])
        # return marshal(QueryworkflowsByGroupid(args["groupid"]), workmodel, envelope='data')


@TasksDtoapi.route('/create')
class Create(Resource):
    # 序列化输入
    @TasksDtoapi.expect(TasksDtomodel, validate=True)
    def post(self):
        """ Create Task """
        return Createtask(data=request.json)