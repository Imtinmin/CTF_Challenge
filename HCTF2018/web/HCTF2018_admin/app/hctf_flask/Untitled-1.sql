create table `user` (
    `id` int (10) auto_increment, email varchar(120), 
    `password_hash` varchar(128), 
    `username` varchar(64) binary, 
    primary key(`id`));