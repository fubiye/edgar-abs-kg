create table edgar_company_filing_craw_log(
    cik varchar(12),
    category int,
    state varchar(10),
    update_ts timestamp default CURRENT_TIMESTAMP,
    constraint fk_crwa_log_cate
    foreign key(category) references edgar_craw_log_category(id)
);