from application import create_app
import os


if os.getenv('FLASK_ENV') == "development":
    app = create_app('Config.DevConfig')
else:
    app = create_app('Config.ProdConfig')
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")