import zipfile, os, tarfile

def unzip_file(file_path,output_path):
    if file_path.find('.zip') != -1:
        zip_ref = zipfile.ZipFile(file_path, 'r')
        zip_ref.extractall(output_path)
        zip_ref.close()
    else:
        tar = tarfile.open(file_path)
        tar.extractall(output_path)
        tar.close()
    return None
class Unzip_class():
    def __init__(self, path, file):
        out_path = os.path.join(path,'Unzipped',file.split('.zip')[0])
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        unzip_file(os.path.join(path,file),out_path)
        down_folder(out_path)


def down_folder(path):
    files = []
    dirs = []
    for root, dirs, files in os.walk(path):
        break
    for file in files:
        if file.find('.zip') != -1:
            print(os.path.join(path,file))
            unzip_file(os.path.join(path,file),path)
    for dir in dirs:
        down_folder(os.path.join(path,dir))
if __name__ == '__main__':
    xxx = 1
    # file_path = r"C:\Users\bmanderson\Downloads"
    # Unzip_class(path=file_path,file='coi_disclosure.zip')