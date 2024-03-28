-- Populate Race table
INSERT INTO Race (name, description, state)
VALUES
    ('Time Lord', 'A race of time-traveling aliens from the planet Gallifrey', 'Active'),
    ('Human', 'The dominant species on Earth', 'Active'),
    ('Dalek', 'A race of mutant cyborg aliens bent on universal domination', 'Active'),
    ('Cyberman', 'A race of cybernetic beings that seek to convert all organic life', 'Active'),
    ('Sontaran', 'A race of clone warriors from the planet Sontar', 'Active');

-- Populate Character table
INSERT INTO Character (race_id, name, age, state, date_of_death)
VALUES
    (1, 'The Doctor', 900, 'Active', NULL),
    (2, 'Rose Tyler', 25, 'Active', NULL),
    (2, 'Martha Jones', 28, 'Active', NULL),
    (2, 'Donna Noble', 32, 'Active', NULL),
    (3, 'Dalek Sec', NULL, 'Inactive', '2007-06-23'),
    (4, 'Cyberman Leader', NULL, 'Inactive', '2006-07-08'),
    (5, 'Commander Strax', NULL, 'Active', NULL);

-- Populate Doctor table
INSERT INTO Doctor (character_id, appearance, personality)
VALUES
    (1, 'A tall, thin man with wild hair and a long coat', 'Eccentric, curious, and compassionate'),
    (1, 'A man with a pinstripe suit and a great hair', 'Charismatic, energetic, and witty'),
    (1, 'A young man with a bow tie and a tweed jacket', 'Quirky, enthusiastic, and adventurous');

-- Populate Planet table
INSERT INTO Planet (race_id, coordinates)
VALUES
    (2, 1234),
    (3, 5678),
    (4, 9012),
    (5, 3456);

-- Populate Time table
INSERT INTO Time (timeRFBuinverse, timeRFBplanet)
VALUES
    ('2005-03-26 18:00:00', '2005-03-26 18:00:00'),
    ('2008-06-07 22:00:00', '2008-06-07 22:00:00'),
    ('2010-04-03 15:30:00', '2010-04-03 15:30:00');

-- Populate Journey table
INSERT INTO Journey (planet_id, time_id, doctor_id, description)
VALUES
    (1, 1, 1, 'The Doctor met Rose Tyler and fought off the Auton invasion'),
    (2, 2, 2, 'The Doctor and Martha Jones stopped the Sontaran invasion'),
    (3, 3, 3, 'The Doctor and Donna Noble stopped the Cybermen from conquering Earth');

-- Populate Enemy table
INSERT INTO Enemy (character_id, reason)
VALUES
    (5, 'Tried to destroy the Earth'),
    (6, 'Attempted to convert all humans into Cybermen');

-- Populate Companion table
INSERT INTO Companion (character_id, first_journey_id)
VALUES
    (2, 1),
    (3, 2),
    (4, 3);

-- Populate Users table
INSERT INTO Users (character_id, password_hash, login)
VALUES
    (2, 123456, 'rose_tyler'),
    (3, 789012, 'martha_jones'),
    (4, 345678, 'donna_noble');

-- Populate Message table
INSERT INTO Message (from_user_id, to_user_id, message)
VALUES
    (1, 2, 'Hey Martha, remember that time we fought the Sontarans?'),
    (2, 1, 'Of course! That was a close one.'),
    (3, 1, 'Hello Doctor, I miss our adventures together.');

-- Populate the Character_In_Journey table
INSERT INTO Character_In_Journey (character_id, journey_id)
VALUES
    (1, 1), -- The Doctor in Journey 1
    (2, 1), -- Rose Tyler in Journey 1
    (1, 2), -- The Doctor in Journey 2
    (3, 2), -- Martha Jones in Journey 2
    (1, 3), -- The Doctor in Journey 3
    (4, 3); -- Donna Noble in Journey 3
