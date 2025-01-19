import os
from dotenv import load_dotenv
from pathlib import Path



def _set_env(var: str):
    # Load environment variables from the .env file
    dotenv_path = Path('./.env')
    load_dotenv(dotenv_path=dotenv_path)

    # Retrieve the value of the environment variable
    value = os.getenv(var)

    if value is None:
        raise ValueError(f"The environment variable '{var}' is not set in the .env file or system environment.")
    
    # Set the environment variable
    os.environ[var] = value
    return value