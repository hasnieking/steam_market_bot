CREATE TABLE itemvalues (
    id INT NOT NULL AUTO_INCREMENT,
    item_id INT,
    lowest_price INT,
    volume INT,
    median_price INT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);