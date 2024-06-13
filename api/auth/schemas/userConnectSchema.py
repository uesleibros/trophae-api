from marshmallow import Schema, fields

class UserConnectSchema(Schema):
	email: str = fields.Str(required=True)
	username: str = fields.Str(required=True)
	password: str = fields.Str(required=True)