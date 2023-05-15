import time
import yaml
from datetime import datetime
import utils
 


# date object
now = datetime.now()

# dd/mm/YY H:M:S
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

# **********************************************************
# DECORATORS

# Return name and elapsed time
def status(f):
    def wrapper(*args, **kwargs):
        timestart = time.time()
        
        f(*args, **kwargs)                  # main_function
        
        time_elapsed = round(time.time() - timestart,2)   #round it off to read easier
        print(f'"{f.__name__}" took {time_elapsed} seconds to execute') 
    return wrapper

# **********************************************************
# CLASS

class Asset():
    """
    DESCRIPTION
        storing asset data to be used in exporting/importing process and for cataloguing purposes.

    TODO
        - Get size of asset
        - Get asset name from Maya
        - Store thumbnail image
        -
    """    

    def __init__(self, name, translate, rotate, scale):
        self.name = name
        self.translate = translate
        self.rotate = rotate
        self.scale = scale
        self.date = current_time

    # write file with asset data    
    @status
    def print_metadata(self):   #print out yaml file
        # export path
        write_path = f"{utils.get_assetlib_path()}\{self.name}\metadata.yaml"
        time.sleep(1)
        asset_data = [{"Name": self.name}, {"Date": self.date}, {"Translate":self.translate}, {"Rotate":self.rotate}, {"Scale":self.scale}]
        print(asset_data)

        with open(write_path, "w") as output_file:
            yaml.dump(asset_data, output_file, default_flow_style = False, allow_unicode = True)
  
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

obj = Asset(name = "asset01", translate = [0,0,0], rotate = [0,0,0], scale = [1,1,1])
obj.print_metadata()
print(obj.get_name())
print(obj.get_date())
