
import os
from maya import cmds

#create directory
DIRECTORY   = os.path.expanduser("~\documents")
LIBRARYPATH = os.path.join(DIRECTORY + "\AssetsLib")

def createDirectory():
    #Creates a directory to store all assets and returns path to it
    if not os.path.exists(LIBRARYPATH):
        os.makedirs(LIBRARYPATH, exist_ok = True)
        return "Created directory: " + LIBRARYPATH
    return LIBRARYPATH + " Exists already"


def getDirectory():
    if os.path.exists(LIBRARYPATH):
        return LIBRARYPATH
    else:
        return LIBRARYPATH + " Not Found"


def assetImport():
    #need to find a way for the PySide UI button to return path+name of the selected object
    selectedOBJ = None 
    cmds.file(selectedOBJ, i = True)


def assetExport(ExportPath):
    #this saves to the project folder which is not ideal...
    WORKSPACEPATH = cmds.workspace(rootDirectory = True, query = True)
    #switch to the LIBRARYPATH which was passed into this func as a parameter
    cmds.workspace(openWorkspace = ExportPath)
    #exports the selected object as an OBJ
    cmds.file(force = True, exportSelected = True, type = "OBJ") 
    #switch back to workspace
    cmds.workspace(openWorkspace = WORKSPACEPATH)

def listAssets():
    #find a way to return list of assets from our designated assets folder
    directoryPath = getDirectory()
    assetsList    = list(os.listdir(directoryPath))
    return assetsList
