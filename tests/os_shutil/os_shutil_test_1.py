import os
import shutil

src = "/Users/christian.gentry/Desktop/_from"
dest = "/Users/christian.gentry/Desktop/_to"

src_files = os.listdir(src)

for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)
