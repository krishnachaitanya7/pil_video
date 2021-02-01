from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


# Tip: Generate requirements using pigar: pigar -p requirements.txt -P pil_video/
setup(
    name="pil_video",
    version="0.0.1",
    description="Play a PIL Image list as a video",
    author=" Kodur Krishna Chaitanya",
    author_email="kodur.chaitanya@colorado.edu",
    url="https://github.com/krishnachaitanya7/pil_video",
    install_requires=parse_requirements("requirements.txt"),
    packages=find_packages(exclude=("tests", "docs")),
)

# Some important notes to keep in mind,

