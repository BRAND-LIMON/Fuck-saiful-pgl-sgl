import requests

cookies = {
    'datr': 'w5YEZALhC_vo2hUBwRbjPg09',
    'sb': 'w5YEZM13DFdGJKGBgrHrw8Uv',
    'fr': '0BBvNm2IY2JztpMND..BkBJbD.BI.AAA.0.0.BkBJbY.AWW1geAIczM',
}

headers = {
    'authority': 'free.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'datr=w5YEZALhC_vo2hUBwRbjPg09; sb=w5YEZM13DFdGJKGBgrHrw8Uv; fr=0BBvNm2IY2JztpMND..BkBJbD.BI.AAA.0.0.BkBJbY.AWW1geAIczM',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13',
}

response = requests.get('https://free.facebook.com/', cookies=cookies, headers=headers)