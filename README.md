# DockerSro

**Орындаған:** Жанбай Ақерке
**Пән:** Киберрисктер, 3 СРО, 2 команда

## 1. Docker image: nginx сайты

Файлдар: `Dockerfile`, `index.html`.

```bash
docker build -t my-html-app .
docker run -d -p 8080:80 --name my-site my-html-app
```

Сайт `http://localhost:8080` мекенжайында ашылады.

![Сайт](images/site.png)

## 2. Docker-да PostgreSQL базасы

Сайттың орнына PostgreSQL базасы көтерілді, pgAdmin 4 арқылы қосылды.

```bash
docker run -d --name my-db -e POSTGRES_PASSWORD=<құпия сөз> -e POSTGRES_DB=testdb -p 5433:5432 postgres:18
```

Өз образым (`postgres/` папкасы): `init.sql` арқылы `students` кестесі автоматты түрде жасалады.

```bash
cd postgres
docker build -t my-postgres .
docker run -d --name my-db2 -e POSTGRES_PASSWORD=<құпия сөз> -p 5434:5432 my-postgres
docker exec -it my-db2 psql -U postgres -d testdb -c "SELECT * FROM students;"
```

![База](images/db.png)

## 3. Docker Hub

Үш образ Docker Hub-қа жүктелді: https://hub.docker.com/u/akerke2007

```bash
docker login
docker tag my-html-app akerke2007/my-html-app:v1
docker tag my-postgres akerke2007/my-postgres:v1
docker tag postgres:18 akerke2007/postgres-base:v1
docker push akerke2007/my-html-app:v1
docker push akerke2007/my-postgres:v1
docker push akerke2007/postgres-base:v1
```

| Образ | Сипаттама |
|-------|-----------|
| `akerke2007/my-html-app:v1` | nginx сайты |
| `akerke2007/my-postgres:v1` | PostgreSQL + `students` кестесі |
| `akerke2007/postgres-base:v1` | базалық PostgreSQL 18 образы |

![Docker Hub](images/hub.png)
