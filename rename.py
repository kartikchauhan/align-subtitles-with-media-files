import sys,os

src_dir = raw_input("Enter the src directory: ")
str_name = {}
str_ext = {}
subtitle_name ={}
subtitle_ext = {}
str_index = 0
subtitle_index = 0
num_subtitles = int(raw_input("Enter number of subtitles that exist for a single episode in the directory: "))
subtitles_set_index = int(raw_input("Enter which set of subtitles you want to align with your media files: "))
path,dirs,files = os.walk(src_dir).next()
for i in files:
    filename,file_ext = os.path.splitext(i)
    if(file_ext=='.avi' or file_ext=='.mp4' or file_ext=='.mpeg' or file_ext=='.mkv'):
        str_name[str_index] = filename
        str_ext[str_index] = file_ext
        str_index+=1
    elif(file_ext=='.srt'):
        if(subtitle_index%num_subtitles==(subtitles_set_index-1)):
            subtitle_name[subtitle_index] = filename
            subtitle_ext[subtitle_index] = file_ext
        subtitle_index+=1
            
subtitle_index = subtitles_set_index-1

for i in range(0,str_index):
    path_str_name = os.path.join(path,str_name[i])
    path_str_name = path_str_name + subtitle_ext[subtitle_index]    
    path_subtitle_name = os.path.join(path,subtitle_name[subtitle_index])
    path_subtitle_name = path_subtitle_name + subtitle_ext[subtitle_index]    
    print "path_str_name = {}".format(path_str_name)
    print "path_subtitle_name={}".format(path_subtitle_name)
    os.rename(path_subtitle_name,path_str_name)
    print subtitle_index
    subtitle_index+=num_subtitles


    
    
    
