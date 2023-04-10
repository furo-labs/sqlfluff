"""The Oracle PL/SQL dialect.
https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/index.html

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
    MultiStringParser,
)
from sqlfluff.core.parser.segments.raw import KeywordSegment
from sqlfluff.dialects import dialect_oracle as oracle
from sqlfluff.dialects.dialect_plsql_keywords import (
    plsql_reserved_keywords,
    plsql_unreserved_keywords,
)

oracle_dialect = load_raw_dialect("oracle")
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

class StatementSegment(ansi.StatementSegment):
    """A generic segment, to any of its child subsegments."""

    match_grammar = ansi.StatementSegment.match_grammar
    parse_grammar = ansi.StatementSegment.parse_grammar.copy(
        insert=[
            Ref("AlterConnectionRotateKeys"),
            Ref("AlterIndexStatementSegment"),
            Ref("AlterRenameStatementSegment"),
            Ref("AlterSecretStatementSegment"),
            Ref("AlterSourceSinkSizeStatementSegment"),
            Ref("CloseStatementSegment"),
            Ref("CopyToStatementSegment"),
            Ref("CopyFromStatementSegment"),
            Ref("CreateClusterStatementSegment"),
            Ref("CreateClusterReplicaStatementSegment"),
            Ref("CreateConnectionStatementSegment"),
            Ref("CreateIndexStatementSegment"),
            Ref("CreateMaterializedViewStatementSegment"),
            Ref("CreateSecretStatementSegment"),
            Ref("CreateSinkKafkaStatementSegment"),
            Ref("CreateSourceKafkaStatementSegment"),
            Ref("CreateSourceLoadGeneratorStatementSegment"),
            Ref("CreateSourcePostgresStatementSegment"),
            Ref("CreateTypeStatementSegment"),
            Ref("CreateViewStatementSegment"),
            Ref("DropStatementSegment"),
            Ref("FetchStatementSegment"),
            Ref("MaterializeExplainStatementSegment"),
            Ref("ShowStatementSegment"),
            Ref("ShowCreateStatementSegment"),
            Ref("ShowIndexesStatementSegment"),
            Ref("ShowMaterializedViewsStatementSegment"),
            Ref("DeclareStatementSegment"),
        ],
        remove=[
            Ref("CreateIndexStatementSegment"),
            Ref("DropIndexStatementSegment"),
        ],
    )


