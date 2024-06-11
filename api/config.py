from dotenv import load_dotenv
import os

load_dotenv()

class Config:
   SUPABASE_API_URI: str = os.environ.get("SUPABASE_API_URI")
   SUPABASE_API_ANON_KEY: str = os.environ.get("SUPABASE_API_ANON_KEY")