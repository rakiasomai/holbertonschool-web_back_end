-- sql project
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (SELECT sum((SELECT weight FROM projects WHERE corrections.project_id = id) * score) / (SELECT sum(weight) ROM projects) FROM corrections WHERE corrections.user_id = user_id)
WHERE users.id = user_id;
END//
DELIMITER ;
