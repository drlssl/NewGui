from cx_Freeze import setup, Executable

# ADD FILES
files = ['01.png', 'themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="01.png"
)

# SETUP CX FREEZE
setup(
    name = "PyDracula",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
