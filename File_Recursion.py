"""
Finding Files
For this problem, the goal is to write code for finding 
all files under a directory (and all directories beneath it) 
that end with ".c"

"""

import os 




def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if path == None:
          return None
    
    if not os.path.exists(path):
          print("File Doesnt exist")
          return None
    
    file_list = []

    dir_list = os.listdir(path)
    # get files benaat the given path
    for item in dir_list:
          temp_path = os.path.join(path,item)

          #check if it not a file recurse the function
          # else check with the file ends with ".c"
          #and get the path to that file and add to  list
          
          #print("Temp File", temp_path)
          
          if os.path.isfile(temp_path) and temp_path.endswith(suffix):
                #print("Temp XFile", temp_path)
                file_list.append(temp_path)
                #print("LIIST File", file_list)
          elif os.path.isdir(temp_path):
                file_list += find_files(suffix, temp_path)


    return file_list



# test 


# should print a list of files ending in .c
print(find_files(".c", 'C:\\Users\\IAN CECIL AKOTO\\Desktop\\Data Structures and Algorithm\\Show me your data Sctructure\\testdir'))