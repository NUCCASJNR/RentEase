-- sql script


CREATE DATABASE IF NOT EXISTS rentease_db;
       CREATE USER IF NOT EXISTS 'rent_user'@'localhost' IDENTIFIED BY 'Rent_pwd123@';
              GRANT ALL PRIVILEGES ON rentease_db.* TO 'rent_user'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'rent_user'@'localhost';
FLUSH PRIVILEGES;