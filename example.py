from encryption import encryption, fileSupport
import os

os.chdir(os.path.dirname(__file__))

sampleDict = {"1": "text", "2": "also text"}
sampleList = ["name1", "name2", "name3"]

print("Dictionary and list to encrypt:")
print(sampleDict)
print(sampleList)

# encryption
print()
print("Encrypted dictionary:")
encryptedDict = encryption.encrypt_dict(sampleDict)
print(encryptedDict)
print()
print("Encrypted list:")
encryptedList = encryption.encrypt_list(sampleList)
print(encryptedList)

print()
# save encrypted JSON files
fileSupport.save_file(encryptedDict, "fileName", path="directory/")
fileSupport.save_file(encryptedList, "listName", path="directory/")

# read and decrypt JSON files
print("Read and decrypted dictionary from JSON file:")
decryptedDict = encryption.decrypt_dict(
    fileSupport.read_file("fileName", path="directory/"))
print(decryptedDict)

print("Read and decrypted list from JSON file:")
decryptedList = encryption.decrypt_list(
    fileSupport.read_file("listName", path="directory/"))
print(decryptedList)
