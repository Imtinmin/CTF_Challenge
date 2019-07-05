-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: hctf_kouzone
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `F1444g`
--

DROP TABLE IF EXISTS `F1444g`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `F1444g` (
  `F1a9` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `F1444g`
--

LOCK TABLES `F1444g` WRITE;
/*!40000 ALTER TABLE `F1444g` DISABLE KEYS */;
INSERT INTO `F1444g` VALUES ('hctf{hctf_2018_kzone_Author_Li4n0}');
/*!40000 ALTER TABLE `F1444g` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_admin`
--

DROP TABLE IF EXISTS `fish_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fish_admin` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(32) NOT NULL,
  `name` varchar(255) DEFAULT '',
  `qq` varchar(255) DEFAULT '',
  `per` int(11) NOT NULL DEFAULT '3' COMMENT '权限，1=超级管理员；2=普通管理员；3=未知权限；',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_admin`
--

LOCK TABLES `fish_admin` WRITE;
/*!40000 ALTER TABLE `fish_admin` DISABLE KEYS */;
INSERT INTO `fish_admin` VALUES (1,'admin','be933cba048a9727a2d2e9e08f5ed046','小杰','1503816935',1);
/*!40000 ALTER TABLE `fish_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_ip`
--

DROP TABLE IF EXISTS `fish_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fish_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin` int(11) NOT NULL,
  `ip` varchar(30) DEFAULT NULL,
  `addres` varchar(30) DEFAULT NULL,
  `platform` varchar(150) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_ip`
--

LOCK TABLES `fish_ip` WRITE;
/*!40000 ALTER TABLE `fish_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `fish_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_user`
--

DROP TABLE IF EXISTS `fish_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fish_user` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(32) NOT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `device` varchar(255) DEFAULT '',
  `output` int(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_user`
--

LOCK TABLES `fish_user` WRITE;
/*!40000 ALTER TABLE `fish_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `fish_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fish_user_fake`
--

DROP TABLE IF EXISTS `fish_user_fake`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fish_user_fake` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(32) NOT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `device` varchar(255) DEFAULT '',
  `output` int(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fish_user_fake`
INSERT INTO `fish_user_fake` VALUES (1,'512343234','woainishangderen','223.104.247.244','','2018-11-09 20:38:00','Huawei DUK',0),
(2,'22342344','19990623','213.102.245.245','','2018-11-09 20:38:01','Huawei DUK',0),
(3,'12323234','ttehedfsdf','213.102.245.245','','2018-11-09 20:38:00','Huawei DUK',0),
(4,'9438327474','zjh19970406','213.102.245.245','','2018-11-09 20:05:10','Huawei DUK',0),
(5,'173848483','admin8888','223.104.247.244','','2018-11-09 20:05:20','Huawei DUK',0),
(6,'939303033','wojizhehhh','223.104.247.244','','2018-11-09 20:05:30','Huawei DUK',0),
(7,'1090239123','2333333haixingba','223.104.247.244','','2018-11-09 20:06:00','Huawei DUK',0),
(8,'84466465','zhetizazua','223.104.247.244','','2018-11-09 20:07:01','Huawei DUK',0),
(9,'51234234234','@!jjsjjdn','223.100.245.242','','2018-11-09 20:08:20','Huawei DUK',0),
(10,'556643223','buhuizuoaaa','33.104.247.242','','2018-11-09 20:08:23','Huawei DUK',0),
(11,'34234324324','udnkaj','23.105.147.44','','2018-11-09 20:10:10','Huawei DUK',0),
(12,'986884646','11111111','223.104.247.244','','2018-11-09 20:15:12','Huawei DUK',0),
(13,'846469468','12345678','23.103.27.24','','2018-11-09 20:15:43','Huawei DUK',0),
(14,'98898769','888888888','22.10.147.44','','2018-11-09 20:15:44','Huawei DUK',0),
(15,'512123123','admin123','223.104.247.244','','2018-11-09 20:15:45','Huawei DUK',0),
(16,'123143433','admin888','22.10.24.204','','2018-11-09 20:15:50','Huawei DUK',0),
(17,'84843937','testtesttest','223.104.247.244','','2018-11-09 20:15:51','Huawei DUK',0),
(18,'897987987','woaini','223.104.247.244','','2018-11-09 20:15:53','Huawei DUK',0),
(19,'65637980','5201314ads','203.108.246.214','','2018-11-09 20:15:54','Huawei DUK',0),
(20,'45453459','asdasdasd','203.105.247.201','','2018-11-09 20:15:55','Huawei DUK',0),
(21,'590980980','895qazqaz','117.104.222.243','','2018-11-09 20:15:56','Huawei DUK',0),
(22,'90980989','orzorzorz23333','213.114.247.243','','2018-11-09 20:16:20','Huawei DUK',0),
(23,'864565468','1234asdfg','123.104.247.242','','2018-11-09 20:17:43','Huawei DUK',0);
--

LOCK TABLES `fish_user_fake` WRITE;
/*!40000 ALTER TABLE `fish_user_fake` DISABLE KEYS */;
/*!40000 ALTER TABLE `fish_user_fake` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09  7:40:07
