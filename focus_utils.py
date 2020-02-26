''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = []  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

# from util_submodules.focus_utils import focus_utils as fu                  ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''



import subprocess
import os


# DONT DELTE UNTIL YOU KNOW NEW ONE WORKS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import win32gui
# import re
# 
# 
# class WindowMgr:
#     """Encapsulates some calls to the winapi for window management"""
# 
#     def __init__ (self):
#         """Constructor"""
#         self._handle = None
# 
#     def find_window(self, class_name, window_name=None):
#         """find a window by its class_name"""
#         self._handle = win32gui.FindWindow(class_name, window_name)
# 
#     def _window_enum_callback(self, hwnd, wildcard):
#         """Pass to win32gui.EnumWindows() to check all the opened windows"""
#         if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
#             self._handle = hwnd
# 
#     def find_window_wildcard(self, wildcard):
#         """find a window whose title matches the wildcard regex"""
#         self._handle = None
#         win32gui.EnumWindows(self._window_enum_callback, wildcard)
# 
#     def set_foreground(self):
#         """put the window in the foreground"""
#         win32gui.SetForegroundWindow(self._handle)
# 
# 
# def set_foreground(window_title):
#     w = WindowMgr()
#     w.find_window_wildcard(window_title)
#     w.set_foreground()

def set_foreground(window_title):
# '''#     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line
# # 
# #     print(os.path.dirname())'''

    sendkeys_path = os.path.dirname(os.path.abspath(__file__)) + '//sendkeys.bat'
#     cmd = 'call sendkeys.bat "' + window_title + '" ""'
    cmd = 'call ' + sendkeys_path + ' "' + window_title + '" ""'
    subprocess.call(cmd, shell = True)



''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':
    print('In Main:  focus_utils')
    
    
    
    set_foreground('Explorer')
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  focus_utils')


