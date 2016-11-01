# drone-inspy
Parses and imports InSpy JSON output into a lair project

## Installation
-----

This library is dependent on [pylair](https://github.com/lair-framework/pylair). After installing pylair, download the latest release [here](https://github.com/lair-framework/drone-inspy/releases/latest).

```
$ sudo pip install drone-recon_contacts*.tar.gz
$ drone-recon_contacts -h
```

## Help
-----

```
drone-recon_contacts - Import recon_export JSON output into the Lair framework

positional arguments:
  id             Lair Project ID
  json_file      Recon JSON output file

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -k             Allow insecure SSL connections

```