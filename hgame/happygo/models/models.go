package models

import (
	"fmt"
	"github.com/astaxie/beego/config"
	"github.com/astaxie/beego/orm"
	_ "github.com/go-sql-driver/mysql"
)

type Users struct {
	Id       int
	Username string
	Password string
	Avatar   string `orm:"default('static/img/avatar.jpg')`
}

type Messages struct {
	Id  int
	Uid int
	Msg string
}

func init() {
	iniconf, _ := config.NewConfig("ini", "conf/app.conf")
	username := iniconf.String("mysql::username")
	password := iniconf.String("mysql::password")
	host := iniconf.String("mysql::host")
	port := iniconf.String("mysql::port")
	database := iniconf.String("mysql::database")
	orm.RegisterDriver("mysql", orm.DRMySQL)
	orm.RegisterDataBase("default", "mysql", fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?allowAllFiles=true", username, password, host, port, database))
	orm.RegisterModel(new(Users))
	orm.RegisterModel(new(Messages))
}
