-- table user creation
DELIMITER //
CREATE TRIGGER valisation_mail BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END; //
DELIMITER ;
