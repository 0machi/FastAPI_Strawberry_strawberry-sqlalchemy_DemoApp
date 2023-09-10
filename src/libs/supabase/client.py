import os

from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions

try:
    env = os.environ["ENV"]
    url = os.environ["SUPABASE_URL"]
    key = os.environ["SUPABASE_KEY"]
except KeyError as e:
    print(f"Environment variable not set: {e}")

supabase_client: Client = create_client(
    supabase_url=url, supabase_key=key, options=ClientOptions(schema=env)
)
