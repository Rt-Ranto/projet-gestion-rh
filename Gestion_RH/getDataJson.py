from django.apps import apps
from pathlib import Path
import json

class DataJson:
    def __init__(self):
        self.__app_path = Path(apps.get_app_config('Gestion_RH').path)
        self.__path = self.__app_path/'data'/'data.json'

    def ecrire_json_data(self, data):
        with open(self.__path,"w", encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)

    def lire_json_data(self):
        with open(self.__path,"r",encoding="utf-8") as f:
            data = json.load(f)
        return data