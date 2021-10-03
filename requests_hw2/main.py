from pprint import pprint
import requests


class YaUpLoader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': disk_file_path, 'overwrite': 'true'}
        headers = self.get_headers()
        response = requests.get(upload_url, params=params, headers=headers)
        pprint(response.json())
        return response.json()

    def upload_file(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    TOKEN = 'AQAAAABI2kSwAADLW8ANSlFIRkGGuDSpZiiyNx4'
    uploader = YaUpLoader(TOKEN)
    uploader.upload_file('project/_test.txt', '_test.txt')