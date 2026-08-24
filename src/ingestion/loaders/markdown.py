from pathlib import Path

from markdown_it import MarkdownIt

from ingestion.models import Document, DocumentMetadata
from ingestion.normalization import normalize_text


class MarkdownLoader:
    """Load a Markdown file and convert it to a Document."""

    def load(self, path: str | Path) -> Document:
        markdown_path = Path(path)

        if not markdown_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {markdown_path}")

        if markdown_path.suffix.lower() not in {".md", ".markdown"}:
            raise ValueError(f"Expected a Markdown file: {markdown_path}")

        raw_text = markdown_path.read_text(encoding="utf-8")

        parser = MarkdownIt()
        tokens = parser.parse(raw_text)

        text_parts: list[str] = []
        first_heading: str | None = None

        for token in tokens:
            if token.type == "inline" and token.content.strip():
                text = token.content.strip()
                text_parts.append(text)

                if first_heading is None and token.map is not None:
                    first_heading = text

        content = normalize_text("\n\n".join(text_parts))

        metadata = DocumentMetadata(
            source=str(markdown_path),
            title=first_heading or markdown_path.stem,
            section=first_heading,
        )

        return Document(
            content=content,
            metadata=metadata,
            source_path=markdown_path,
        )
