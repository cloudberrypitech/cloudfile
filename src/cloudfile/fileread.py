myvar = []

def read_file(filepath, storage_var=None):
    with open(filepath, "r") as file:
        contents = file.read()

    if storage_var is None:
        return contents

    storage_var[:] = [contents]


class Testing:
    def __init__(self):
        pass
    def test_code(self):
        test = read_file("src/cloudfile/__init__.py")
        print(test)
        print("+++++++")

        read_file("src/cloudfile/__init__.py", myvar)
        print(*myvar, sep="")
