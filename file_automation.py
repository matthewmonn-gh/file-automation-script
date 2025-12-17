"""
Base version of the program. 
"""

# Shell Utility. Provides a way for file and directory operations, such as copying and moving.
import shutil

# Hardcoded file to be moved and destination location
source_file = "C:/Users/13605/Downloads/MatthewMonnResume.pdf"
destination_location = "C:/Users/13605/Desktop/DL_Docs"


def move_file(file, location):
    """
    Moves a file from one location to another.

    :param file: File to be moved
    :param location: Location for file to be moved to
    """
    try:
        shutil.move(source_file, destination_location)
        print("File was successfully moved ")
    except:
        print("An error has occurred")


move_file(source_file, destination_location)
