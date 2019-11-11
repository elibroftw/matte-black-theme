from zipfile import ZipFile
import os
from shutil import rmtree
from glob import glob

rmtree('Builds', ignore_errors=True)
os.makedirs('Builds')


build_folders = ['Matte Black (Cyan) Theme Firefox', 'Matte Black (Pink) Theme Firefox', 'Matte Black (Blue) Theme Firefox', 'Matte Black (Grey) Theme Firefox', 'Matte Black (Orange) Theme Firefox', 'Matte Black (Red) Theme Firefox', 'Matte Black (Violet) Theme Firefox', 'Matte Black (White) Theme Firefox', 'Dark Knight Joker Theme Firefox']
for folder in build_folders:
    
    with ZipFile(f'Builds/{folder}.zip', 'w') as zf:
        for file in glob(f'{folder}/*'):
            zf.write(f'{file}', os.path.basename(file))


folder = 'Matte Black Theme Chrome'
with ZipFile(f'Builds/{folder}.zip', 'w') as zf:
        for file in glob(f'{folder}/*'):
            zf.write(f'{file}', os.path.basename(file))
        for icon in os.listdir(f'{folder}/icons'):  # add icons to archive
            zf.write(f'{folder}/icons/{icon}', f'icons/{icon}')