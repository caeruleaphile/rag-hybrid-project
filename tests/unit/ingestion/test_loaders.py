from pathlib import Path

from ingestion.loaders.html import HTMLLoader
from ingestion.loaders.markdown import MarkdownLoader
from ingestion.loaders.pdf import PDFLoader
from ingestion.loaders.txt import TXTLoader


def test_txt_loader(tmp_path: Path) -> None:
    path = tmp_path / "sample.txt"
    path.write_text("Hello    RAG\n\n\nWorld", encoding="utf-8")

    document = TXTLoader().load(path)

    assert document.content == "Hello RAG\n\nWorld"
    assert document.metadata.source == str(path)
    assert document.metadata.title == "sample"


def test_markdown_loader(tmp_path: Path) -> None:
    path = tmp_path / "sample.md"
    path.write_text(
        "# RAG Hybrid\n\nThis is a RAG project.",
        encoding="utf-8",
    )

    document = MarkdownLoader().load(path)

    assert "RAG Hybrid" in document.content
    assert "This is a RAG project." in document.content
    assert document.metadata.source == str(path)


def test_html_loader(tmp_path: Path) -> None:
    path = tmp_path / "sample.html"
    path.write_text(
        """
        <html>
            <head>
                <title>RAG Project</title>
            </head>
            <body>
                <h1>Introduction</h1>
                <p>Hybrid search system.</p>
                <script>console.log("remove me")</script>
            </body>
        </html>
        """,
        encoding="utf-8",
    )

    document = HTMLLoader().load(path)

    assert document.metadata.title == "RAG Project"
    assert document.metadata.section == "Introduction"
    assert "Hybrid search system." in document.content
    assert "remove me" not in document.content


def test_pdf_loader_pages() -> None:
    path = Path("data/raw/sample.pdf")

    documents = PDFLoader().load_pages(path)

    assert len(documents) > 0
    assert documents[0].content
    assert documents[0].metadata.source == str(path)
    assert documents[0].metadata.title == "sample"
    assert documents[0].metadata.page == 1
