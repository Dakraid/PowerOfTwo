from cx_Freeze import setup, Executable

base = None    

executables = [Executable("PowerOfTwo.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':["sys","getopt","magic","os","re"],
        'optimize': 2
    },    
}

target = Executable(
    script="PowerOfTwo.py",
    icon="icon.ico"
)

setup(
    name = "PowerOfTwo",
    options = options,
    version = "1.0.0",
    description = 'PowerOfTwo checks all subdirectories within its directory for power of two textures',
    executables = [target]
)
