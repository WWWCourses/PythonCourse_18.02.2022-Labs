
use test;

-- create index on existing table:
ALTER TABLE users ADD INDEX (sname(10));

desc users;

/* ------------------------------- Primary key ------------------------------ */
DROP TABLE artist;

CREATE TABLE artist (
  id MEDIUMINT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  fname VARCHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL DEFAULT '',
  INDEX (lname),
  UNIQUE (fname, lname)
);

desc artist;

INSERT INTO artist (fname) VALUES ('Milena');
INSERT INTO artist (fname,lname) VALUES ('Milena','Atanasova');

INSERT INTO artist (fname,lname) VALUES ('Robert','Smith');
INSERT INTO artist (fname,lname) VALUES ('Fname','Lname');

SELECT * FROM artist;

DELETE FROM artist WHERE id=1;



/* ------------------------------- Foreign Key ------------------------------ */

/* -------------------------- ONE TO MANY RELATION -------------------------- */
CREATE TABLE artist (
  id MEDIUMINT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  fname VARCHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL DEFAULT '',
  INDEX (lname),
  UNIQUE (fname, lname)
);

CREATE TABLE albums(
	id INT NOT NULL AUTO_INCREMENT,
	artist_id MEDIUMINT(4) NOT NULL,
	title VARCHAR(50) NOT NULL,
	year DATE,
	PRIMARY KEY(id),
	FOREIGN KEY (artist_id) REFERENCES artist(id)
);


INSERT INTO albums (artist_id, title, year) VALUES
	(5, 'Album1','2000-01-20'),
	(5, 'Album2','2002-01-10'),
	(5, 'Album3','2004-12-30');


/* -------------------------- MANY TO MANY RELATION ------------------------- */

CREATE TABLE artist (
  id MEDIUMINT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  fname VARCHAR(20) DEFAULT NULL,
  lname VARCHAR(20) NOT NULL DEFAULT '',
  INDEX (lname),
  UNIQUE (fname, lname)
);

CREATE TABLE albums(
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(50) NOT NULL,
	year DATE,
	PRIMARY KEY(id)
);

CREATE TABLE artists_albums(
	album_id INT NOT NULL,
	artist_id MEDIUMINT(4) NOT NULL,
	FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE,
	FOREIGN KEY (artist_id) REFERENCES artist(id)
)



