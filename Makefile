
build:
	@docker build -t rajalokan/dynamodb-bootstrap .

push: build
	@docker push rajalokan/dynamodb-bootstrap