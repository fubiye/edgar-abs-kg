/**
 *  EDGAR ABS Company (SPV) Analysis
 */
select category, COUNT(1) from (
SELECT 
cik, company,
case 
when lower(company) like '%card%' then 'ABS - CARD'
when lower(company) like '%auto%' then 'ABS - AUTO'
when lower(company) like '%home%' then 'RMBS'
when lower(company) like '%mort%' then 'MBS'
else 'OTHER'
end as category
FROM edgar_company)
spv
GROUP BY category
-- where spv.category = 'OTHER'
;

select loc, count(1) as cnt from edgar_company
group by loc
order by cnt desc
;
/**
 *  EDGAR ABS Company (SPV) Filings Analysis
 */
select company.company as company, count(1) as cnt from edgar_company company
left join edgar_company_filing filing on company.cik = filing.cik
group by company.company
order by cnt desc
limit 10;
select category, count(1) as cnt from (
select company,
case when cnt > 1000 then '> 1000'
when cnt > 500 and (cnt < 1000 or cnt = 1000) then '(500, 1000]'
when cnt > 100 and (cnt < 500 or cnt = 500) then '(100, 500]'
when cnt > 50 and (cnt < 100 or cnt = 100) then '(50, 100]'
when cnt > 40 and (cnt < 50 or cnt = 50) then '(40, 50]'
when cnt > 30 and (cnt < 40 or cnt = 40) then '(30, 40]'
when cnt > 25 and (cnt < 30 or cnt = 30) then '(25, 30]'
when cnt > 20 and (cnt < 25 or cnt = 25) then '(20, 25]'
when cnt > 15 and (cnt < 20 or cnt = 20) then '(15, 20]'
when cnt > 10 and (cnt < 15 or cnt = 15) then '(10, 15]'
when cnt > 5 and (cnt < 10 or cnt = 10) then '(5, 10]'
else '(0, 5]'
end as category
 from (
select company.company as company, count(1) as cnt from edgar_company company
left join edgar_company_filing filing on company.cik = filing.cik
group by company.company
order by cnt desc) company_filing_cnt
) company_filing_cnt_category
group by category
;
select * from edgar_company_filing;

select count(1) from edgar_company_filing;

select yy, count(1) from (
SELECT id, 
-- STR_TO_DATE(trim(effective), '%Y-%m-%d') as eff, 
substr(effective, 1, 4) as yy FROM edgar_company_filing
) filing_by_year
group by yy
order by yy;

select filing_type, sum(cnt) as cnt from ( 
select
case when cnt < 2000 then 'OTHERS'
ELSE filing end as filing_type, cnt from (
select filing, count(1) as cnt from edgar_company_filing 
group by filing
) fling_types) f_types
group by filing_type
order by cnt desc;

/**
 *  EDGAR ABS Company (SPV) Filing Files Analysis
 */
 SELECT * FROM edgar_filing_file;
 
 select count(1) from edgar_filing_file where doc_link not like '%/';
 
 SELECT file_type, count(1) as cnt FROM (
select ID, 
CASE WHEN doc_type = 'GRAPHIC' THEN 'GRAPHIC'
	 WHEN doc_name like '%.txt' THEN 'TXT'
     WHEN doc_name like '%.htm%' THEN 'HTML'
     WHEN doc_name like '%.xml' THEN 'XML'
     WHEN doc_name like '%.pdf' THEN 'PDF'
     else 'OTHERS'
END AS FILE_TYPE
from edgar_filing_file where doc_link not like '%/'
) filing_file_types
group by file_type
order by cnt desc
;
 
-- file count (exclude GRAPHIC) per filing
 
 SELECT c.company, fi.filing, fi.effective, f.filing_id, count(1) as cnt FROM edgar_company c
 left join edgar_company_filing fi on c.cik = fi.cik
 left join edgar_filing_file f on fi.id = f.filing_id
 where f.doc_link not like '%/' and f.doc_type <> 'GRAPHIC'
 group by c.company, fi.filing, fi.effective, f.filing_id
 order by cnt desc
 limit 10;
 
select cfc.count_cate, count(1) as cate from (
 select cf.company, cf.filing, cf.effective, cf.filing_id, cf.cnt,
 case 
	  when cf.cnt = 1 then '1'
      when cf.cnt = 2 then '2'
      when cf.cnt = 3 then '3'
      when cf.cnt = 4 then '4'
      when cf.cnt = 5 then '5'
      when cf.cnt = 6 then '6'
      when cf.cnt = 7 then '7'
      when cf.cnt = 8 then '8'
      when cf.cnt = 9 then '9'
      when cf.cnt = 10 then '10'
	  when cf.cnt > 10 and (cf.cnt < 20 or cf.cnt = 20) then '(10, 20]'
      when cf.cnt > 20 and (cf.cnt < 30 or cf.cnt = 30) then '(20, 30]'
      when cf.cnt > 30 and (cf.cnt < 40 or cf.cnt = 40) then '(30, 40]'
      when cf.cnt > 40 and (cf.cnt < 50 or cf.cnt = 50) then '(40, 50]'
      when cf.cnt > 50 and (cf.cnt < 100 or cf.cnt = 100) then '(50, 100]'
      when cf.cnt > 100 then '> 100'
 end as count_cate
 from (
  SELECT c.company, fi.filing, fi.effective, f.filing_id, count(1) as cnt FROM edgar_company c
 left join edgar_company_filing fi on c.cik = fi.cik
 left join edgar_filing_file f on fi.id = f.filing_id
 where f.doc_link not like '%/' and f.doc_type <> 'GRAPHIC'
 group by c.company, fi.filing, fi.effective, f.filing_id
 ) cf 
) cfc group by cfc.count_cate;

/*
 *  EDGAR ABS Filing Universal
 */ 
 SELECT * 
 FROM edgar_company c
 left join edgar_company_filing fi on c.cik = fi.cik
 left join edgar_filing_file f on fi.id = f.filing_id