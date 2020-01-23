DROP TABLE if exists data;

CREATE TABLE data
(
    id              serial,
    field_1         integer,
    field_2         varchar(64)
);

COMMIT;

INSERT INTO data (field_1, field_2) VALUES (1, '1');

COMMIT;
