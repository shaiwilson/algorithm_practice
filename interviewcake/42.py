""" 
Write a function that returns a list of all the 
duplicate files. We'll check them by hand before actually deleting them, 
since programmatically deleting files is really scary. 
To help us confirm that two files are actually duplicates, 
return a list of tuples where:

the first item is the duplicate file
the second item is the original file

"""

import os 

# print current working directory
# relative - starts from the curr dir
# absolute - starts from the topmost file in a file system
pwd = os.getcwd()
print pwd



def find_duplicates(starting_dir):
    # start in the current dir and walk downward
    

    # a dict to hold the files seen already
    uniq_filenames = {}
    stack = [starting_dir]

    # track duplicates (dulicate, original)
    duplicates = []


    while len(stack):
        for(dirname, dirs, files) in os.walk('.'):

            curr_path = stack.pop
            # if it is a dir add it to the stack
            if os.path.isdir(curr_path):
                for path in os.listdir(curr_path):
                    full_path = os.path.join(current_path, path)
                    stack.append(full_path)
            # if it is a file
            else:
                with open(curr_path) as file:
                    file_contents = file.read()

                # get the last edited item
                current_last_edited_time = os.path.getmtime(current_path)

            if file_contents in uniq_filenames:
                existing_last_edited_time, existing_path = files_seen_already[file_contents]
                if current_last_edited_time > existing_last_edited_time:
                    duplicates.append((current_path, existing_path))
                else:
                    # old file is the duplicate
                    dupplicates.append((existing_path, current_path))

                    # update uniq files to have new file info
                    uniq_filenames[file_contents] = \
                        (current_last_edited_time, current_path)

            else:
                # new file
                uniq_filenames[file_contents] = \
                    (current_last_edited_time, current_path)
    return duplicates


            



        # if it is a directory
        # put the contents in the stack

        



