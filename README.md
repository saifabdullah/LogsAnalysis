# How to Run:
This is a sql-report created with python and posgresql database.
This report can be run in a host machine with python 2.7 and psql database installed. It also needs pythons psql DB-API psycopg2. 
After installing python 2.7 and psql database, the database have to be created by running the newsdata.sql file.
After the database created, run the main logs_analysis.py file from the command line. It will generate a text output by querying the 'news' database,
where 3 questions has been answered with 3 single sql queries.

#Architecture
The logs_analysis.py has been written to generate a report containing all the answers required. First, psycopg module has been imported. and then a connection to the news database has been established. Three functions, namely
top_three_articles(),popular_authors() and high_error_days() has been written and inside those functions the queries needed to get the desired output has been generated. Then those queries are printed with formatting to show the desired text output. At the end, after the main function, the three functions has been called to generate the report.

#Views used in the project
view-name: viewcount
"CREATE VIEW viewcount AS SELECT articles.title,articles.author,count(log.path) as views from articles inner join log on log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title,articles.author ORDER BY views DESC;"

