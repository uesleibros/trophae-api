import aiobcrypt

async def hashPassword(password: str) -> str:
	salt: str = await aiobcrypt.gensalt(14)
	hashed: str = await aiobcrypt.hashpw(password, salt)

	return hashed

async def checkPassword(password: str, hashed: str) -> bool:
	return await aiobcrypt.checkpw(password, hashed)