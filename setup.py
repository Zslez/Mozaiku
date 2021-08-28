from setuptools import setup

with open('README.md', encoding = 'utf-8') as f:
    setup(
        name = 'Mozaiku',
        version = '1.0.3',
        description = 'Use YouTube urls, videos and folder of images to create photo mosaics with 1 line of code.',
        long_description = f.read().replace(
            ' - ザ・モザイク', '\n\nif you like the project, '\
            'consider starring the [repository](https://github.com/Zslez/Mozaiku) on GitHub'
        ).replace('* [ ]', '*'),
        long_description_content_type = 'text/markdown',
        author = 'Cristiano Sansò',
        author_email = 'cristiano.sanso.04@gmail.com',
        url = 'https://github.com/Zslez/Mozaiku',
        packages = ['mozaiku'],
        setup_requires = ['wheel', 'pillow'],
        classifiers = [
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Development Status :: 5 - Production/Stable',
            'Natural Language :: English'
        ],
    )
