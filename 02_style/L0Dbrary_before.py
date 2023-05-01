
import os

def createDirectory():
    directorypath = os.path.expanduser("~\documents")
    librarypath = os.path.join(directorypath+"\AssetsLib")
    
    if os.path.exists(librarypath) == False:
        pass
    else: 
        os.makedirs(librarypath, exist_ok = True)
        return "Created directory: " + librarypath

def getDirectory():
    directorypath = os.path.expanduser("~\documents")
    librarypath = os.path.join(directorypath+"\AssetsLib")
    if os.path.exists(librarypath):
        return librarypath
    elif os.path.exists(librarypath) == false:
        return librarypath + " Not Found"
    else:
        pass

def assetImport():
    from maya import cmds
    #TODO
    selectedOBJ = None 

    #cmds.file(file path/name, i(import) = True)
    cmds.file(selectedOBJ, i=True)

def assetExport(ExportPath):
    from maya import cmds
    WORKSPACEPATH = cmds.workspace(rootDirectory = True, query=True)
    cmds.workspace(openWorkspace = ExportPath)
    cmds.file(force = True, exportSelected = True, type = "OBJ") 
    cmds.workspace(openWorkspace = WORKSPACEPATH)

def listAssets():
    directorypath = getDirectory()
    assetsList = list(os.listdir(directorypath))
    return assetsList
