echo "Downloading kindle metadata"
sudo apt update
sudo apt install unzip
#wget -c https://istd50043.s3-ap-southeast-1.amazonaws.com/meta_kindle_store.zip -O meta_kindle_store.zip
wget -c https://github.com/chiziheng/ziheng-s-first-repo/blob/main/kindle_metadata_final.zip?raw=true -O kindle_metadata_final.zip
unzip kindle_metadata_final.zip
echo "Installing MongoDB"
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
echo "Openning MongoDB port for remote connection" 
sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mongod.conf
sudo systemctl restart mongod
wget https://github.com/chiziheng/ziheng-s-first-repo/blob/main/mongo_commands.js
mongo < mongo_commands.js
mongoimport --db kindle_metadata --collection kindle_metadata --file kindle_metadata_final.json --legacy
#mongo --eval kindle_metadata 'db.kindle_metadata.remove({title: { $exists: false }})'
rm -rf kindle_metadata_final.zip mongo_commands.js
