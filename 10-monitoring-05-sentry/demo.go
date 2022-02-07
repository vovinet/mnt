package main

import (
	"io"
	"log"
	"net/http"
	"time"

	"github.com/getsentry/sentry-go"
)

func hello(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello world!")
}

func main() {
	err := sentry.Init(sentry.ClientOptions{
		Dsn: "https://789ad7dd370945f483f3f3b6d152103c@o1137342.ingest.sentry.io/6190050",
	})
	if err != nil {
		log.Fatalf("sentry.Init: %s", err)
	}
	// Flush buffered events before the program terminates.
	defer sentry.Flush(2 * time.Second)

	//sentry.CaptureMessage("It works!")

	mux := http.NewServeMux()
	mux.HandleFunc("/", hello)

	if err := http.ListenAndServe(":8000", mux); err != nil {
		sentry.CaptureException(err)
		//sentry.CaptureMessage("App crashed binding while port")
	}

}
