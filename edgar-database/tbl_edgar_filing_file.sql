create table edgar_filing_file(
    id int NOT NULL AUTO_INCREMENT primary key,
    filing_path varchar(150),
    seq varchar(3),
    description varchar(200),
    doc_name varchar(100),
    doc_link varchar(200),
    doc_type varchar(50),
    size int,
    update_ts timestamp default CURRENT_TIMESTAMP
);

ALTER TABLE edgar_filing_file ADD UNIQUE INDEX `idx_path_seq` (`filing_path`,`seq`);