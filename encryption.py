import json
from cryptography.fernet import Fernet
from os.path import isfile, join
import os
os.chdir(os.path.dirname(__file__))


class Encryption:

    def __init__(self):
        with open("key.key", "rb") as keyFile:
            self.key = keyFile.read()
        self.f = Fernet(self.key)

    def encrypt_dict(self, dictionary):
        f = Encryption().f
        encryptedDict = {str(f.encrypt(bytes(element, encoding="UTF-8-sig"))):
                         str(f.encrypt(
                             bytes(dictionary[element], encoding="UTF-8-sig")))
                         for element in dictionary
                         }
        return encryptedDict

    def decrypt_dict(self, dictionary):
        f = Encryption().f
        decryptedDict = {f.decrypt(bytes(element.strip("'").replace("b'", ""),
                                         encoding="UTF-8-sig")).decode(encoding="UTF-8-sig"):
                         f.decrypt(bytes(dictionary[element].strip("'").replace("b'", ""),
                                         encoding="UTF-8-sig")).decode(encoding="UTF-8-sig")
                         for element in dictionary
                         }
        return decryptedDict

    def encrypt_list(self, listName):
        f = Encryption().f
        encryptedList = [str(f.encrypt(bytes(element, encoding="UTF-8-sig")))
                         for element in listName
                         ]
        return encryptedList

    def decrypt_list(self, listName):
        f = Encryption().f
        decryptedList = [f.decrypt(bytes(element.strip("'").replace(
            "b'", ""), encoding="UTF-8-sig")).decode(encoding="UTF-8-sig")
            for element in listName
        ]
        return decryptedList


class FileSupport:

    def save_file(self, dictToSave, fileName, path=""):
        filePath = "./" + path + str(fileName) + ".json"
        with open(filePath, "w", encoding="UTF-8-sig") as fileJson:
            json.dump(dictToSave, fileJson,
                      ensure_ascii=False, indent=4)

    def read_file(self, fileName, path=""):
        filePath = "./" + path + str(fileName) + ".json"
        with open(filePath, "r", encoding="UTF-8-sig") as fileJson:
            return json.load(fileJson)


encryption = Encryption()
fileSupport = FileSupport()
