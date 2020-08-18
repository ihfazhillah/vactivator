import os


def activate(path: str):
    ret_code = os.system(f"bash --rcfile {path}")
    if ret_code == 0:
        print("success")
    else:
        print(f"Error with status: {ret_code}")
