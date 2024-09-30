import deepl, os
key = os.environ.get("NS31_DEEPL_TOKEN")
trans = deepl.Translator(str(key))

def toeng(message):
    print(trans.translate_text(message, target_lang="EN-US"))

def tokr(message):
    print(trans.translate_text(message, target_lang="KO"))


def translate():
    print("\n번역 서비스는 DeepL의 API를 사용하였습니다.")
    try:
        opt = int(input("\n원하는 옵션을 선택해주세요.\n1. 영어로 번역\n2. 한글로 번역\n 옵션: "))
        if (opt == 1):
            message = input("\n번역할 내용을 입력해주세요: ")
            toeng(message)
        else:
            message = input("\n번역할 내용을 입력해주세요: ")
            tokr(message)
    except Exception:
        print("\n내용이 잘못되었거나 서버에 오류가 있습니다.")

