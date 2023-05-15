import os

"""
MODULE FOR L0DBRARY FUNCTIONS

FUNCTIONS
    create_assetlib_directory
    getDirectory
    listAssets
"""

# **********************************************************
# VARIABLES

DIRECTORY   = os.path.expanduser("~\documents")
LIBRARYPATH = os.path.join(DIRECTORY + "\AssetsLib")

# *********************************************************
# FUNCTIONS

def main():
    ...

def create_assetlib_directory():
    #Creates a directory to store all assets and returns path to it
    if not os.path.exists(LIBRARYPATH):
        os.makedirs(LIBRARYPATH, exist_ok = True)
        return f"Created directory: {LIBRARYPATH}"
    return f"{LIBRARYPATH} Exists already"

def create_asset_slot(asset):
    if not os.path.exists(f"{LIBRARYPATH}\\{asset}"):
        os.makedirs(f"{LIBRARYPATH}\\{asset}", exist_ok = True)
        return f"Created directory: {LIBRARYPATH}\\{asset}"
    return f"Created directory: {LIBRARYPATH}\\{asset}"

def get_assetlib_path():
    if os.path.exists(LIBRARYPATH):
        return LIBRARYPATH
    else:
        return f"{LIBRARYPATH} Not Found"

def listAssets():
    #
    return list(os.listdir(LIBRARYPATH))

# **********************************************************

if __name__ == "__main__":
    main()