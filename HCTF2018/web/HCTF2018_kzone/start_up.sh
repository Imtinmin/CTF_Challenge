docker-compose build
echo "running the container"
docker-compose up -d
sleep 6
echo "init the database"
docker exec -it hctf_kouzone /bin/bash /home/init.sh

echo "All finished! Please check the output message to confirm the service is running, or to rebuild"
