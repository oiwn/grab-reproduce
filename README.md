# grab-reproduce

Reproduce Grab scrapers errors.

# Annoying issues with emoji

```
encoding error : input conversion failed due to input error, bytes 0x21 0x00 0x00 0x00
lxml.etree.XMLSyntaxError: switching encoding: encoder error, line 1, column 1
```

### How to reproduce

Python

```bash
python --version
Python 3.5.2
```

System (OSX 10.11.6 El Capitan)

```bash
uname -a
Darwin Kernel Version 15.6.0
```

#### Run

```bash
pip install -r requirements.txt
python -m http.server
python github.py
```

## Note

On Python 2.7.13 everything running without any errors.
