package main

import (
	"context"
	"fmt"
	"os"

	getter "github.com/hashicorp/go-getter"
)

func main() {
	dst := "./dl"
	client := &getter.Client{
		Ctx: context.Background(),
		Src: "https://example.com/fixture.tar.gz",
		Dst: dst,
		Pwd: ".",
		Mode: getter.ClientModeDir,
	}
	if err := client.Get(); err != nil {
		fmt.Fprintln(os.Stderr, "get failed:", err)
		os.Exit(1)
	}
	fmt.Println("downloaded to", dst)
}
