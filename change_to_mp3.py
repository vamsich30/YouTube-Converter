import os
def file_check(base,out_file,ext):
    new_file = base + ext
    if os.path.exists(new_file):
        count = 1
        while os.path.exists(base + str(count) + ext):
            count+=1
        new_file = base +" - "+str(count) + ext
    os.rename(out_file,new_file)
    print("(•‿•)successfully Downloaded(•‿•)")
