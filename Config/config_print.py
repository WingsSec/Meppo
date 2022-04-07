#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import platform
import time


if 'Windows' in platform.system():
    import ctypes, sys
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    # 字体颜色定义 text colors
    FOREGROUND_BLUE = 0x09  # blue.
    FOREGROUND_GREEN = 0x0a  # green.
    FOREGROUND_DEEPGREEN = 0x02 # dark green.
    FOREGROUND_RED = 0x0c  # red.
    FOREGROUND_YELLOW = 0x0e  # yellow.
    FOREGROUND_WHITE = 0x0f  # white.
    FOREGROUND_PINK = 0x0d # pink.

    # get handle
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    def set_cmd_text_color(color, handle=std_out_handle):
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return Bool
    # reset white
    def resetColor():
        set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    # green
    def printGreen(mess):
        set_cmd_text_color(FOREGROUND_GREEN)
        sys.stdout.write(mess)
        sys.stdout.flush()
        resetColor()

    # red
    def printRed(mess):
        set_cmd_text_color(FOREGROUND_RED)
        sys.stdout.write(mess)
        sys.stdout.flush()
        resetColor()

    # yellow
    def printYellow(mess):
        set_cmd_text_color(FOREGROUND_YELLOW)
        sys.stdout.write(mess)
        sys.stdout.flush()
        resetColor()

    def printDeepGreen(mess):
        set_cmd_text_color(FOREGROUND_DEEPGREEN)
        sys.stdout.write(mess)
        sys.stdout.flush()
        resetColor()

    def printBlue(mess):
        set_cmd_text_color(FOREGROUND_BLUE)
        sys.stdout.write(mess)
        sys.stdout.flush()
        resetColor()

    def printBluen(mess):
        set_cmd_text_color(FOREGROUND_BLUE)
        sys.stdout.write(mess + '\n')
        sys.stdout.flush()
        resetColor()

    def printWhite(mess):
        set_cmd_text_color(FOREGROUND_WHITE)
        sys.stdout.write(mess + '\n')
        sys.stdout.flush()
        resetColor()

    def printPink(mess):
        set_cmd_text_color(FOREGROUND_PINK)
        sys.stdout.write(mess + '\n')
        sys.stdout.flush()
        resetColor()

    def get_INFO():
        printBlue('[{0}] '.format(get_time()))
        printDeepGreen('[INFO] ')

    def get_SUCCESS():
        printBlue('[{0}] '.format(get_time()))
        printGreen('[SUCCESS] ')

    def get_WARNING():
        printBlue('[{0}] '.format(get_time()))
        printYellow('[WARNING] ')

    def get_CRITICAL():
        printBlue('[{0}] '.format(get_time()))
        printRed('[CRITICAL] ')

else:
    DEEP_GREEN = "\033[30;1m{0}\033[0m"
    GREEN = "\033[32;1m{0}\033[0m"
    WHITE = "\033[29;1m{0}\033[0m"
    RED = "\033[31;1m{0}\033[0m"
    YELLOW = "\033[33;1m{0}\033[0m"
    BLUE = "\033[34;1m{0}\033[0m"
    PINK = "\033[35;1m{0}\033[0m"

    def get_INFO():
        print('{0} {1} '.format(BLUE.format('[' + get_time() + ']'), DEEP_GREEN.format('[INFO]')), end='')

    def get_SUCCESS():
        print('{0} {1} '.format(BLUE.format('[' + get_time() + ']'), GREEN.format('[SUCCESS]')), end='')

    def get_WARNING():
        print('{0} {1} '.format(BLUE.format('[' + get_time() + ']'), YELLOW.format('[WARNING]')), end='')

    def get_CRITICAL():
        print('{0} {1} '.format(BLUE.format('[' + get_time() + ']'), RED.format('[CRITICAL]')), end='')

    def printWhite(mess):
        print('{0}'.format(WHITE.format(mess)))

    def printBlue(mess):
        print('{0}'.format(BLUE.format(mess)))

    def printBluen(mess):
        print('{0}'.format(BLUE.format(mess)))

    def printPink(mess):
        print('{0}'.format(PINK.format(mess)))


def get_time():
    return time.strftime("%H:%M:%S", time.localtime())



def status_print(value='', status = -1):        # 输出函数
    if status == -1:                      # default      status = -1
        print(value)
    elif status == 0:                     # INFO         status = 0
        get_INFO()
        print(value)
    elif status == 1:                     # SUCCESS      status = 1
        get_SUCCESS()
        printWhite(value)
    elif status == 2:                     # WARNING      status = 2
        get_WARNING()
        print(value)
    elif status == 3:                     # CRITICAL     status = 3
        get_CRITICAL()
        print(value)
    elif status == 4:                     # 加粗          status = 4
        printWhite(value)
    elif status == 5:                     # 主色 猛男粉    status = 5
        printPink(value)
    elif status == 6:                     # 副色 蓝色      status = 6
        printBluen(value)



if __name__ == '__main__':
    for i in range(-1,7):
        status_print(str(i),i)