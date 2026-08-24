from pathlib import Path

from ingestion.models import Document


def save_processed_document(
    document: Document,
    output_dir: str | Path = "data/processed",
) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    source_format = document.source_path.suffix.lstrip(".")
    target = output_path / f"{document.source_path.stem}_{source_format}.txt"

    target.write_text(document.content, encoding="utf-8")

    return target
