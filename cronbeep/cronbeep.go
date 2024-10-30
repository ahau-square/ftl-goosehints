package cronbeep

import (
	"context"
	"os/exec"
	"time"

	"github.com/TBD54566975/ftl/go-runtime/ftl"
)

type Empty struct{}

//ftl:verb
//ftl:schedule "@every 10s"
func Beep(ctx context.Context, _ Empty) error {
	cmd := exec.Command("say", "beep")
	return cmd.Run()
}