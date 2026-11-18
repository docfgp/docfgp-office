"""Convert Office files to PDF and report conversion failures."""

import zipfile
from pathlib import Path

import pytest

from docfgp_office import office_to_pdf


def _docx(path: Path, text: str) -> None:
    content_types = (
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" '
        'ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/'
        'vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'
    )
    relationships = (
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Target="word/document.xml" Type="http://schemas.'
        'openxmlformats.org/officeDocument/2006/relationships/officeDocument"/></Relationships>'
    )
    document = (
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>"
    )

    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", relationships)
        archive.writestr("word/document.xml", document)


def test_docx_converts_to_pdf(tmp_path: Path) -> None:
    """Return PDF bytes for a DOCX file."""
    path = tmp_path / "one.docx"
    _docx(path, "alpha beta gamma")

    assert office_to_pdf(path).startswith(b"%PDF-")


def test_unreadable_files_raise_runtime_error(tmp_path: Path) -> None:
    """Report a file that office2pdf cannot read as RuntimeError."""
    path = tmp_path / "broken.docx"
    path.write_bytes(b"not an Office file")

    with pytest.raises(RuntimeError):
        office_to_pdf(str(path))
