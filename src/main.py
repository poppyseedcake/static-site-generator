import os
import shutil
from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

#    copy_static_to_public()    

#def copy_static_to_public():    
#    if os.path.exists("./public/"):
#        print(f"Removing ./public/")
#        shutil.rmtree("./public/")
#        print(f"Creating new folder ./public")
#        os.mkdir("./public")
#    list_static("", "")
#    return
#
#def list_static(base_path, next_path):
#    abs_path = os.path.join("./static/", base_path, next_path)    
#    rel_path = os.path.join(base_path, next_path)
#    dir = os.listdir(abs_path)
#    for element in dir:
#        element_path = os.path.join(abs_path, element)
#        if os.path.isfile(element_path):
#            public_path = os.path.join("./public", rel_path)
#            if not os.path.exists(public_path):
#                print(f"Creating public path: {public_path}")
#                os.mkdir(public_path)
#            print(f"Copy {element} from {abs_path} to {public_path}")
#            shutil.copy(element_path, public_path)            
#        else:
#            print(f"found folder: {element_path}")
#            list_static(rel_path, element)
#    return

if __name__ == "__main__":
    main()
