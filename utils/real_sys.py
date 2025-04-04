import sys

def get_os():
    if sys.platform.startswith('win'):
        return 'Windows'
    elif sys.platform.startswith('darwin'):
        return 'MacOS'
    elif sys.platform.startswith('linux'):
        return 'Linux'
    else:
        return 'Unknown'

def get_os_version():
    if get_os() == 'Windows':
        return sys.getwindowsversion()
    elif get_os() == 'MacOS':
        return sys.platform
    elif get_os() == 'Linux':
        return sys.platform
    else:
        return 'Unknown'

def get_os_style():
    if get_os() == 'Windows':
        return 'win'
    elif get_os() == 'MacOS':
        return 'aqua'
    elif get_os() == 'Linux':
        return 'clam'
    else:
        return 'unknown'

# # пример использования
# if __name__ == '__main__':
#     print('Операционная система:', get_os())
#     print('Версия операционной системы:', get_os_version())
#     print('Стиль операционной системы:', get_os_style())