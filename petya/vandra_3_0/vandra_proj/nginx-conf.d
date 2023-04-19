upstream app{
    server web:8000;
}

server {

    listen 80;
    server_name test.vandra

}