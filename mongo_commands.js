use kindle_metadata
db.createCollection("kindle_metadata")
use web_logs
db.createCollection("web_logs")
db.createUser({user:'Mongodbadmin',pwd:'Mongodbadmin',roles:[{role:'readWrite',db:'kindle_metadata'},{role:'readWrite',db:'web_logs'}]})
