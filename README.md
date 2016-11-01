# drone-recon_contacts
Parses and imports JSON output from recon-ng module optiv/export_contacts into a LAIR project

## Installation
-----

This library is dependent on [pylair](https://github.com/lair-framework/pylair). After installing pylair, download the latest release [here](https://github.com/lair-framework/drone-recon_contacts/releases/latest).

```
$ sudo pip install drone-recon_contacts*.tar.gz
$ drone-recon_contacts -h
```

## Help
-----

```
drone-recon_contacts - Import JSON output from recon-ng module optiv/export_contacts into the Lair framework

positional arguments:
  id             Lair Project ID
  json_file      Recon JSON output file

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -k             Allow insecure SSL connections

```
