
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
	INSERT INTO projects(name) SELECT project_name from DUAL
	WHERE NOT EXISTS (SELECT * FROM projects WHERE name=project_name LIMIT 1);
     SET @project_id = SELECT id from projects WHERE name=project_name)
	INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @project_id, score);
END //
DELIMITER ;