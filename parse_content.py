import os
import glob
import shutil
import sys

default_directories = ['members', 'highlights', 'presentations', 'projects', 'software', 'vacancies', 'calendar', 'publications', 'research']
optional_directories = ['courses']

directories = default_directories + optional_directories
site = sys.argv[1]
group_name = site[8:]

print(f"Copying content for {site} (group: {group_name})")

for dir in default_directories:
    output_dir = os.path.join(site, dir)
    print(output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

for dir in directories:
    output_dir_ = os.path.join(site, dir)
    print(output_dir_)
    if not os.path.isdir(output_dir_):
        print('huh')
        continue

    files = glob.glob(os.path.join('content', 'pages', dir, '*.md'))

    for file_path in files:
        filename = os.path.basename(file_path)
        with open(file_path) as file:
            try:
                for line in file:
                    if 'groups:' in line:

                            groups = line.split(':')[1].replace(' ','').rstrip().split(',')

                            # Check if the content belongs to the current website
                            if group_name in groups:
                                if dir == 'highlights':
                                    # Write hightlights to directory out of pages dir
                                    out_dir = os.path.join(site, 'content', dir)
                                else:
                                    out_dir = os.path.join(site, 'content', 'pages', dir)

                                if not os.path.exists(out_dir):
                                    os.makedirs(out_dir)
                                shutil.copyfile(file_path, os.path.join(out_dir, filename))
  


                            # Stop parsing file
                            break
            except Exception as e:
                print(f"Error parsing {file_path}.")
                print(e)

        


print(f'Copied pages to {site}.')
