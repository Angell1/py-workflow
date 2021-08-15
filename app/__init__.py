from flask_restplus import Api
from flask import Blueprint

from .main.controller.workflow_controller import Workflowapi
from .main.controller.workflowgroup_controller import Workflowgroupapi
from .main.controller.tasks_controller import TasksDtoapi


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='py-workflow',
          version='1.0',
          description='支持HTTP、RPC接口以任务节点链式调用'
          )

api.add_namespace(Workflowapi, path='/workflow')
api.add_namespace(Workflowgroupapi, path='/workflowgroup')
api.add_namespace(TasksDtoapi, path='/tasks')