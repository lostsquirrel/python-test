import requests


def download(url):
    params = {
        'method':' add_task',
        'app_id': 250528,
        'source_url': url,
        'save_path': '/'
    }

    cookies = dict(PANWEB='1',
                   bdshare_firstime='1462874105274',
                   Hm_lvt_eb77799942fcf84785b5626e398e49ab='1470296852',
                   PSTM='1471239607',
                   BIDUPSID='8A8446A26C4303B7E9AFDBAEEA522866',
                   BAIDUID='A0085F1FF82C5AA4298E56FFA89BD4F9:FG=1',
                   BDUSS='WEycmx5amt3WDlVbG5QcTlNMW91Rk9WUS1KWUVoc3BCUnI5Tk9jV0ZFa3BiQWhZQVFBQUFBJCQAAAAAAAAAAAEAAAAmpqQFbHMyNTQwMzEyNTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACnf4Fcp3-BXW',
                   STOKEN='68fc6423444d3822a7463db6c254105e018a99cc7abf4b44b9eccb68f763a774',
                   SCRC='43180c2408db0b3a752ea18597a26f7a',
                   Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0='1474354959;1476147991',
                   Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0='1476147991',
                   cflag='15%3A3',
                   PANPSC='10698350779774694994%3AmTP0WM%2Fa3Ky64eIw0ngbvNwxnZzNwr1wlNy1uIsy5V%2F4qyI5%2B5mMvoM6La9EbgvRi49OW4js1N9mET5jWHOCivISZKOyrzcAWgOwUqNMWAS%2FYCuu9v6mREtwbo5kSFAXA%2BxG4rXTWE1lVnBz%2FZp9zD4wgdQ%2F1cWMmgeUfIab6RA1jwuzSnCYVYlROd9IBwsr'
    )

    headers = {
        'Host': 'pan.baidu.com',
        'Origin': 'http://pan.baidu.com',
        'Referer': 'http://pan.baidu.com/disk/home',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    burl = 'http://pan.baidu.com/rest/2.0/services/cloud_dl'
    print requests.post(url, data=params, cookies=cookies, headers=headers).content


def read_url():
    hd = open('free_book_url.txt')
    for l in hd:
        download(l)

if __name__ == '__main__':
    read_url()