create table edgar_file_log(
    id int NOT NULL AUTO_INCREMENT primary key,
    file_path varchar(150),
    state varchar(5),
    update_ts timestamp default CURRENT_TIMESTAMP
);