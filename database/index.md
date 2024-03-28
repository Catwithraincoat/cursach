Sure, here are some indexes that can be added to the tables in the Doctor Who fun site database, along with explanations for why they are needed and which queries will benefit from them:

1. **Index on `Character.name`**
```sql
CREATE INDEX idx_character_name ON Character (name);
```
This index can help improve the performance of queries that filter or sort characters by their name, such as:
```sql
SELECT c.name, r.name AS race, c.age, c.state, c.date_of_death
FROM Character c
JOIN Race r ON c.race_id = r.id
WHERE c.name LIKE 'The Doctor%';
```

2. **Index on `Companion.character_id`**
```sql
CREATE INDEX idx_companion_character_id ON Companion (character_id);
```
This index can help speed up queries that join the `Companion` and `Character` tables, such as:
```sql
SELECT c.name, j.description AS first_journey_description
FROM Companion cp
JOIN Character c ON cp.character_id = c.id
JOIN Journey j ON cp.first_journey_id = j.id;
```

3. **Index on `Enemy.character_id`**
```sql
CREATE INDEX idx_enemy_character_id ON Enemy (character_id);
```
Similar to the index on `Companion.character_id`, this index can improve the performance of queries that join the `Enemy` and `Character` tables, like:
```sql
SELECT c.name, e.reason
FROM Enemy e
JOIN Character c ON e.character_id = c.id;
```

5. **Index on `Journey.doctor_id`**
```sql
CREATE INDEX idx_journey_doctor_id ON Journey (doctor_id);
```
This index can improve the performance of queries that filter or sort journeys by the associated doctor, like:
```sql
SELECT j.description, p.coordinates AS planet, t.timeRFBuinverse, t.timeRFBplanet, c.name AS doctor
FROM Journey j
JOIN Planet p ON j.planet_id = p.id
JOIN Time t ON j.time_id = t.id
JOIN Doctor d ON j.doctor_id = d.id
JOIN Character c ON d.character_id = c.id
WHERE c.name = 'The Doctor';
```

6. **Index on `Message.from_user_id` and `Message.to_user_id`**
```sql
CREATE INDEX idx_message_users ON Message (from_user_id, to_user_id);
```
This index can help improve the performance of queries that retrieve messages based on the sender and recipient users, such as:
```sql
SELECT u.login AS from_user, u2.login AS to_user, m.message
FROM Message m
JOIN User u ON m.from_user_id = u.id
JOIN User u2 ON m.to_user_id = u2.id
ORDER BY m.id;
```

Indexes are used to speed up queries that involve filtering, sorting, or joining tables based on the indexed columns. By creating an index on frequently used columns, the database can quickly locate the relevant rows without having to scan the entire table, leading to improved query performance, especially for large datasets.

When creating indexes, it's important to consider the trade-off between the performance benefits and the additional storage and maintenance overhead. Indexes should be created judiciously, focusing on columns that are frequently used in queries involving filtering, sorting, or joining tables.