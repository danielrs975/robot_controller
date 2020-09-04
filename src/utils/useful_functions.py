'''
In here we implement some useful functions that
we can use across all the project
'''

def is_modified(old_time, new_time):
    '''
    This function returns a boolean to recognize if
    a file has been modified
    Parameters:
        - old_time (Float) --> The time (In seconds) of the old file
        - new_time (Float) --> The time (In seconds) of the new file
    Returns:
        - True if the file has been modified
        - False otherwise
    '''
    return new_time > old_time