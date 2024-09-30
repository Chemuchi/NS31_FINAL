import requests, os

token = os.environ.get('NS31_OPENDICT_TOKEN')

def word(word):
    definitions = []
    url = 'https://stdict.korean.go.kr/api/search.do'
    params ={
        "key" : token,
        "q" : word,
        "num": 10,
        "req_type" : 'json',

    }
    response = requests.get(url, params=params)
    data = response.json()
    items = data['channel']['item']
    for item in items:
        definition = item['sense']['definition']
        definitions.append(definition)

    return definitions

def dic():
    print("\n데이터는 국립 국어원의 우리말샘 API에서 가져옵니다..")
    try:
        search = input("\n검색할 단어를 입력해주세요: ")
        data = word(search)
        for i, definition in enumerate(data):
            print(f"【{i + 1}】 {definition}")
    except Exception:
        print("\n검색할 수 없는 단어거나 서버에 오류가 있습니다.")