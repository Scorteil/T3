'Hello GitHub

set objShell= createobject("wscript.shell")

objShell.run "notepad.exe"

wscript.sleep	 1000

objShell.sendkeys "Hello world"