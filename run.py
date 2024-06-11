from app import create_app
from flask import Flask

app: Flask = create_app()

if __name__ == "__main__":
	app.run(port=4000, host="0.0.0.0", debug=True)