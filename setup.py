import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="session",
    version="0.0.1",
    author="Taylor L Money",
    author_email="git@taylorlmoney.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/youngmoney/session",
    packages=setuptools.find_packages(),
    install_requires=["Flask", "requests"],
    entry_points={"console_scripts": ["session = session.cli:parse_and_run"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
