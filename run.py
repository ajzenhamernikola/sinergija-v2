from dotenv import load_dotenv
from eve import Eve

from authentication import auth
from configs.register_hooks import register_hooks
from configs.swagger import config_swagger
from hooks.database_hooks.people import PeopleHooksTable

load_dotenv()
app = Eve()

config_swagger(app)
register_hooks(app, [PeopleHooksTable()])

if __name__ == "__main__":
    app.register_blueprint(auth.bp)
    app.run()
