import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text')


def main():
    text = parser.parse_args().text

    text = text.replace('http://', 'httpcolomslashslash')
    text = text.replace('https://', 'httpscolomslashslash')
    text = text.replace('=', 'equal_sign')
    text = text.replace('+', 'plus_sign')
    text = text.replace('?', 'question_mark')
    text = text.replace('&', 'ampersand')

    text = encode(text)
    text = text.replace('httpcolomslashslash', 'http://')
    text = text.replace('httpscolomslashslash', 'https://')
    text = text.replace('equal_sign', '=')
    text = text.replace('plus_sign', '+')
    text = text.replace('question_mark', '?')
    text = text.replace('ampersand', '&')

    print(text)


def encode(text):
    if is_python_2():
        import urllib
        return urllib.quote(text)

    if is_python_3():
        import urllib.parse
        return urllib.parse.quote(text)

    raise RuntimeError("Python 2 or 3 are needed")


def is_python_2():
    return sys.version_info.major == 2


def is_python_3():
    return sys.version_info.major == 3


if __name__ == '__main__':
    main()
