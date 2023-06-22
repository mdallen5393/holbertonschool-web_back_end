-- SQL script that creates a function `SaveDiv` that
-- divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0.
DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS INT DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    END IF;
    RETURN CAST(a AS float) / CAST(b as float);
END;
//

DELIMITER ;
