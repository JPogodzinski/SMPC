# SMPC
App handling auctions for the purpose of OD project (REST API)

Works on 127.0.0.1:8080

## Technologies
Project is created with:
 * Spring Boot version 2.3.1
 * PostgreSQL

## Item endpoints:
```
GET 127.0.0.1:8080/item/get-all - get list of all items
GET 127.0.0.1:8080/item/{id} - get item by id
POST 127.0.0.1:8080/item/add - add new item in JSON format {name, year, value}
DELETE 127.0.1.1:8000/item/delete/{id} - delete an item
```
## Bidder endpoints:
```
GET 127.0.0.1:8080/bidder/get-all - get list of all bidders
GET 127.0.0.1:8080/bidder/{id} - get bidder by id
POST 127.0.0.1:8080/bidder/add - add new bidder in JSON format {firstName, surname}
DELETE 127.0.1.1:8000/bidder/delete/{id} - delete a bidder
```
## Auction endpoints:
```
GET 127.0.0.1:8080/auction/get-all - get list of all ongoing auctions
POST 127.0.0.1:8080/auction/add - add new auction for specific item in JSON format {item : "id_of_an_item"}
GET 127.0.0.1:8080/auction/{id} - get auction by id
DELETE 127.0.0.1:8080/auction/delete/{id} - delete an auction
POST 127.0.0.1:8080/auction/add-bidder/{auctionId}/{bidderId} - add a bidder to an auction
DELETE 127.0.0.1:8080/auction/delete-bidder/{auctionId}/{bidderId} - delete a bidder from an auction
POST 127.0.0.1:8080/auction/start/{auctionId} - start an auction, solving millionaire's problem is taking place between every bidder and it returns a winner with value of bid
```
## Pairs endpoints:
```
GET 127.0.0.1:8080/pairs/get-all - get pair of public RSA keys of all bidders
GET 127.0.0.1:8080/auction/{id} - get pair by id (id of pair = id of bidder)
```
## Setup
```
To run this project install Docker Engine and Docker Compose then:
$ cd rentcar/src/main/resources
$ sudo docker-compose up
```
