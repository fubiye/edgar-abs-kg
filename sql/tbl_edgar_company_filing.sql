create table edgar_company_filing(
    cik varchar(12),
    filing varchar(10),
    docs_link varchar(150),
    filing_desc text,
    effective varchar(50),
    file_num varchar(20),
    file_num_raw varchar(50),
    filing_date DATETIME,
    update_ts timestamp default CURRENT_TIMESTAMP,
    index(cik)
);
alter table edgar_company_filing add primary key filing_pk (cik, docs_link);
alter table edgar_company_filing add id int NOT NULL AUTO_INCREMENT primary key;
# alter table edgar_company_filing change id id int NOT NULL AUTO_INCREMENT primary key;
alter table edgar_company_filing modify id int first;