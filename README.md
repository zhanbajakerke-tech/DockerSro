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

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/adf64f6c-1546-4fc6-a3e4-98365aa97054" />


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

<img width="1600" height="899" alt="WhatsApp Image 2026-10-26 at 22 36 03" src="https://github.com/user-attachments/assets/aaf1587d-ba21-4f80-81d6-3731abe74cd5" />
<img width="1600" height="435" alt="WhatsApp Image 2026-10-26 at 22 36 03 (1)" src="https://github.com/user-attachments/assets/0f210168-9468-40a7-8fc6-c5a6e4478ff9" />

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

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1648c6a0-bc3e-4ca3-88fa-57220211b90f" />

