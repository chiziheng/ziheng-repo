echo "Downloading kindle metadata"
sudo apt-get update
sudo apt install unzip
#wget -c https://istd50043.s3-ap-southeast-1.amazonaws.com/meta_kindle_store.zip -O meta_kindle_store.zip
wget -c https://github.com/chiziheng/ziheng-s-first-repo/blob/main/kindle_metadata_final.zip?raw=true --output-document=kindle_metadata_final.zip
echo "Unzipping metadata file"
unzip kindle_metadata_final.zip
echo "Installing MongoDB"

