#!/usr/bin/env python
import os
from glob import glob
from shutil import rmtree
from zipfile import ZipFile

rmtree('Builds', ignore_errors=True)
os.makedirs('Builds', exist_ok=True)


def build_zips(series_name):
    for folder in os.scandir(series_name):
        folder = folder.path
        zip_name = folder.replace('\\', '/').split('/')[1]
        with ZipFile(f'Builds/{zip_name}.zip', 'w') as zf:
            for file in glob(f'{folder}/**/*.*', recursive=True):
                if not file.endswith('.pak'):
                    new_name = file.replace('\\', '/').split('/', 2)[2]
                    zf.write(file, new_name)


for series in ('Matte Black Series', 'Plexus Series', 'Carbon Fiber Series'):
    build_zips(series)
