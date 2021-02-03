-- table user creation
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
	INSERT INTO projects (name)
	SELECT project_name
	FROM DUAL
	WHERE project_name NOT IN (SELECT name FROM projects);
    INSERT INTO corrections (user_id, project_id, score)
    SET @project_id = SELECT id FROM projects WHERE name = project_name
    VALUES (user_id, @project_id, score);
END //
DELIMITER ;