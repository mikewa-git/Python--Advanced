# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):
    #creating dictionary with 'color' keys and corresponding values to use in for loop
    color_dict = {
        1:4,
        2:13,
        3:25,
        4:17,
        5:17,
        6:15,
        7:6,
        8:16
    }
    
    for ctrlName in ctrlList:
        #Shape.overrideEnabled for each ctrlName in ctrlList
        mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)  
        
        #iterate through items in color_dict and if the key matches the color argument value then the color_dict's "values" is matched
        for key, values in color_dict.items():
            if key == color:
                mc.setAttr(ctrlName + 'Shape.overrideColor', values)



# EXAMPLE
# set_color(['circle','circle1'], 8)
#for ctrlnames in 'circle','circle1'
