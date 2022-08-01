# read text file

file_path='privileges.py'
num=0

# open file scope by read mode
with open(file_path) as file_obj:
    # read() : read all file content
    '''
    content = file_obj.read()
    print(content)
    '''

    # for in obj : read file content one line one time
    '''
    for line in file_obj:
        num+=1
        print(str(num)+": "+line)
    '''
    
    # readlines(): read all lines in file by once
    '''
    lines = file_obj.readlines()

    for line in lines:
        num+=1
        print(str(num)+": "+ line)
    '''

# write file by write mode 
#       if there is no such file , create the file 
#       if there exists the file , clear file 

wfile="test.txt"
'''
with open(wfile,'w') as file_obj:
    file_obj.write("hello , this content write by python code...\n")
    file_obj.write("wow~, this is amazing...\n")
'''

# write file by append mode
with open(wfile,'a') as file_obj:
    file_obj.write("this is append content\n")
    file_obj.write("surjuest to use append mode\n")
