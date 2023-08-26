from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured


class Secrets():

    def __init__(self, filename:str):
        """Initialize a Secrets Instance   

        Args:
            filename (str): a json file
        """
        try:
            EnvVarReader_Dir = Path(__file__).resolve().parent
            file_path = os.path.join(EnvVarReader_Dir, filename)
            with open(file_path) as f:
                self.secrets = json.loads(f.read())
        except OSError:
            error_msg = "The file: {0} failed to open.. Is it in the EnvVarReader?".format(filename)
            raise ImproperlyConfigured(error_msg)
            

    def getSecret(self, setting:str) -> str: 
        """Get the secret variable or return explicit exception."""
        try:
            return self.secrets[setting]
        except KeyError:
            error_msg = "Set the {0} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)
        