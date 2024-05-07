def color_format():
    '''
    Text Color             Background Color
    Black: \033[30m         Black: \033[40m
    Red: \033[31m           Red: \033[41m
    Green: \033[32m         Green: \033[42m
    Yellow: \033[33m        Yellow: \033[43m
    Blue: \033[34m          Blue: \033[44m
    Magenta: \033[35m       Magenta: \033[45m
    Cyan: \033[36m          Cyan: \033[36m
    White: \033[37m         White: \033[37m

    Reset: \033[0m (Resets all attributes)
    Bold: \033[1m
    '''

def getColorText(color_code, text):
    return f"\u001b[{color_code}m{text}\u001b[0m"


def getRedText(text):
    return getColorText('31;1', text)


def getCyanText(text):
    return getColorText('36;1', text)


def getPurpleText(text):
    return getColorText('35;1', text)


def getGreenText(text):
    return getColorText('32;1', text)

def getBoldText(text):
    return f"\033[1m{text}\033[0m"
