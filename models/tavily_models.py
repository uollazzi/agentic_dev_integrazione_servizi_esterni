from typing import Any, List, Optional

from pydantic import BaseModel


class Result(BaseModel):
    url: str
    title: str
    content: str
    score: float
    raw_content: Any
    id: str


class TavilySearchResponse(BaseModel):
    query: str
    follow_up_questions: Any
    answer: Any
    images: List
    results: List[Result]
    response_time: float
    request_id: str
