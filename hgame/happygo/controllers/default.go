package controllers

import (
	"catmsg/models"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
)

type MainController struct {
	beego.Controller
}

func (c *MainController) Get() {
	uid := c.GetSession("uid")
	if uid == nil {
		c.Abort("500")
	}

	o := orm.NewOrm()
	u := models.Users{Id:uid.(int)}

	err := o.Read(&u)
	if err != nil {
		c.Abort("500")
	}

	type Msg struct {
		Id int
		Uid int
		Msg string
		Username string
		Avatar string
	}

	var msgs []Msg
	_, err = o.Raw("SELECT T0.id, T0.uid, T0.msg, T1.username, T1.avatar FROM `messages` T0 INNER JOIN `users` T1 ON T1.`id` = T0.`uid`").QueryRows(&msgs)
	if err != nil {
		c.Abort("500")
	}

	if uid.(int) == 1 {
		c.Data["IsAdmin"] = true
	}

	c.Data["Username"] = u.Username
	c.Data["UID"] = uid.(int)
	c.Data["Avatar"] = u.Avatar
	c.Data["Messages"] = msgs
	c.TplName = "index.tpl"
}

func (c *MainController) Post() {
		uid := c.GetSession("uid")
	if uid == nil {
		c.Abort("500")
	}

	msg := c.GetString("msg")

	o := orm.NewOrm()
	m := models.Messages{Uid:uid.(int), Msg:msg}

	_, err := o.Insert(&m)
	if err != nil {
		c.Ctx.WriteString("false")
		return
	}
	c.Ctx.WriteString("success")
}

type LRController struct {
	beego.Controller
}

func (l *LRController) Get() {
	l.TplName = "login_reg.tpl"
}
