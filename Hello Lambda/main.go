package main

import (
	"fmt"

	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
	Name string `json:"name"`
}

type MyResponse struct {
	Message string `json:"response"`
}

func HandleEvent(event MyEvent) (MyResponse, error) {
	return MyResponse{Message: fmt.Sprintf("Hello mr. %s", event.Name)}, nil
}

func main() {
	lambda.Start(HandleEvent)
}

// build
// GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o main main.go
