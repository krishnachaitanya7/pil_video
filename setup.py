from distutils.core import setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


# Tip: Generate requirements using pigar: pigar -p requirements.txt -P pil_video/
reqs = [str(ir.req) for ir in parse_requirements("requirements.txt")]
setup(
    name="pil_video",
    version="1.0",
    description="Play a PIL Image list as a video",
    author=" Kodur Krishna Chaitanya",
    author_email="kodur.chaitanya@colorado.edu",
    url="https://www.python.org/sigs/distutils-sig/",
    packages=["pil_video"],
    install_requires=reqs,
)

