from postgrest import AsyncPostgrestClient
from ..config import Config

class Database:
	def __init__(self, config: Config) -> None:
		self.__url: str = config.SUPABASE_API_URI
		self.__key: str = config.SUPABASE_API_ANON_KEY
		self.db: AsyncPostgrestClient = AsyncPostgrestClient(base_url=self.__url + "/rest/v1", headers={"apiKey": self.__key})