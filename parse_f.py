import os

path = input('Insira o caminho do arquivo: ')

file_status = os.path.isfile(path)

if(file_status):
        # Arrays for storing data
    contents = []
    important = []
        # Opening the file  
    with open(path) as f:
        contents = f.readlines()
        for line in contents:
            if '->' in line:
                important = contents

    f.close()

    count = 0
    output = []
        # Going through file contents
    for content in important:
        count += 1
            # Splitting values for another array loop
        splitted = content.split()
        for index in splitted:
                # searching for arrows in array string
            search = index.find('->')
                # >= because it returns position of, -1 for "false"
            if (search >= 0):
                output = index
                print(f'{count}: {output}')
        
        # Empty output
    if not output:
        print('Nothing to show from file.')
else:
    print(f'File not found.\nCheck the inserted path: {path}')
