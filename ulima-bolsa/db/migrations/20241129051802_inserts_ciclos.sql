-- migrate:up
INSERT INTO ciclos (id, ciclo) VALUES (1, 1);
INSERT INTO ciclos (id, ciclo) VALUES (2, 2);
INSERT INTO ciclos (id, ciclo) VALUES (3, 3);
INSERT INTO ciclos (id, ciclo) VALUES (4, 4);
INSERT INTO ciclos (id, ciclo) VALUES (5, 5);
INSERT INTO ciclos (id, ciclo) VALUES (6, 6);
INSERT INTO ciclos (id, ciclo) VALUES (7, 7);
INSERT INTO ciclos (id, ciclo) VALUES (8, 8);
INSERT INTO ciclos (id, ciclo) VALUES (9, 9);
INSERT INTO ciclos (id, ciclo) VALUES (10, 10);

-- migrate:down
DELETE FROM ciclos;
