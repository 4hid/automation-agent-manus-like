"""Setup script for Automation Agent."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="automation-agent-manus-like",
    version="1.0.0",
    author="4hid",
    author_email="automation@example.com",
    description="AI Automation Agent with Manus.im-like capabilities for full task automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4hid/automation-agent-manus-like",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Office/Business :: Scheduling",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=3.0.0",
            "coverage>=7.0.0",
        ],
        "web": [
            "scrapy>=2.7.0",
            "playwright>=1.30.0",
            "selenium>=4.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "automation-agent=automation_agent.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "automation_agent": [
            "prompts/*.j2",
            "prompts/*.md",
        ],
    },
)