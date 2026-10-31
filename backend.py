import zipfile

def archive_extractor(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(dest_dir)

if __name__ == '__main__':
    archive_extractor("E:/Other computers/My Laptop/Google Drive Uploadable/AI Engineering Practise/zip_extractor_app/compressed.zip",
                      "E:/Other computers/My Laptop/Google Drive Uploadable/AI Engineering Practise/zip_extractor_app")