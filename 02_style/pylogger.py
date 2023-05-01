# STYLE ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    frame = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if frame:
        frame = frame.f_back
    
    while hasattr(frame, "f_code"):
        co = frame.f_code
        filename = os.path.normcase(co.co_filename)
        
        if filename == _srcfile:
            frame = frame.f_back
        else:
            return (co.co_filename, frame.f_lineno, co.co_name)

    return ("(unknown file)", 0, "(unknown function)")

# How can we make this code better?
