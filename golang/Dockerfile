FROM golang:1.18-alpine as build

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download && go mod verify

COPY . .

RUN CGO_ENABLED=0 go build -o ./build/fizzbuzz

FROM gcr.io/distroless/static:debug

WORKDIR /app

COPY --from=build /app/templates/index.html ./templates/index.html

COPY --from=build /app/build/fizzbuzz ./fizzbuzz

EXPOSE 8080

ENTRYPOINT [ "./fizzbuzz" ]