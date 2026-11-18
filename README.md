# DocFGP Office

[![PyPI version](https://img.shields.io/pypi/v/docfgp-office)](https://pypi.org/project/docfgp-office/)
[![PyPI downloads](https://img.shields.io/pepy/dt/docfgp-office)](https://pepy.tech/projects/docfgp-office)
[![CI](https://github.com/iamzices/docfgp-document-fingerprint-office/actions/workflows/ci.yml/badge.svg)](https://github.com/iamzices/docfgp-document-fingerprint-office/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/iamzices/docfgp-document-fingerprint-office)](LICENSE)

DocFGP Office provides the [office2pdf](https://github.com/developer0hye/office2pdf) converter that lets [DocFGP](https://github.com/iamzices/docfgp-document-fingerprint) convert DOCX and PPTX files.

## Requirements

- Python 3.11+
- Linux (x86_64, aarch64), macOS, or Windows (x64)

## Installation

```bash
pip install "docfgp[office]"
```

## Usage

```python
from docfgp_office import office_to_pdf

pdf = office_to_pdf("report.docx")  # PDF bytes; raises RuntimeError on failure
```
