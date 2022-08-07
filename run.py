from dotenv import load_dotenv
from eve import Eve

load_dotenv()
app = Eve()

if __name__ == "__main__":
    app.run()
