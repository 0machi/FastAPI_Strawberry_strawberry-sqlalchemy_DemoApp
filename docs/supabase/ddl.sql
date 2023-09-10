-- 参考: https://qiita.com/kabochapo/items/26b1bb753116a6904664
CREATE TABLE dev.countries (
    country_id int PRIMARY KEY,
    country_name varchar(32) NOT NULL
);

CREATE TABLE dev.cities (
    city_id int PRIMARY KEY,
    country_id int REFERENCES dev.countries (country_id) NOT NULL,
    city_name varchar(32) NOT NULL,
    population int NOT NULL
);

INSERT INTO dev.countries
(country_id, country_name)
VALUES
(1, 'Japan'),
(2, 'United Kingdom');

INSERT INTO dev.cities
(city_id, country_id, city_name, population)
VALUES
(1, 1, 'Osaka', 2760000),
(2, 1, 'Nagoya', 2330000),
(3, 1, 'Sapporo', 1960000),
(4, 2, 'London', 9000000);
