import os

env = os.getenv("OMAGENT_MODE", "lite").lower()

if env == "lite":
    print ("importing lite client") 
    from .lite_client import DefaultClient
else:
    print ("importing pro client")
    from .client import DefaultClient

