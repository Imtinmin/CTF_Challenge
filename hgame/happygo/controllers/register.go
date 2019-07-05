package controllers

import (
	"catmsg/models"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
)

type RegisterController struct {
	beego.Controller
}

func (c *RegisterController) Post() {
	type register struct {
		Username	string	`form:"username"`
		Password	string 	`form:"password"`
		ConfirmPass	string	`form:"confirmpass"`
	}
	u := register{}
	if err := c.ParseForm(&u); err != nil {
		c.Abort("500")
	}
	if (len(u.Password)&len(u.ConfirmPass) != 0 && u.Password == u.ConfirmPass) {
		o := orm.NewOrm()
		user := models.Users{Username:u.Username, Avatar:"static/img/avatar.jpg"}
		if created, _, err := o.ReadOrCreate(&user, "username"); err == nil {
			if created {
				if o.Read(&user) == nil {
					user.Password = u.Password
					_, err := o.Update(&user)
					if err != nil {
						c.Abort("500")
					}
				} else {
					c.Abort("500")
				}
				c.Ctx.WriteString("success")
				return
			} else if err != nil {
				c.Abort("500")
			} else {
				c.Ctx.WriteString("exist")
				return
			}
		}
	}
}
