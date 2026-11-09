myvar = []
def read_file(filepath, storage_var=None):
    if storage_var == None:
        with open(filepath, "r") as file:
            return file.read()
    else:
        with open(filepath, "r") as file:
            initvar = file.read()
            nvar = initvar.splitlines("\n")
            storage_var = nvar


test = read_file("src/cloudfile/__init__.py")
print(test)
print("+++++++")

read_file("src/cloudfile/__init__.py", myvar)
print(myvar)