from setuptools import setup, find_packages

setup(
    name='image_downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A simple package to download images from a URL.',
    author='Estifanos Abebaw',
    author_email='tekl.estifano.17@gmail.com',
    url='https://github.com/esti_tech/image_downloader',  # replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)