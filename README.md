# dynamodb-bootstrap

Provides a simple and quick way to populate local dynamoDb(running in Docker) with tables. Currently there is no direct way to populate [dynamodb-local](https://hub.docker.com/r/amazon/dynamodb-local/) docker image. 

## Usage
### Run dynamodb-local and dynamodb-admin
```
docker-compose up -d dynamodb-local dynamodb-admin
```

### Populate DB 
Dynamodb-bootstrap expects db data to be in `data/*` folder and in following format
- schema.yaml (contains table schemas)
- <table_name>.json (contains table data). 

Once these files are ready, running `docker-compose up dynamodb-bootstrap` will populate DB.

### Verify
