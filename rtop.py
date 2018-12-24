import psutil
import urwid
import datetime
import socket
import os
hostname = socket.gethostname()

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


palette = [
    ('header', 'light gray','default'),]
 
time = str(datetime.datetime.now().time())

def refresh(_loop, _data):
    _loop.draw_screen()
    header_items[2].set_text(str(datetime.datetime.now().time()))
    _loop.set_alarm_in(1, refresh)

    

header_items = [
    urwid.Text(('header', os.uname()[1]), align='left'),
    urwid.Text(('header', os.uname()[1]), align='center'),
    urwid.Text(('header', time), align='right'),
]

footer_items = [
    urwid.Text(('header', os.uname()[1]), align='left'),
    urwid.Text(('header', os.uname()[1]), align='center'),
    urwid.Text(('header', os.uname()[1]), align='right'),
]


urwid.Text(('header', os.uname()[1]), align='left')

header = urwid.Columns(header_items)
body = urwid.BarGraph(['1','2','2'])
bardata = [1,2,2,1,1]
lines = [5]
body.set_data(bardata, 4)





footer = urwid.Columns(footer_items)

view = urwid.Frame(body=body, header=header, footer=footer)


loop = urwid.MainLoop(view, palette, unhandled_input=exit_on_q)
loop.set_alarm_in(1, refresh)
loop.run()




    