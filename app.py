from dotenv import load_dotenv
load_dotenv()
from core import constants
from core.api.v1 import apiv1 as api_v1
from core.models import app

app.register_blueprint(api_v1, url_prefix='/api/v1')

@app.route("/")
def index():
    return "Hello from Histents API!"

if __name__ == "__main__":
    app.run(debug=constants.DEBUG)