# -*- coding:utf-8 -*-
import json


class Load:
    def Load(self):
        with open("saveFile.json", "r", encoding="utf-8") as json_file:
            Load = json.load(json_file)

            return Load


Load().Load()
