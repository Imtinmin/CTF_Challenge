package controllers

import (
	"catmsg/models"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/orm"
	"net/http"
	"os"
	"strconv"
)

type AdminController struct {
	beego.Controller
}

func (c *AdminController) Get() {
	uid := c.GetSession("uid")
	if uid == nil {
		c.Abort("500")
	}

	if uid.(int) != 1 {
		c.Redirect("/", http.StatusFound)
		return
	}



	o := orm.NewOrm()
	u := models.Users{Id:uid.(int)}
	us := []models.Users{}

	err := o.Read(&u)
	if err != nil {
		c.Abort("500")
	}

	_, err = o.QueryTable("users").Filter("id__gt",1).All(&us)
	if err != nil {
		c.Abort("500")
	}

	c.Data["Users"] = us
	c.Data["Avatar"] = u.Avatar
	c.Data["Username"] = u.Username
	c.Data["UID"] = u.Id

	c.TplName = "admin.tpl"
}

type UserDelController struct {
	beego.Controller
}

func (u *UserDelController) Get() {
	uid := u.GetSession("uid")
	if uid == nil {
		u.Abort("500")
	}

	if uid.(int) != 1 {
		u.Redirect("/", http.StatusFound)
		return
	}

	id := u.Ctx.Input.Param(":id")
	i, _ := strconv.Atoi(id)
	if i == 1 {
		u.Redirect("/admin", http.StatusFound)
		return
	}

	o := orm.NewOrm()
	user := models.Users{Id:i}
	err := o.Read(&user)
	if err != nil {
		u.Abort("500")
	}

	if user.Avatar != "/static/img/avatar.jpg" {
		os.Remove(user.Avatar)
	}

	o.QueryTable("messages").Filter("uid", id).Delete()
	o.Delete(&user)

	u.Redirect("/admin", http.StatusFound)
}
