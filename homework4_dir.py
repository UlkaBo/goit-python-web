# в потоки уходят только рекурсивные вызовы разбора папки
from pathlib import *
import sys
import re
import shutil
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread
MAX_THREAD = 5

# ------ заготовки для создания словаря расширений

images = '.jpg .png .jpeg .svg .gif .eps'.split()
video = '.avi .mp4 .mov .mkv'.split()
documents = '.doc .docx .txt .pdf .xlsx .pptx .odt'.split()
audio = '.mp3 .ogg .wav .amr'.split()
archives = '.zip .gz .tar'.split()
progrs = '.py'.split()
another = ' '.split()
list_ext = ['images', 'video', 'documents',
            'audio', 'archives', 'progrs', 'another']

# ------конец  заготовки для создания словаря расширений


def parse_folder(path, path_dir, dict_ext):
    if not list(path.iterdir()):
        path.rmdir()
        return
    with ThreadPoolExecutor(max_workers=MAX_THREAD) as executor:
        for new_el in path.iterdir():
            fromm = new_el
            if new_el.is_dir():

                # разные способы склеивания пути
                # p = path.joinpath(new_el.name)  # p  = path / new_el.name

                if new_el.name not in list_ext or len(new_el.parts) > 2:
                    
                    future = executor.submit(parse_folder, new_el, path_dir, dict_ext )
                    future.result()
                    #parse_folder(new_el, path_dir, dict_ext)
                    
            else:

                # если это архив, то добавляю к пути подпапку с именем new_el.stem

                if new_el.suffix in archives:
                    #future = executor.submit(
                    #    unpacking, new_el, path_dir, dict_ext)
                    #future.result()
                    unpacking(new_el, path_dir, dict_ext)

                elif new_el.suffix in dict_ext:
                    # запоминаю путь к файлу в директории, куда хочу перенести
                    too = path_dir / dict_ext[new_el.suffix] / new_el.name
                    while too.is_file():
                        new_el = Path('-'.join(new_el.parts))
                        too = path_dir / dict_ext[new_el.suffix] / new_el.name
                    fromm.rename(too)

                else:
                    too = path_dir / 'another'/new_el.name
                    while too.is_file():
                        new_el = Path('-'.join(new_el.parts))
                        too = path_dir / 'another'/new_el.name
                    fromm.rename(too)
  
    if not list(path.iterdir()):
        path.rmdir()
        return


def unpacking(new_el, path_dir, dict_ext):

    # сейчас правильный (рабочий) путь к файлу(директории) - new_el, это объект Path
    too = path_dir / 'archives' / new_el.stem
    # распаковываю в too
    try:
        shutil.unpack_archive(str(new_el), str(too))
    except :
        print('ups...')

    # удаляю сам архив
    new_el.unlink()


def main():
    dir_name = sys.argv[1]
    path_dir = Path(dir_name)
    # -------create a dictionary  - extantion : directory
    #        and create directories
    start_time = time.time()
    dict_ext = {}

    if not (path_dir / 'unknows').exists():
        Path.mkdir(path_dir / 'unknows')
    for el in list_ext:
        l = eval(el)
        if not (path_dir / el).exists():
            Path.mkdir(path_dir / el)
        dict_ext.update(dict(zip(l, [el] * len(l))))

    # -------  end of create a dictionary

    parse_folder(path_dir,  path_dir, dict_ext)
    end_time = time.time()
    print(f'I spend time {end_time-start_time} with {MAX_THREAD} threads ')


if __name__ == '__main__':
    main()
