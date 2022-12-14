# Check pip

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://python.org)

[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-GREEN?style=for-the-badge)](LICENSE)

Python script to check if any malicious pip packages listed in a text file have been installed.

## Requirements

Python 2.7 or Python 3

## Instructions

Create a text file `malicious_packages.txt` in the repository folder filled with malicious Python package names, one name per line. Refer to `malicious_packages.txt.example` for the format.

Afterwards, run:

```bash
python check.py
```

If none of the packages listed in `malicious_packages.txt` have been installed, there will be no output.

Otherwise the list of installed malicious packages will be printed to stdout as follows:

```bash
3 malicious pip packages from `malicious_packages.txt` detected in `pip list --format=freeze` output
The packages are
['malicious_package1', 'malicious_package2', 'malicious_package3']
```
