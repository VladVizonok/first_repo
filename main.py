import re
from pathlib import Path
import shutil
import sys
import  normalize

main_folder = Path(sys.argv[1])

# Створюємо папки для сортування.
folder_list = ['images', 'video', 'documents', 'audio', 'archive', 'other']

image_dir = Path(f'{main_folder}/images')
image_dir.mkdir(exist_ok=True)

video_dir = Path(f'{main_folder}/video')
video_dir.mkdir(exist_ok=True)

documents_dir = Path(f'{main_folder}/documents')
documents_dir.mkdir(exist_ok=True)

audio_dir = Path(f'{main_folder}/audio')
audio_dir.mkdir(exist_ok=True)

archive_dir = Path(f'{main_folder}/archive')
archive_dir.mkdir(exist_ok=True)

other_dir = Path(f'{main_folder}/other')
other_dir.mkdir(exist_ok=True)

# Створюємо словник розширень
folder_dict = {
    'image' : ['JPEG', 'PNG', 'JPG', 'SVG'],
    'video' : ['AVI', 'MP4', 'MOV', 'MKV'],
    'documents' : ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'audio' : ['MP3', 'OGG', 'WAV', 'AMR'],
    'archive' : ['ZIP', 'GZ', 'TAR'],
}

def get_extencion(file_name):
    return Path(file_name).suffix[1:].upper()

def manage_archive(archive_name, extencion):

    # Нормалізуємо імʼя архіву та видаляємо формат файлу для створення імʼя папки 

    new_archive_name = normalize.normalize(archive_name).replace(f'.{extencion.lower()}', '') 
    archive_folder = archive_dir/new_archive_name
    archive_folder.mkdir(exist_ok=True)

    # Розпаковуємо архів 

    try:
        shutil.unpack_archive(str(archive_name.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    archive_name.unlink()

def remove_empty_folder(folder_name):
    for item in folder_name.iterdir():
        if item.is_dir() and item.name not in folder_list:
            remove_empty_folder(item)
            try:
                item.rmdir()
            except FileNotFoundError:
                pass
            except OSError:
                pass
                
def scan(folder_name):
    # Створюємо списки для статистики
    image_list = []
    video_list = []
    documents_list = []
    audio_list = []
    archive_list = []
    known_extension_list = set()
    unknown_extension_list = set()

    # Сортуємо імʼя значень залежно від розширення 
    image_path = Path(folder_name/'images')
    for file in image_path.iterdir():
        image_list.append(file.name)
        known_extension_list.add(get_extencion(file))

    video_path = Path(folder_name/'video')
    for file in video_path.iterdir():
        video_list.append(file.name)
        known_extension_list.add(get_extencion(file))

    documents_path = Path(folder_name/'documents')
    for file in documents_path.iterdir():
        documents_list.append(file.name)
        known_extension_list.add(get_extencion(file))

    audio_path = Path(folder_name/'audio')
    for file in audio_path.iterdir():
        audio_list.append(file.name)
        known_extension_list.add(get_extencion(file))

    archive_path = Path(folder_name/'archive')
    for file in archive_path.iterdir():
        archive_list.append(file.name)
        known_extension_list.add(get_extencion(file))

    other_path = Path(folder_name/'other')
    for file in other_path.iterdir():
        image_list.append(file.name)
        unknown_extension_list.add(get_extencion(file))

    print("Image List:", image_list, sep='\n')
    print("Video List:", video_list, sep='\n')
    print("Documents List:", documents_list, sep='\n')
    print("Audio List:", audio_list, sep='\n')
    print("Archive List:", archive_list, sep='\n')
    print("Known Extensions List:", known_extension_list, sep='\n')
    print("Unknown Extensions List:", unknown_extension_list, sep='\n')

def main(folder_for_sort):
    for file in folder_for_sort.iterdir():
        try:
            if file.name in folder_list:
                continue

        # Рекурсивно перевіряємо папки та видаляємо пусті
            if file.is_dir:
                try:
                    main(file)
                except NotADirectoryError:
                    pass
            remove_empty_folder(folder_for_sort)

        # Сортуємо файли за їх розширеннями 

            if get_extencion(file) in folder_dict['image']:
                file.replace(image_dir/normalize.normalize(file))

            if get_extencion(file) in folder_dict['video']:
                file.replace(video_dir/normalize.normalize(file))

            if get_extencion(file) in folder_dict['documents']:
                file.replace(documents_dir/normalize.normalize(file))

            if get_extencion(file) in folder_dict['audio']:
                file.replace(audio_dir/normalize.normalize(file))

            if get_extencion(file) in folder_dict['archive']:
                manage_archive(file, get_extencion(file))
            else:
                try:   
                    file.replace(other_dir/normalize.normalize(file))
                except FileNotFoundError:
                    continue
                except OSError:
                    continue
        except FileNotFoundError:
            continue
    
if __name__ == '__main__':
    main_folder = Path(sys.argv[1])
    main(main_folder)
    scan(main_folder)


    
    


