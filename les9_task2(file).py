import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        file_name = self.file_path[11:]
        with open(self.file_path, encoding='utf-8') as f:
            file_to_ya = f.read()
        header = {'Authorization': ' '} # токен убран, как написано в задании
        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=%2F{file_name}',
                                headers=header)
        href = response.json()['href']
        requests.put(href, data=file_to_ya)
        return 'Файлы успешно загружены'


if __name__ == '__main__':
    uploader = YaUploader('\\my_folder\\file.txt')
    result = uploader.upload()

    print(result)
