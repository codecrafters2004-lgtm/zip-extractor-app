import zipfile

def archive_extractor(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(dest_dir)

if __name__ == '__main__':
    archive_extractor("",
                      "")