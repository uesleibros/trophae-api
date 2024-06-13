from api.auth import auth_blueprint
from flask import g, request, jsonify
from typing import Dict
from marshmallow import ValidationError
from api.auth.schemas.userConnectSchema import UserConnectSchema
from api.auth.utils.password import checkPassword

@auth_blueprint.route("/user/connect", methods=["POST"])
async def UserConnect() -> Dict[str, any]:
	try:
		schema: UserConnectSchema = UserConnectSchema()
		data: Dict[str, any] = request.get_json()
		user_connect_data: Dict[str, any] = schema.load(data)
	except ValidationError as err:
		return jsonify({"errors": err.messages}), 400
	except Exception as e:
		return jsonify({"error": str(e)}), 500  # Handle unexpected errors

	try:
		db: g.database = g.database.db
		email: str = user_connect_data["email"]
		username: str = user_connect_data["username"]
		password: str = user_connect_data["password"].encode("utf-8")

		user_hashed_password: Dict[str, any] = await db.table("users").select("hashed_password").eq("username", username).eq("email", email).execute()
		if not user_hashed_password.data:
			return jsonify({"error": "User not found"}), 404

		if not await checkPassword(password, user_hashed_password.data[0]["hashed_password"].encode("utf-8")):
			return jsonify({"error": "Incorrect password"}), 401

		user_id: Dict[str, any] = await db.table("users").select("id").eq("username", username).eq("email", email).eq("hashed_password", user_hashed_password.data[0]["hashed_password"]).execute()
		if not user_id.data:
			return jsonify({"error": "User not found"}), 404

		return jsonify({"access_token": user_id.data[0]["id"]}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 500  # Handle unexpected database or other errors
