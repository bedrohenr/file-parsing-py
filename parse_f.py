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
    with open(path, "r", encoding="utf-8") as f:
        contents = f.readlines()
        for line in contents:
            if search_string in line:
                important = contents
        # Closing the file
    f.close()

    if(important):
            # Store the line number and text that matches
        lines = []
        found = []

            # Counting the lines
        count = 0
            # Going through file contents
        for content in important:
            count += 1
                # Splitting values for another array loop
            search = content.find(search_string)
                # >= because it returns position of, -1 for "false"
            if (search >= 0):
                # Appending to variables (line number and matching text)
                found.append(content)
                lines.append(count)

    for line_number, line_text in zip(lines, found):
        # Searching for line break in text
        if (line_text.find('\n')):
            # True case it will let the text break the line itself with the arg end=""
            print(f'{yellow}{line_number}: {cyan}{line_text}{white}', end = "")
        else:
            # False will print each in its own line
            print(f'{yellow}{line_number}: {cyan}{line_text}{white}')
        
        # Empty output
    if not found:
        print(cyan + 'Nothing to show from file.' + white)
else:
    # Case wrong path is given or file doesnt exist
    print(f'{yellow}File not found.\nCheck the inserted path: {cyan}{path}{white}')
