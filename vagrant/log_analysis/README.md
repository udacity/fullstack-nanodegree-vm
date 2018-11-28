The 


** The view below was created to add a column called article_name to log information in order to simplify the join to the table articles **

news=> create view log_article as select *,substring(path,10) as Article_Name from log;


** The next view was created to consolidate information about logs, articles and authors into a single place **

news=> create view complete_log as select path,ip,method,status,la.time,la.id,article_name,title,a.name from log_article la left join articles on la.article_name = articles.slug left join authors as a on a.id = articles.author;

** The two following views were designed to make the calculation of status error codes percentage easier **
Total views per day
news=> create view total_views_by_day as select count(*) as views, time::date as day from complete_log group by day;

Daily access by status
news=> create view views_by_status as select count(*) as views, time::date as day, status from complete_log group by day,status order by day desc;
