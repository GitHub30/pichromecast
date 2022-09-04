from setuptools import setup

setup(
    name='pichromecast',
    version='0.1',
    description='Library for MicroPython to communicate with the Google Chromecast.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GitHub30/pichromecast',
    project_urls={ 'Bug Tracker': 'https://github.com/GitHub30/pichromecast/issues' },
    author='Tomofumi Inoue',
    author_email='funaox@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    py_modules=['pichromecast']
)

# Publish commands
# https://packaging.python.org/tutorials/packaging-projects/
#pip install --upgrade pip build twine
#python -m build
#python -m twine upload dist/*
