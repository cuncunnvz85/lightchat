from setuptools import setup, find_packages
import pathlib

# Load README.md for long_description
here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="lightchat",
    version="0.1.2",
    description="Lightweight GPT2 training and deployment toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Required for Markdown rendering on PyPI
    author="RePromptsQuest",
    author_email="repromptsquest@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "transformers>=4.30.0",
        "datasets>=2.14.0",
        "torch>=1.13.0",
        "accelerate>=0.26.0",
        "fastapi>=0.100.0",
        "uvicorn[standard]>=0.22.0",
        "typer[all]>=0.9.0",
        "rich>=13.4.0",
    ],
    entry_points={
        "console_scripts": [
            "lightchat=lightchat.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
