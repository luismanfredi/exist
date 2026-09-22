CREATE TABLE IF NOT EXISTS predictions (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    model_version   TEXT NOT NULL,
    u               DOUBLE PRECISION NOT NULL,
    g               DOUBLE PRECISION NOT NULL,
    r               DOUBLE PRECISION NOT NULL,
    i               DOUBLE PRECISION NOT NULL,
    z               DOUBLE PRECISION NOT NULL,
    redshift        DOUBLE PRECISION NOT NULL,
    predicted_class TEXT NOT NULL CHECK (predicted_class IN ('GALAXY', 'STAR', 'QSO')),
    confidence      DOUBLE PRECISION NOT NULL CHECK (confidence BETWEEN 0 AND 1)
);

CREATE INDEX IF NOT EXISTS idx_predictions_created_at ON predictions (created_at);
