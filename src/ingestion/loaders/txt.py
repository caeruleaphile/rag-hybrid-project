from pathlib import Path

from ingestion.models import Document, DocumentMetadata
from ingestion.normalization import normalize_text


class TXTLoader:
    """Load a plain text file and convert it to a Document."""

    def load(self, path: str | Path) -> Document:
        txt_path = Path(path)

        if not txt_path.exists():
            raise FileNotFoundError(f"TXT file not found: {txt_path}")

        if txt_path.suffix.lower() != ".txt":
            raise ValueError(f"Expected a TXT file: {txt_path}")

        content = normalize_text(txt_path.read_text(encoding="utf-8"))

        metadata = DocumentMetadata(
            source=str(txt_path),
            title=txt_path.stem,
        )

        return Document(
            content=content,
            metadata=metadata,
            source_path=txt_path,
        )
