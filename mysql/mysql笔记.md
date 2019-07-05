# *mysql-forget*

## *一些花式查询：*

`hex`

```
select hex(([YOUR SQL]))
```

```mysql
select hex((select database()))
```

将查询结果以`hex`编码的方式显示

​	`16进制编码`

```SELECT(extractvalue(0x3C613E61646D696E3C2F613E,0x2f61))
SELECT(extractvalue(0x3C613E61646D696E3C2F613E,0x2f61))
```



`in`

```mysql
select database() in ('xiaocms')
```

> 查询结果相同为1，不同返回0

`like`

```mysql
select database() like ('xiaocms)
```











## *创建视图*

```1&#39; and ascii(substr((select databae()),1,1)
CREATE view [name] AS SELECT * AS VALUE FROM table
```

## *删除视图*

DROP VIEW [name]

## *删除行*

DELETE FROM [table_name] WHERE [colum_name] = xxx

## *删除列*

ALTER TABLE [table_name] DROP column = xxx

