from zipfile import ZipFile
import os
from shutil import rmtree
from glob import glob

rmtree('Builds', ignore_errors=True)
os.makedirs('Builds')


for folder in glob('Matte Black *'):
    if folder != ('Matte Black Theme Resources'):
        with ZipFile(f'Builds/{folder}.zip', 'w') as zf:
            for file in glob(f'{folder}/*'):
                zf.write(f'{file}', os.path.basename(file))
