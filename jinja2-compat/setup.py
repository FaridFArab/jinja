import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="Jinja2",
    version="2.11.0rc1",
    url="https://palletsprojects.com/p/jinja/",
    project_urls={
        "Documentation": "https://jinja.palletsprojects.com/",
        "Code": "https://github.com/pallets/jinja",
        "Issue tracker": "https://github.com/pallets/jinja/issues",
    },
    license="BSD-3-Clause",
    maintainer="Pallets",
    maintainer_email="contact@palletsprojects.com",
    description=(
        "A very fast and expressive template engine. Compatibility"
        " package for Jinja2 to Jinja rename."
    ),
    long_description=readme,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["Jinja<4.0"],
    extras_require={"i18n": ["Babel>=0.8"]},
    entry_points={"babel.extractors": ["jinja2 = jinja2.ext:babel_extract[i18n]"]},
)