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