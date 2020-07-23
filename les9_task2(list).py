import requests
import os


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def making_file_list(self):
        file_list = []
        for d, dirs, files in os.walk(self.file_path):
            for f in files:
                path = os.path.join(d, f)
                file_list.append(path)
        return file_list

    def upload(self):
        header = {'Authorization': ''}  #токен убран, как написано в задании
        file_list = self.making_file_list()
        for files in file_list:
            with open(files, encoding='utf-8') as f:
                _file = f.read()
            response = requests.get(
                f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=%2F{files[11:]}',
                headers=header)
            href = response.json()['href']
            requests.put(href, data=_file)
        return 'Файлы успешно загружены'


if __name__ == '__main__':
    uploader = YaUploader('\\my_folder\\')
    result = uploader.upload()

    print(result)
