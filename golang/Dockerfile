FROM golang:1.18-alpine as build

WORKDIR /usr/src/app

COPY go.mod go.sum ./

RUN go mod download && go mod verify

COPY . .

RUN CGO_ENABLED=0 go build -v -o ./build/fizzbuzz .

FROM scratch

COPY --from=build /usr/src/app/templates/index.html ./templates/index.html

COPY --from=build /usr/src/app/build/fizzbuzz ./fizzbuzz

EXPOSE 8080

ENTRYPOINT [ "./fizzbuzz" ]
