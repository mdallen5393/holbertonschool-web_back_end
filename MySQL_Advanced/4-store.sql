-- SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.
DELIMITER //

CREATE TRIGGER decrease_item
AFTER UPDATE ON orders
FOR EACH Row
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = New.item_name;
END //

DELIMITER ;
