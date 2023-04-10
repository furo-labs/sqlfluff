"""The Oracle PL/SQL dialect.
https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/index.html

This is based off the oracle dialect.
"""
from sqlfluff.core.dialects import load_raw_dialect
from sqlfluff.core.parser import (
    AnyNumberOf,
    AnySetOf,
    Anything,
    BaseSegment,
    Bracketed,
    CodeSegment,
    Delimited,
    Matchable,
    Nothing,
    OneOf,
    OptionallyBracketed,
    Ref,
    RegexLexer,
    RegexParser,
    SegmentGenerator,
    Sequence,
)

from sqlfluff.dialects import dialect_ansi as ansi
from sqlfluff.dialects import dialect_oracle as oracle
from sqlfluff.dialects.dialect_plsql_keywords import (
    plsql_reserved_keywords,
    plsql_unreserved_keywords,
)

oracle_dialect = load_raw_dialect("oracle")
ansi_dialect = load_raw_dialect("ansi")
plsql_dialect = oracle_dialect.copy_as("plsql")

# Set Keywords
plsql_dialect.sets("unreserved_keywords").clear()
plsql_dialect.sets("unreserved_keywords").update(
    [n.strip().upper() for n in plsql_unreserved_keywords.split("\n")]
)

plsql_dialect.sets("reserved_keywords").clear()
plsql_dialect.sets("reserved_keywords").update(
    [n.strip().upper() for n in plsql_reserved_keywords.split("\n")]
)

