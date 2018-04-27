import os
import shutil
import glob
from conda_build import config

wheel_path = os.path.join(config.croot, "ecos_*", "work_moved_ecos*", "dist", "*.whl")
print("Looking for wheel in path matching '{}'".format(wheel_path))
wheel = glob.glob(wheel_path)[0]

shutil.move(wheel, '.')
