import os
def change_extension(loc,extension):
    # Going through the dir
    for path,subdirs,files in os.walk(loc):
        if(len(files) != 0):
            curr_ext = files[0].split('.')[1]
            # Obtain the file names without the extension that are to have their ext changed
            f_names = [ f.split('.')[0] for f in files]
            # do rename op
            for f in f_names:
                os.rename(path+'/'+f+'.'+curr_ext,path+'/'+f+extension)
change_extension('test data/','.d')