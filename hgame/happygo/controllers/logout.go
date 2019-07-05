package controllers

import (
	"github.com/astaxie/beego"
	"net/http"
)

type LogoutController struct {
	beego.Controller
}

func (c *LogoutController) Get() {
	c.DestroySession()
	c.Redirect("/auth", http.StatusFound)
}
