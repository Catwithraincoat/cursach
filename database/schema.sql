CREATE TABLE Message (
    id SERIAL PRIMARY KEY,
    from_user_id INTEGER,
    to_user_id INTEGER,
    message TEXT
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    character_id INTEGER,
    password_hash VARCHAR(100),
    login VARCHAR(32)
);

CREATE TABLE Character (
    id SERIAL PRIMARY KEY,
    race_id INTEGER,
    name VARCHAR(32),
    age INTEGER,
    state VARCHAR(10),
    relationship VARCHAR(10),
    date_of_death VARCHAR(50)
);

CREATE TABLE Doctor (
    id SERIAL PRIMARY KEY,
    character_id INTEGER,
    appearance TEXT,
    personality TEXT
);

CREATE TABLE Enemy (
    id SERIAL PRIMARY KEY,
    character_id INTEGER,
    reason VARCHAR(50)
);

CREATE TABLE Companion (
    id SERIAL PRIMARY KEY,
    character_id INTEGER,
    first_journey_id INTEGER
);

CREATE TABLE Journey (
    id SERIAL PRIMARY KEY,
    planet_id INTEGER,
    time_id INTEGER,
    doctor_id INTEGER,
    description TEXT
);

CREATE TABLE Race (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE Planet (
    id SERIAL PRIMARY KEY,
    race_id INTEGER,
    coordinates INTEGER
);

CREATE TABLE Time (
    id SERIAL PRIMARY KEY,
    timerfbuinverse VARCHAR(50),
    timerfbplanet VARCHAR(50)
);

CREATE TABLE Character_In_Journey (
  character_id INTEGER REFERENCES Character(ID) NOT NULL,
  journey_id INTEGER REFERENCES Journey(ID) NOT NULL,
  PRIMARY KEY (character_id, journey_id)
);


-- Foreign Key Constraints
ALTER TABLE Message ADD FOREIGN KEY (from_user_id) REFERENCES Users(id);
ALTER TABLE Message ADD FOREIGN KEY (to_user_id) REFERENCES Users(id);
ALTER TABLE Users ADD FOREIGN KEY (character_id) REFERENCES Character(id);
ALTER TABLE Character ADD FOREIGN KEY (race_id) REFERENCES Race(id);
ALTER TABLE Doctor ADD FOREIGN KEY (character_id) REFERENCES Character(id);
ALTER TABLE Enemy ADD FOREIGN KEY (character_id) REFERENCES Character(id);
ALTER TABLE Companion ADD FOREIGN KEY (character_id) REFERENCES Character(id);
ALTER TABLE Companion ADD FOREIGN KEY (first_journey_id) REFERENCES Journey(id);
ALTER TABLE Journey ADD FOREIGN KEY (planet_id) REFERENCES Planet(id);
ALTER TABLE Journey ADD FOREIGN KEY (time_id) REFERENCES Time(id);
ALTER TABLE Journey ADD FOREIGN KEY (doctor_id) REFERENCES Doctor(id);
ALTER TABLE Planet ADD FOREIGN KEY (race_id) REFERENCES Race(id);


CREATE OR REPLACE FUNCTION prevent_character_delete()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM Users WHERE character_id = OLD.id
        UNION
        SELECT 1 FROM Doctor WHERE character_id = OLD.id
        UNION
        SELECT 1 FROM Enemy WHERE character_id = OLD.id
        UNION
        SELECT 1 FROM Companion WHERE character_id = OLD.id
    ) THEN
        RAISE EXCEPTION 'Cannot delete character referenced by other tables';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER prevent_character_delete
BEFORE DELETE ON Character
FOR EACH ROW
EXECUTE PROCEDURE prevent_character_delete();

