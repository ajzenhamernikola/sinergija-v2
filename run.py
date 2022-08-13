from dotenv import load_dotenv
from eve import Eve

from configs.swagger import config_swagger

load_dotenv()
app = Eve()

config_swagger(app)

if __name__ == "__main__":
    app.run()
