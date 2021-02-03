-- table user creation
CREATE TRIGGER minus_item AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET
quantity = quantity - NEW.number
WHERE name = NEW.item_name;
