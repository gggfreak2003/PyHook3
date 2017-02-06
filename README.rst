PyHook3
=======================
A fork of pyHook from Peter Parente (https://sourceforge.net/projects/pyhook/).

Works with Python 3.x


Requirements
---------------

- Windows 2000 or later
- Python 3.2 or later
- PyWin32 library (https://sourceforge.net/projects/pywin32/)

If you want to build PyHook3 from source code, then you additionally need
- MinGW (with gcc-core, gcc-g++, binutils, runtime, utils, w32api) (http://www.mingw.org/)
- SWIG (http://www.swig.org/)


Known bugs
---------------

- PyInstaller can't build single-file executables using pyHook. This may be
  fixed in 1.5.1, but hasn't been tested.
- PyHook3 is reported to break dead keys on non-US-english keyboards.
- WM_CHAR messages are not intercepted by pyHook, even if SubscribeKeyChar() or
  SubscribeKeyAll() are used to set the callback function.


Limitations
---------------

- PyHook3 will not work on Win9x (no messages show up) as it uses hooks which
  are not present in Windows systems prior to NT 4.0 SP3.


Website
---------------

Visit https://github.com/gggfreak2003/PyHook3 for binaries, documentation, and tutorials.

Bug reports and feature requests should be reported via the github page at
https://github.com/gggfreak2003/PyHook3
