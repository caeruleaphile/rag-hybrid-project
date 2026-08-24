from pathlib import Path

from bs4 import BeautifulSoup

from ingestion.models import Document, DocumentMetadata
from ingestion.normalization import normalize_text


class HTMLLoader:
    """Load an HTML file and convert it to a Document."""

    def load(self, path: str | Path) -> Document:
        html_path = Path(path)

        if not html_path.exists():
            raise FileNotFoundError(f"HTML file not found: {html_path}")

        if html_path.suffix.lower() not in {".html", ".htm"}:
            raise ValueError(f"Expected an HTML file: {html_path}")

        raw_html = html_path.read_text(encoding="utf-8")

        soup = BeautifulSoup(raw_html, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        title_tag = soup.find("title")
        first_heading = soup.find(["h1", "h2", "h3", "h4", "h5", "h6"])

        title = title_tag.get_text(strip=True) if title_tag else html_path.stem

        section = first_heading.get_text(strip=True) if first_heading else None

        content = normalize_text(soup.get_text(separator="\n", strip=True))

        metadata = DocumentMetadata(
            source=str(html_path),
            title=title,
            section=section,
        )

        return Document(
            content=content,
            metadata=metadata,
            source_path=html_path,
        )
