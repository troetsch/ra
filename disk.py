######################################
# shutil                             #
######################################

import shutil
 
total, used, free = shutil.disk_usage("/")
 
print("Total:", total // (1024**3), "GB")
print("Used:", used // (1024**3), "GB")
print("Free:", free // (1024**3), "GB")
