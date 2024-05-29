import os
import shutil

def recursive_copy(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError("Invalid source directory")
    
    if not os.path.exists(dst):
        raise FileNotFoundError("Invalid destination directory")
    
    shutil.rmtree(dst)
    
    dirs = os.listdir(src)

    for dir in dirs:
        if not os.path.isfile(dir):
            next_dst = os.path.join(dst,dir)
            os.mkdir(next_dst)
            recursive_copy(os.path.join(src,dir), next_dst)
        shutil.copy(os.path.join(src,dir), dst)
        print("Copied: " + os.path.join(src,dir))
