from pathlib import Path

from pypdf import PdfReader

from ingestion.models import Document, DocumentMetadata
from ingestion.normalization import normalize_text


class PDFLoader:
    """Load a PDF file and convert it to a Document."""

    def load(self, path: str | Path) -> Document:
        pdf_path = Path(path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected a PDF file: {pdf_path}")

        reader = PdfReader(pdf_path)

        pages: list[str] = []

        for page in reader.pages:
            text = page.extract_text() or ""
            pages.append(text.strip())

        content = normalize_text("\n\n".join(page for page in pages if page))

        metadata = DocumentMetadata(
            source=str(pdf_path),
            title=pdf_path.stem,
        )

        return Document(
            content=content,
            metadata=metadata,
            source_path=pdf_path,
        )

    def load_pages(self, path: str | Path) -> list[Document]:
        pdf_path = Path(path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected a PDF file: {pdf_path}")

        reader = PdfReader(pdf_path)

        documents: list[Document] = []

        for page_number, page in enumerate(reader.pages, start=1):
            content = normalize_text(page.extract_text() or "")

            if not content:
                continue

            metadata = DocumentMetadata(
                source=str(pdf_path),
                title=pdf_path.stem,
                page=page_number,
            )

            documents.append(
                Document(
                    content=content,
                    metadata=metadata,
                    source_path=pdf_path,
                )
            )

        return documents
