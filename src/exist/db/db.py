import logging
import os
from pathlib import Path
from typing import LiteralString, cast

import psycopg
from psycopg.rows import dict_row

logger = logging.getLogger(__name__)


def _dsn() -> str:
    return os.environ["DATABASE_URL"]


def init_db() -> None:
    schema = Path(__file__).with_name("schema.sql").read_text()
    with psycopg.connect(_dsn()) as conn:
        conn.execute(cast(LiteralString, schema))


def log_prediction(
    features: dict[str, float],
    predicted_class: str,
    confidende: float,
    model_version: str,
) -> None:
    with psycopg.connect(_dsn()) as conn:
        conn.execute(
            "INSERT INTO predictions "
            "(model_version, u, g, i, r, z, redshift, predicted_class, confidence) "
            "VALUES (%(model_version)s, %(u)s, %(g)s, %(r)s, %(i)s, %(z)s, %(redshift)s, %(predicted_class)s, %(confidence)s) ",
            {
                **features,
                "model_version": model_version,
                "predicted_class": predicted_class,
                "confidence": confidende,
            },
        )


def stats_by_class() -> list[dict]:
    with psycopg.connect(_dsn(), row_factory=dict_row) as conn:  # type: ignore
        return conn.execute(  # type: ignore
            "SELECT predicted_class, COUNT(*) AS total, "
            "ROUND(AVG(confidence)::numeric, 3) AS avg_confidence "
            "FROM predictions GROUP BY predicted_class ORDER BY total DESC"
        ).fetchall()
