"""Toy retriever. Keyword overlap stands in for vector similarity."""

import re

from .documents import CORPUS, Document, can_read


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(query: str, user: str, *, enforce_acl: bool, k: int = 3) -> list[Document]:
    terms = _tokens(query)
    scored = []
    for doc in CORPUS:
        # The secure build filters BEFORE ranking: relevance is not authorisation.
        if enforce_acl and not can_read(user, doc):
            continue
        score = len(terms & _tokens(doc.text))
        if score:
            scored.append((score, doc.doc_id, doc))
    scored.sort(key=lambda s: (-s[0], s[1]))
    return [doc for _, _, doc in scored[:k]]
