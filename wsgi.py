from application import create_app
import os
import socket


if os.getenv("FLASK_ENV") == "development":
    app = create_app("Config.DevConfig")
else:
    app = create_app("Config.ProdConfig")


ip_address = socket.gethostbyname(socket.gethostname)

if __name__ == "__main__":
    app.run(debug=True, host=ip_address)
