from dotenv import load_dotenv
from eve import Eve
from flask_cors import CORS

from authentication import auth
from configs.register_hooks import register_hooks
from configs.swagger import config_swagger
from core.request import SinergijaRequest
from hooks.database_hooks.domain_hooks.people import PeopleHooksTable
from hooks.database_hooks.request_hooks.pre_get_hooks import PreGetHooksTable

load_dotenv()
app = Eve()

CORS(app, supports_credentials=True)
config_swagger(app)
register_hooks(app, [PeopleHooksTable(), PreGetHooksTable()])

if __name__ == "__main__":
    app.register_blueprint(auth.bp)
    app.request_class = SinergijaRequest
    app.run()
