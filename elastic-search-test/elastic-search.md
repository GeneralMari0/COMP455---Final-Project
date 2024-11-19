# Elastic Search
---

## Docs
---
[docs](https://elasticsearch-py.readthedocs.io/en/latest/)

## Installation
---
You can install it directly or through Docker
[installation instructions](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

> Elasticsearch is built using Java, and includes a bundled version of OpenJDK within each distribution.
> We strongly recommend using the bundled JVM in all installations of Elasticsearch.

---
sample code
https://dev.to/itachiuchiha/using-elasticsearch-with-python-and-flask-2i0e

## Elastic Search in your Flask App
---
https://www.gitauharrison.com/articles/elasticsearch/install-elasticsearch-in-your-localhost
[Implement Search Feature In Your Flask App Using Elasticsearch](https://www.gitauharrison.com/articles/elasticsearch/implement-search-feature-in-your-flask-app)




# will this work?
---
1. install elasticsearch

```fish
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt update
sudo apt install elasticsearch
```
2. start elasticsearch
`sudo service elasticsearch start`





