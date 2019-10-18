from aip import AipOcr

config = {
    'appId': '17557567',
    'apiKey': 'oGovSju8BFdqW5zd7yyCFcQN',
    'secretKey': 'RdXAV2rB283RqHIXPpjLezCnb220DanM'
}

client = AipOcr(**config)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


image = get_file_content('C://Users/developer/Desktop/CheckCode.png')
result = client.basicAccurate(image)

# text = '/n'.join([w['words'] for w in result['words_result']])
print(result)
