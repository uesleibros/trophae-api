from .... import auth_blueprint
from flask import g

@auth_blueprint.route("/user/connect", methods=["POST"])
async def UserConnect() -> any:
	db: g.database = g.database
	return "oi"