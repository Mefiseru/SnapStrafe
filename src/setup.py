from setuptools import setup, Extension
import platform

# Check if the current operating system is Windows
is_windows = platform.system() == 'Windows'

# Define the module with the correct libraries based on the OS
module = Extension(
    'strafe_tapper',
    sources=['strafe_tapper.c'],
    libraries=['user32'] if is_windows else ['X11', 'Xtst']
)

setup(
    name='strafe_tapper',
    version='1.0',
    description='Ultra-fast key detection and tapping module.',
    ext_modules=[module],
)
