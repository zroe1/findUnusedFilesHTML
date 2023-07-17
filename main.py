import os

VALID_FILE_ENDINGS = ['.jpg', '.jpeg', '.png', '.html', '.css', '.js', '.pdf',
                      'ico',]

def get_all_paths(current_path , all_files):
    in_dir = os.listdir(current_path)
    files_in_dir = []
    directories = []

    for file in in_dir:
        if os.path.isdir(file):
            directories.append(current_path + '/' +  file)
        
        for ending in VALID_FILE_ENDINGS:
            if ending in file:
                files_in_dir.append(current_path + '/' + file)
                break

    all_files += files_in_dir
    for directory in directories:
        get_all_paths(directory, all_files)

def main():
    current_dir_path = '.'
    all_text = ''
    all_files = []
    get_all_paths(current_dir_path, all_files)

    print('\nAll files:\n' +  str(all_files) + '\n')

    for file in all_files:
        with open(file, 'r') as file:
            all_text += file.read()

    print('Unused files:')
    for file in all_files:
        if not file in all_text:
            print(file)
    print()

if __name__ == '__main__':
    main()
