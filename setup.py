import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken_disease_classification"
AUTHOR_USER_NAME = "vision818"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "jeegspatel131@gmail.com"

setuptools.setup(
    name=SRC_REPO
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple Convolutional Neural Network (CNN) classifier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src")
)