display = js.document.getElementById('display')

def updateDisplay(char):
    display.value += char

def clearDisplay():
    display.value = ''

def delChar():
    display.value = display.value[0:-1]

def calculate():
    display.value = eval(display.value)
