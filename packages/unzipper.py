from zipfile import ZipFile
with ZipFile("./packages/temp.zip", 'r') as zObject:
    zObject.extractall(path="/packages/temp")