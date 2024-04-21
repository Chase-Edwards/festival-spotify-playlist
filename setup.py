from setuptools import setup, find_packages

setup(
    name='festival-spotify-playlist',
    version='1.0.0',
    author='Chase Edwards',
    author_email='chase.b.edwards1@gmail.com',
    description='A package that creates a Spotify playlist for a music festival.',
    packages=find_packages(),
    install_requires=[
        'spotipy',
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Developers',
        'License :: Apache License 2.0',
        'Programming Language :: Python :: 3.12.3'
    ],
)