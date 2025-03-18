from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pywhatkit_alt",
    version="0.1.0",
    author="Nathishwar",
    author_email="nathishwarc@gmail.com",
    description="A Python package for automation and utilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nathishwar-prog/Pywhatkit_Alternative-Module",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "yt_dlp",
        "pillow",
        "opencv-python",
        "pyautogui",
        "pyttsx3",
        "speechrecognition",
        "fpdf",
        "webdriver_manager",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
