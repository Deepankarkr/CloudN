from flask_restplus import Api
from .BentekFlowService import us_conf
from .SaveStatus import us_conf1
from .Benteklogin import us_conf3
from .BentekFlowAttributes import us_conf4
from .BentekTimeSeriesService import us_conf5

api = Api(
    title='US Natural Gas REST API',
    version='1.0',
    description='Used by multiple services for US NG Desk',
)

api.add_namespace(us_conf)
api.add_namespace(us_conf1)
api.add_namespace(us_conf3)
api.add_namespace(us_conf4)
api.add_namespace(us_conf5)
