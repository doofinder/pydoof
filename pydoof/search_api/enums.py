from enum import Enum, unique


@unique
class QueryNames(Enum):
    MATCH_AND = "match_and"
    MATCH_OR = "match_or"
    FUZZY = "fuzzy"


@unique
class SearchFilterExecution(Enum):
    AND = "and"
    OR = "or"
