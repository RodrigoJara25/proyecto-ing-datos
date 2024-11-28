-- up
CREATE TABLE albums(
  id NUMBER(7) PRIMARY KEY,
  title VARCHAR2(160) NOT NULL,
  artist_id NUMBER(7),
  FOREIGN KEY (artist_id) REFERENCES artists
);

ALTER TABLE albums ADD (
  CONSTRAINT albums_pk PRIMARY KEY (ID));

CREATE SEQUENCE albums_seq START WITH 1;

CREATE OR REPLACE TRIGGER albums_pk 
BEFORE INSERT ON albums 
FOR EACH ROW

BEGIN
  SELECT albums_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/

-- down

DROP SEQUENCE albums_seq;
DROP TABLE albums;