echo "Installing Mysql on the instance" 
sudo apt update
sudo apt install mysql-server
sudo apt install unzip

echo "Creating root user and assign it without password "
sudo mysql -e 'update mysql.user set plugin = "mysql_native_password" where User="root"'
sudo mysql -e 'create user "root"@"%" identified by ""'
sudo mysql -e 'grant all privileges on *.* to "root"@"%" with grant option'
sudo mysql -e 'flush privileges'
sudo service mysql restart

echo "Opening the port for Mysql for remote connect"
sudo systemctl stop mysql
sudo sed /etc/mysql/mysql.conf.d/mysqld.cnf -i 's/127.0.0.1/0.0.0.0/g'
sudo systemctl restart mysql
#systemctl status mysql.service
#sudo service mysql restart
#ps -A|grep mysql
#sudo pkill mysql

echo "Start downloading sql script and book review data"
wget https://raw.githubusercontent.com/chiziheng/ziheng-s-first-repo/main/sql_commands.sql
wget -c https://istd50043.s3-ap-southeast-1.amazonaws.com/kindle-reviews.zip -O kindle-reviews.zip

echo "Executing SQL commans to create table"
unzip kindle-reviews.zip
sudo mysql -e 'source sql_commands.sql'

echo "Loading data into table"
load data local infile 'kindle_reviews.csv' 
into table Reviews
fields terminated by ',' 
enclosed by '"' 
escaped by '"' 
lines terminated by '\n'
ignore 1 lines;

echo "Finish loading data into Mysql table"
rm -rf kindle_reviews.json kindle-reviews.zip sql_commands.sql