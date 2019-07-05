package controllers

import (
	"fmt"
	"github.com/astaxie/beego"
	"io/ioutil"
	"net/http"
	"os"
)

type InstallController struct {
	beego.Controller
}

func (c *InstallController) Get() {
	_, err := os.Stat("conf/app.conf")
	if err != nil && os.IsNotExist(err) {
		c.TplName = "install.tpl"
	} else {
		c.Redirect("/", http.StatusFound)
		return
	}
}


func (c *InstallController) Post() {
	_, err := os.Stat("conf/app.conf")
	if err != nil && os.IsNotExist(err) {
		//pass
	} else {
		c.Redirect("/", http.StatusFound)
		return
	}
	type data struct {
		Host string	`form:"host"`
		Port string	`form:"port"`
		Username string	`form:"username"`
		Password string	`form:"password"`
		Database string	`form:"database"`
	}
	d := data{}

	if err := c.ParseForm(&d); err != nil {
		c.Abort("500")
	}

	s := `[mysql]
username = %s
password = %s
host = %s
port = %s
database = %s
`
	err = ioutil.WriteFile("conf/app.conf", []byte(fmt.Sprintf(s, d.Username, d.Password, d.Host, d.Port, d.Database)),0666)
	if err != nil {
		c.Abort("500")
	}
	c.Redirect("/", http.StatusFound)
}
