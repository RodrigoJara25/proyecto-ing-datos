-- up
CREATE TABLE ciudades(
	id NUMBER(7) PRIMARY KEY,
	nombre VARCHAR2(30)
);

ALTER TABLE ciudades ADD (
  CONSTRAINT ciudades_pk PRIMARY KEY (ID));

CREATE SEQUENCE ciudades_seq START WITH 1;

CREATE OR REPLACE TRIGGER ciudades_pk 
BEFORE INSERT ON ciudades 
FOR EACH ROW

BEGIN
  SELECT ciudades_seq.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;
/

-- down

DROP SEQUENCE ciudades_seq;
DROP TABLE ciudades;