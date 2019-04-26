# Github Web scrapping & API

# test:
- get data by GET Method
`GET`
```bash
curl -X GET "http://127.0.0.1:8000/repository/nguyenkhacbaoanh" -H "accept: application/json"
```
- crawlling data by POST method
`POST`
```bash
curl -X POST "http://127.0.0.1:8000/githubers/nguyenkhacbaoanh" -H "accept: application/json"
```