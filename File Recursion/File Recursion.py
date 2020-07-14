# Boilerplate Template for the this problem was used

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
   
    # CHeck whether the specified path exists or not
    
    if not os.path.isdir(path):
        if suffix in path:
            return [path]

        else:
            return []
      

    List_of_path = os.listdir(path)
    path_list = []

    for i in List_of_path:
        i_path = os.path.join(path, i)
        #print(i_path)

        if os.path.isdir(i_path):
            path_list = path_list + find_files(suffix, i_path)

        if os.path.isfile(i_path) and i_path.endswith(suffix):
            path_list.append(i_path)

            	
    return path_list

#path = "./testdir"

# The print functions below tests the algorithm
print(find_files('.c', 'testdir'))
print(find_files('.z', 'testdir'))
print(find_files('.c', ''))
print(find_files('.c', 'testdir/subdir5'))
print(find_files('.py', './solution/problems2/problems2.py'))

