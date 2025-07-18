"""
Script setup para la aplicacion de prueba Hello World
"""

from setuptools import setup, find_packages

setup(
    name="hello-world-app",
    version="1.0.0",
    description="Simple App Hello World con Python",
    author="Tu nombre",
    author_email="tu.correo@dominio.com",
    packages=find_packages(),
    py_modules=["app"],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "hello-world=app:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
