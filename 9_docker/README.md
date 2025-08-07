### Создать контейнер
```python
docker build -t my_first_image . 
```
### Посмотреть доступные контейнеры
```python
docker images
```
### Запустить контейнер
```python
docker run --name=my_first_container -p 1253:8000 my_first_image 

http://localhost:1253/docs
```
### Выключить контейнер
```python
docker rm c69870d2250112ba55512375baba2675a9b12ab8a852b66ddc7eec119f31962b
```
### Войти в контейнер
```python
docker exec -it my_first_container bash
```