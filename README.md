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

## 2. Docker-да PostgreSQL базасы

Сайттың орнына PostgreSQL базасы көтерілді, pgAdmin 4 арқылы қосылды.

```bash
docker run -d --name my-db -e POSTGRES_PASSWORD=<құпия сөз> -e POSTGRES_DB=testdb -p 5433:5432 postgres:18
```

Өз образым (`db/` папкасы): `init.sql` арқылы `students` кестесі автоматты түрде жасалады.

```bash
cd db
docker build -t my-postgres .
docker run -d --name my-db2 -e POSTGRES_PASSWORD=<құпия сөз> -p 5434:5432 my-postgres
docker exec -it my-db2 psql -U postgres -d testdb -c "SELECT * FROM students;"
```

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

## 4. Docker Compose: сайт + база данных + приложение

Репозиторийде сайт (`Dockerfile`, `index.html`), база (`db/`) және приложение (`app/`) бар. Бір командамен 5 контейнер көтеріледі: сайт (nginx), PostgreSQL, Flask приложение, pgAdmin және Redis.

### Іске қосу (3 команда)

```bash
git clone https://github.com/zhanbajakerke-tech/DockerSro.git
cd DockerSro
docker compose up -d --build
```

Тексеру: `docker compose ps`

| Контейнер | Сервис | Порт |
|-----------|--------|------|
| Zh.Akerke.web | сайт (nginx) | 8080 |
| Zh.Akerke.db | PostgreSQL + таблица students | 5433 |
| Zh.Akerke.app | Flask приложение (дб-дан оқиды) | 5000 |
| Zh.Akerke.pgadmin | pgAdmin 4 | 5050 |
| Zh.Akerke.redis | Redis | 6379 |

Тоқтату: `docker compose down`

![docker compose ps](images/compose-ps.png)