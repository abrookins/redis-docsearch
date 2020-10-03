from dataclasses import InitVar, dataclass, field
from typing import Dict, List, Set, Tuple, Callable

from docsearch import keys
from redisearch.client import Field

TYPE_PAGE = "page"
TYPE_SECTION = "section"


@dataclass(frozen=True)
class SearchDocument:
    doc_id: str
    title: str
    section_title: str
    hierarchy: List[str]
    url: str
    body: str
    type: str
    position: int = 0


@dataclass(frozen=True)
class SynonymGroup:
    group_id: str
    synonyms: Set[str]


ScoreFn = Callable[[SearchDocument, float], float]
ValidatorFn = Callable[[SearchDocument], None]


@dataclass(frozen=True)
class SiteConfiguration:
    url: str
    synonym_groups: List[SynonymGroup]
    schema: Tuple[Field]
    scorers: Tuple[ScoreFn]
    validators: Tuple[ValidatorFn]
    landing_pages: Dict[str, SearchDocument]

    @property
    def all_synonyms(self) -> Set[str]:
        synonyms = set()
        for syn_group in self.synonym_groups:
            synonyms |= syn_group.synonyms
        return synonyms

    @property
    def index_name(self) -> str:
        return keys.index_name(self.url)
