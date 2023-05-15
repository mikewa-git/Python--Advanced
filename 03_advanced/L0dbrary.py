# My maya doesn't seem to pick up any python packages unless I execute these two lines first
import sys 
sys.path.append( 'C:\\Users\\Mike\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages' )

import os
import re
import time
import yaml

from maya import cmds
from datetime import datetime

# *********************************************************
# VARIABLES

DIRECTORY   = os.path.expanduser("~Documents")
LIBRARYPATH = os.path.join(DIRECTORY + "\AssetsLib")

# Select mesh
target_mesh = cmds.ls(selection=True)[0]

# Date object formatted to D:M:Y H:M:S
current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# *********************************************************
# FUNCTIONS

# Creates AssetLib directory
def create_assetlib_directory(): 
    if not os.path.exists(LIBRARYPATH):
        os.makedirs(LIBRARYPATH, exist_ok = True)
        return f"Created directory: {LIBRARYPATH}"
    return f"{LIBRARYPATH} Exists already"

# Get suffix in case "example_01" already exists
def get_suffix(file):
    try:
        dirlist = os.listdir(LIBRARYPATH)
        newlist = []
        
        for each in dirlist:
            if file in each:
                newlist.append(each)
            else: pass
            
        match = re.compile(r"_\d{2}$")
        suffix_match = [int(match.search(name).group()[1:]) for name in newlist if match.search(name)]
        highest_suffix = max(suffix_match)
        
        return int(highest_suffix)
    except ValueError:
        return "ValueError: Please check AssetLib for proper suffixes"

# Create the slot to store metadata/ .ma files
def create_asset_slot(asset):
    suffix = 1
    filename = f"{LIBRARYPATH}\\{asset}_{suffix:02}"
    
    if not os.path.exists(filename):
        print("NO matching directory exists, creating new one")
        os.makedirs(filename, exist_ok = True)
        return os.path.join(f"{LIBRARYPATH}\\{asset}_{suffix:02}")
    
    else:
        print("Matching directory exists, creating new instance")
        suffix = get_suffix(asset) + 1
        filename = f"{LIBRARYPATH}\\{asset}_{suffix:02}"

        os.makedirs(filename, exist_ok = True)
        return f"{LIBRARYPATH}\\{asset}_{suffix:02}"
    
def status(f):
    def wrapper(*args, **kwargs):
        timestart = time.time()
        
        f(*args, **kwargs)    # function
        
        time_elapsed = round(time.time() - timestart,2)    # round off for readability
        print(f'"{f.__name__}" took {time_elapsed} seconds to execute') 
    return wrapper

def export_asset(path):
    #export to path
    cmds.file(f"{path}//{target_mesh}",force=True, exportSelected = True, type = "mayaAscii") 

# **********************************************************
# CLASS

class Asset():
    """ 
    My code is not complete but I think incorporating classes will be beneficial because I would like the ability to eventually export
    made out of several different meshes which will require me to store data on each of those parts
    """
    def __init__(self, name, translate, rotate, scale):
        self.name = name
        self.translate = translate
        self.rotate = rotate
        self.scale = scale
        self.date = current_time

    @status
    # Writing out a yaml file to store data like name, transforms, and date.
    # This can be used later when I implement ability to swap assets while retaining the position in world space
    def write_metadata(self, write_path):   
        asset_data = [{"Name": self.name}, {"Date": self.date}, {"Translate":self.translate}, {"Rotate":self.rotate}, {"Scale":self.scale}]

        with open(write_path, "w") as output_file:
            yaml.dump(asset_data, output_file, default_flow_style = None, allow_unicode = True)
  
    def get_name(self):
        return self.name


# *********************************************************
# TESTING

# Create AssetLib folder
create_assetlib_directory()
# Creating Asset instance
obj = Asset(name = f"{target_mesh}", translate = cmds.getAttr(f"{target_mesh}.translate"), rotate = cmds.getAttr(f"{target_mesh}.rotate"), scale = cmds.getAttr(f"{target_mesh}.scale"))
# Get asset folder path
asset_path = create_asset_slot(obj.get_name())
# Calling create_asset_slot() and dumping yaml file in new slot
obj.write_metadata(f"{asset_path}\\{obj.get_name()}_metadata")
# Maya export selected as .ma
export_asset(asset_path)
