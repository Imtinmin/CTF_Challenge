package controllers

import (
	"catmsg/models"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
	"net/http"
)

type UserInfoController struct {
	beego.Controller
}

func (c *UserInfoController) Get() {
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

	if uid.(int) == 1 {
		c.Data["IsAdmin"] = true
	}

	c.Data["Username"] = u.Username
	c.Data["UID"] = uid.(int)
	c.Data["Avatar"] = u.Avatar
	c.TplName = "userinfo.tpl"
}

func (c *UserInfoController) Post() {
	uid := c.GetSession("uid")
	if uid == nil {
		c.Abort("500")
	}

	f, h, err := c.GetFile("uploadname")
	if err != nil {
		c.Abort("500")
	}
	defer f.Close()
	c.SaveToFile("uploadname", "static/uploads/" + h.Filename)

	o := orm.NewOrm()
	u := models.Users{Id: uid.(int)}

	err = o.Read(&u)
	if err != nil {
		c.Abort("500")
	}
	u.Avatar = "/static/uploads/" + h.Filename
	_, err = o.Update(&u)
	if err != nil {
		c.Abort("500")
	}

	c.Redirect("/userinfo", http.StatusFound)
}
