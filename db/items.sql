CREATE TABLE items (
    item_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    PRIMARY KEY (item_id),
    UNIQUE (name)
)