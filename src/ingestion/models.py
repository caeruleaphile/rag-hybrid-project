# un modèle Document qui standardise les documents provenant des différents
# loaders, avec leur contenu, leur chemin source et leurs métadonnées.
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class DocumentMetadata:
    source: str
    title: str | None = None
    page: int | None = None
    section: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass
class Document:
    content: str
    metadata: DocumentMetadata
    source_path: Path
