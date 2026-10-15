CREATE DATABASE sistema_tickets_db;
CREATE USER 'usuario_tickets'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON sistema_tickets_db.* TO 'usuario_tickets'@'%';
FLUSH PRIVILEGES;