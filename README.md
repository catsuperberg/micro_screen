# micro_screen
This is a simple python package for creation of basic console user interfaces. For fully featured platforms, the **curses** library is available, but as I often need a quick and convenient way to interact with micropython projects, I decided to implement this package

Goals:
- multiple input fields
- multiple dynamically updatable output fields
- basic input with ability to clear field and switch between them
- stable and glitchless presentation on com port reconnects and terminal size changes

