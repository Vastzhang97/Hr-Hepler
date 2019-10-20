from aip import AipOcr


class BaiDuApi:
    config = {
        'appId': '',
        'apiKey': '',
        'secretKey': ''
    }

    client = AipOcr(**config)

    @staticmethod
    def get_file_content(file):
        with open(file, 'rb') as fp:
            return fp.read()

    def request_api(self, image):
        # return self.client.basicAccurate(image)
        return self.client.basicGeneral(image)

    def read_image(self, file):
        image = self.get_file_content(file)
        result = self.request_api(image)
        text = '/n'.join([w['words'] for w in result['words_result']])
        return text


if __name__ == '__main__':
    image_path = 'C://Users/62526/Desktop/Test/CheckCode.png'
    api = BaiDuApi()
    print(api.read_image(image_path))
