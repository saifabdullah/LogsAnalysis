# How to Run:
This is a sql-report created with python and posgresql database.
This report can be run in a host machine with python 2.7 and psql database installed. It also needs pythons psql DB-API psycopg2. 
To run this project, the steps necessary are followed:
1. Install Virtual Box latest version.
2. Install latest version of vagrant.
3. Copy the latest vagrantfile from this github repo:
https://github.com/udacity/fullstack-nanodegree-vm
4. Put the vagrantfile in the project folder
5. Open command line and run 'vagrant up' in this folder.
6. Download and put newsdata.sql in the vagrant folder. 
7. Type 'vagrant ssh' in the bash.
8. Type 'psql -d news -f newsdata.sql'
9. After the database is setup, exit from psql with '\q' command.
10. Type 'psql -d news' to enter the database.
11. Create view "viewcount" with the view command given in the 3rd part of this README file.
12. In another bash terminal type vagrant ssh and /cd vagrant.
13. Type 'python logs_analysis.py' to run the report.
14. You will a formatted text output where all three questions has been answered with single sql query.

#Architecture
The logs_analysis.py has been written to generate a report containing all the answers required. First, psycopg module has been imported. and then a connection to the news database has been established. Three functions, namely
top_three_articles(),popular_authors() and high_error_days() has been written and inside those functions the queries needed to get the desired output has been generated. Then those queries are printed with formatting to show the desired text output. At the end, after the main function, the three functions has been called to generate the report.

#Views used in the project
view-name: viewcount
"CREATE VIEW viewcount AS SELECT articles.title,articles.author,count(log.path) as views from articles inner join log on log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title,articles.author ORDER BY views DESC;"

