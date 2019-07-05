package controllers

import (
	"catmsg/models"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
)

type LoginController struct {
	beego.Controller
}

func (c *LoginController) Post() {
	type login struct {
		Username	string	`form:"username"`
		Password	string 	`form:"password"`
	}
	u := login{}
	if err := c.ParseForm(&u); err != nil {
		c.Abort("500")
	}

	o := orm.NewOrm()
	us := models.Users{Username:u.Username, Password:u.Password}

	err := o.Read(&us, "username", "password")

	if err == orm.ErrNoRows {
		c.Ctx.WriteString("false")
		return
	}

	c.SetSession("uid", us.Id)

	c.Ctx.WriteString("success")
}
