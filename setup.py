#!/usr/bin/env python3
"""
Setup script for SuperDataAnalysis MCP
"""

from setuptools import setup, find_packages
import os
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read version from VERSION.md
import re

def get_version():
    """从 VERSION.md 文件中读取版本号"""
    version_file = this_directory / "VERSION.md"
    try:
        with open(version_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 查找版本号模式：## v1.0.2 (2025-01-24)
        match = re.search(r'^## v([0-9]+\.[0-9]+\.[0-9]+)', content, re.MULTILINE)
        if match:
            return match.group(1)
        
        # 如果没找到，返回默认版本
        return "1.0.2"
    except Exception as e:
        print(f"Error reading version: {e}")
        return "1.0.2"

version = get_version()

# Read requirements
requirements = []
requirements_file = this_directory / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#'):
                # Handle optional dependencies
                if 'pymysql' in line or 'psycopg2' in line or 'pymongo' in line:
                    continue  # These are optional
                requirements.append(line)

# Core requirements (always needed)
core_requirements = [
    'mcp>=1.0.0',
    'pandas>=2.0.0',
    'numpy>=1.24.0',
    'openpyxl>=3.1.0',
    'xlrd>=2.0.0',
    'scipy>=1.10.0',
    'python-dotenv>=1.0.0',
    'requests>=2.28.0',
    'sqlalchemy>=2.0.0',
]

# Optional dependencies
optional_requirements = {
    'mysql': ['pymysql>=1.1.0'],
    'postgresql': ['psycopg2-binary>=2.9.0'],
    'mongodb': ['pymongo>=4.5.0'],
    'xml': ['xmltodict>=0.13.0'],
    'all': [
        'pymysql>=1.1.0',
        'psycopg2-binary>=2.9.0', 
        'pymongo>=4.5.0',
        'xmltodict>=0.13.0'
    ]
}

setup(
    name="datamaster-mcp",
    version=version,
    author="Shan",
    author_email="szqshan@gmail.com",  # 学习AI1000天
    description="DataMaster MCP - AI-powered data analysis tool with MCP protocol support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/szqshan/DataMaster",
    project_urls={
        "Bug Reports": "https://github.com/szqshan/DataMaster/issues",
        "Source": "https://github.com/szqshan/DataMaster",
        "Documentation": "https://github.com/szqshan/DataMaster/blob/master/README.md",
        "Homepage": "https://www.xueai.org",
        "Learning Platform": "https://www.xueai.me",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=core_requirements,
    extras_require=optional_requirements,
    entry_points={
        "console_scripts": [
            "datamaster-mcp=datamaster_mcp.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "datamaster_mcp": [
            "config/*.json",
            "config/*.py",
            "*.md",
            "requirements.txt",
        ],
    },
    keywords=[
        "mcp", "data-analysis", "ai", "pandas", "database", 
        "excel", "csv", "json", "mysql", "postgresql", "mongodb",
        "data-processing", "analytics", "business-intelligence"
    ],
    zip_safe=False,
)