from setuptools import setup

with open('README.md', encoding = 'utf-8') as f:
    setup(
        name = 'Mozaiku',
        version = '1.0.0',
        description = 'Use YouTube urls, ideos and folder of images to create photo mosaics.',
        long_description = f.read().replace(' - ザ・モザイク', '').replace('* [ ]', '*'),
        long_description_content_type = 'text/markdown',
        author = 'Cristiano Sansò',
        author_email = 'cristiano.sanso.04@gmail.com',
        url = 'https://github.com/Zslez/Mozaiku',
        packages = ['mozaiku'],
        setup_requires = ['wheel', 'pillow']
    )
