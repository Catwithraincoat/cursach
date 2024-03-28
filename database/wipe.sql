-- Disable foreign key constraints
ALTER TABLE Message DROP CONSTRAINT IF EXISTS message_from_user_id_fkey;
ALTER TABLE Message DROP CONSTRAINT IF EXISTS message_to_user_id_fkey;
ALTER TABLE Users DROP CONSTRAINT IF EXISTS user_character_id_fkey;
ALTER TABLE Character DROP CONSTRAINT IF EXISTS character_race_id_fkey;
ALTER TABLE Doctor DROP CONSTRAINT IF EXISTS doctor_character_id_fkey;
ALTER TABLE Enemy DROP CONSTRAINT IF EXISTS enemy_character_id_fkey;
ALTER TABLE Companion DROP CONSTRAINT IF EXISTS companion_character_id_fkey;
ALTER TABLE Companion DROP CONSTRAINT IF EXISTS companion_first_journey_id_fkey;
ALTER TABLE Journey DROP CONSTRAINT IF EXISTS journey_planet_id_fkey;
ALTER TABLE Journey DROP CONSTRAINT IF EXISTS journey_time_id_fkey;
ALTER TABLE Journey DROP CONSTRAINT IF EXISTS journey_doctor_id_fkey;
ALTER TABLE Planet DROP CONSTRAINT IF EXISTS planet_race_id_fkey;
ALTER TABLE Character_In_Journey DROP CONSTRAINT IF EXISTS character_in_journey_character_id_fkey;
ALTER TABLE Character_In_Journey DROP CONSTRAINT IF EXISTS character_in_journey_journey_id_fkey;

-- Truncate tables
TRUNCATE TABLE Message, Users, Character, Doctor, Enemy, Companion, Journey, Race, Planet, Time, Character_In_Journey RESTART IDENTITY;

-- Reset sequences
SELECT setval('message_id_seq', 1, false);
SELECT setval('users_id_seq', 1, false);
SELECT setval('character_id_seq', 1, false);
SELECT setval('doctor_id_seq', 1, false);
SELECT setval('enemy_id_seq', 1, false);
SELECT setval('companion_id_seq', 1, false);
SELECT setval('journey_id_seq', 1, false);
SELECT setval('race_id_seq', 1, false);
SELECT setval('planet_id_seq', 1, false);
SELECT setval('time_id_seq', 1, false);

-- -- Enable foreign key constraints
-- ALTER TABLE Message ADD CONSTRAINT message_from_user_id_fkey FOREIGN KEY (from_user_id) REFERENCES Users(id);
-- ALTER TABLE Message ADD CONSTRAINT message_to_user_id_fkey FOREIGN KEY (to_user_id) REFERENCES Users(id);
-- ALTER TABLE Users ADD CONSTRAINT user_character_id_fkey FOREIGN KEY (character_id) REFERENCES Character(id);
-- ALTER TABLE Character ADD CONSTRAINT character_race_id_fkey FOREIGN KEY (race_id) REFERENCES Race(id);
-- ALTER TABLE Doctor ADD CONSTRAINT doctor_character_id_fkey FOREIGN KEY (character_id) REFERENCES Character(id);
-- ALTER TABLE Enemy ADD CONSTRAINT enemy_character_id_fkey FOREIGN KEY (character_id) REFERENCES Character(id);
-- ALTER TABLE Companion ADD CONSTRAINT companion_character_id_fkey FOREIGN KEY (character_id) REFERENCES Character(id);
-- ALTER TABLE Companion ADD CONSTRAINT companion_first_journey_id_fkey FOREIGN KEY (first_journey_id) REFERENCES Journey(id);
-- ALTER TABLE Journey ADD CONSTRAINT journey_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES Planet(id);
-- ALTER TABLE Journey ADD CONSTRAINT journey_time_id_fkey FOREIGN KEY (time_id) REFERENCES Time(id);
-- ALTER TABLE Journey ADD CONSTRAINT journey_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES Doctor(id);
-- ALTER TABLE Planet ADD CONSTRAINT planet_race_id_fkey FOREIGN KEY (race_id) REFERENCES Race(id);
-- ALTER TABLE Character_In_Journey ADD CONSTRAINT character_in_journey_character_id_fkey FOREIGN KEY (character_id) REFERENCES Character(id);
-- ALTER TABLE Character_In_Journey ADD CONSTRAINT character_in_journey_journey_id_fkey FOREIGN KEY (journey_id) REFERENCES Journey(id);
