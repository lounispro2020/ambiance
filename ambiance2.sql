BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "playlist" (
	"id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "led_color" (
	"id"	INTEGER,
	"color"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "music" (
	"id"	INTEGER,
	"name"	TEXT,
	"id_playlist"	INTEGER,
	"path"	TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_playlist") REFERENCES "playlist"("id")
);
CREATE TABLE IF NOT EXISTS "algorithme" (
	"id_playlist"	INTEGER,
	"id_led"	INTEGER,
	"begin_time"	TIME,
	"end_time"	TIME,
	"begin_month"	DATE,
	"end_month"	DATE,
	"min_temp"	INTEGER,
	"max_temp"	INTEGER,
	FOREIGN KEY("id_playlist") REFERENCES "playlist"("id"),
	FOREIGN KEY("id_led") REFERENCES "led_color"("id")
);
CREATE TABLE IF NOT EXISTS "temperature" (
	"temperature"	INTEGER,
	"date_time"	DATE
);
INSERT INTO "playlist" VALUES (1,'hiver');
INSERT INTO "playlist" VALUES (2,'été');
INSERT INTO "playlist" VALUES (3,'test');
INSERT INTO "led_color" VALUES (1,'0,255,0');
INSERT INTO "led_color" VALUES (2,'255,0,0');
INSERT INTO "led_color" VALUES (3,'0,0,255');
INSERT INTO "music" VALUES (1,'musique 1',1,'C:\musique 1');
INSERT INTO "music" VALUES (2,'musique 2',1,'C:\musique 2');
INSERT INTO "music" VALUES (3,'musique 3',1,'C:\musique 3');
INSERT INTO "music" VALUES (4,'musique 4',2,'C:\musique 4');
INSERT INTO "music" VALUES (5,'musique 5',2,'C:\musique 5');
INSERT INTO "music" VALUES (6,'musique 6',1,'C:\musique 6');
INSERT INTO "music" VALUES (7,'musique 7',3,'C:\musique 7');
INSERT INTO "music" VALUES (8,'musique 8',3,'C:\musique 8');
INSERT INTO "music" VALUES (9,'musique 9',3,'C:\musique 9');
INSERT INTO "algorithme" VALUES (1,1,10,18,11,3,10,20);
INSERT INTO "algorithme" VALUES (2,2,8,18,4,7,20,30);
INSERT INTO "algorithme" VALUES (3,3,10,18,4,7,0,10);
COMMIT;
