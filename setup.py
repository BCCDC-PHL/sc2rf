from setuptools import setup

setup(
    name="sc2rf",
    description="SARS-Cov-2 Recombinant Finder for fasta sequences",
    license="MIT",
    author="Lena Schimmel",
    url="https://github.com/lenaschimmel/sc2rf",
    version="0.0.2",
    install_requires=[
        "termcolor>=1.1.0",
        "requests>=2.27.1",
        "tqdm>=4.63.1",
    ],
    python_requires=">=3.6",
    package_data = {'sc2rf': ['data/mapping.csv', 'data/reference.fasta', 'data/virus_properties.json']},
    include_package_data = True,
    entry_points={
        "console_scripts": [
            "sc2rf = sc2rf.sc2rf:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="cli"
)
