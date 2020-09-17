# TrueConf

REST API должно удовлетворять следующие возможности:
### Добавление User
curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""your name"""}" http://localhost:5000/users/api/v1.0/users
### Получение списка User
curl -i http://localhost:5000/users/api/v1.0/users
### Получение User по Id
curl -i http://localhost:5000/users/api/v1.0/users/1
### Редактирование User по Id
curl -i -H "Content-Type: application/json" -X PUT -d "{"""Sex""":"""male"""}" http://localhost:5000/users/api/v1.0/users/2
### Удаление User по Id
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/api/v1.0/users/3
