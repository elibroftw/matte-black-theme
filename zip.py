from zipfile import ZipFile
import os
from shutil import rmtree
from glob import glob

rmtree('Builds', ignore_errors=True)
os.makedirs('Builds')

colors = {'Cyan', 'Pink', 'Blue', 'Classic Blue', 'Grey', 'Orange', 'Red', 'Violet', 'White'}
colors = {f'Matte Black ({color}) Theme Firefox' for color in colors}
build_folders = {'Dark Knight Joker Theme Firefox', 'Plexus Crystals Firefox', 'Plexus Lines Firefox', 'Plexus Beams Firefox'}.union(colors)
for folder in build_folders:
    with ZipFile(f'Builds/{folder}.zip', 'w') as zf:
        for file in glob(f'{folder}/*'):
            zf.write(f'{file}', os.path.basename(file))


chrome_folders = {'Matte Black Theme Chrome', 'Plexus Crystals Chrome'}
for folder in chrome_folders:
    with ZipFile(f'Builds/{folder}.zip', 'w') as zf:
        zf.write(f'{folder}/manifest.json', os.path.basename(file))
        if os.path.exists(f'{folder}/images'):
            for image in os.listdir(f'{folder}/images'):  # add images to archive
                zf.write(f'{folder}/images/{image}', f'images/{image}')
        for icon in os.listdir(f'{folder}/icons'):  # add icons to archive
            zf.write(f'{folder}/icons/{icon}', f'icons/{icon}')