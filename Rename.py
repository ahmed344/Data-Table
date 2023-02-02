import os
import pathlib

# Rename all the directories of the directories in the directory Data/Cells/
for directory in os.listdir('Data/Cells/'):
    for path in pathlib.Path('Data/Cells/{}'.format(directory)).iterdir():
        # Make sure the path is a directory
        if path.is_dir():
            # Rename the directory by modifying the old name
            print(path.name, ' --> ', path.name.replace('|','='))
            path.rename(pathlib.Path(path.parent, path.name.replace('|','=')))

# Rename all the directories in the directory Data/Cells/
for path in pathlib.Path('Data/Cells/').iterdir():
    # Make sure the path is a directory
    if path.is_dir():
        # Rename the directory by modifying the old name
        print(path.name, ' --> ', path.name.replace('cells','SHC'))
        path.rename(pathlib.Path(path.parent, path.name.replace('cells','SHC')))