import os

    # colors
yellow = '\033[93m'
cyan =  '\033[96m'
white = '\033[00m'

path = input('Insert path to file: ')
search_string = input('Insert text to search: ')

file_status = os.path.isfile(path)

if(file_status):
        # Arrays for storing data
    contents = []
    important = []
        # Opening the file  
    with open(path) as f:
        contents = f.readlines()
        for line in contents:
            if search_string in line:
                important = contents

    f.close()

    output = [] 
    if(important):
        count = 0
            # Going through file contents
        for content in important:
            count += 1
                # Splitting values for another array loop
            splitted = content.split()
            for index in splitted:
                    # searching in array string
                search = index.find(search_string)
                    # >= because it returns position of, -1 for "false"
                if (search >= 0):
                    output = index
                    print(f'{yellow}{count}: {cyan}{output}{white}')
        
        # Empty output
    if not output:
        print(cyan + 'Nothing to show from file.' + white)
else:
    print(f'{yellow}File not found.\nCheck the inserted path: {cyan}{path}{white}')
