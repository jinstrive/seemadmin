# 创建管理后台数据库
create database seemadmin;
create user 'seemanager'@'localhost' identified by 'seem#manage';
GRANT ALL PRIVILEGES ON seemadmin.* TO 'seemanager'@'localhost' IDENTIFIED BY 'seem#manage';

# 创建seem数据库

create database seem;
create user 'seem'@'127.0.0.1' identified by 'seem#@!';
GRANT ALL ON seem.* TO 'seem'@'127.0.0.1' IDENTIFIED BY 'seem#@!';

FLUSH PRIVILEGES;


# 创建projects

use seem;

CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(20) NOT NULL,
  `english_name` varchar(50) DEFAULT NULL,
  `descr` varchar(5000) DEFAULT NULL,
  `avatar` varchar(500) DEFAULT NULL,
  `author_type` tinyint(2) DEFAULT 0,
  `status` tinyint(2) DEFAULT 1,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `descr` varchar(5000) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `ptype` tinyint(2) DEFAULT 1,
  `status` tinyint(2) DEFAULT 1,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` varchar(5000) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `status` tinyint(2) DEFAULT 1,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `cdn_image` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `image` varchar(255) NOT NULL COMMENT '相对路径, 根路径为:',
  `width` smallint(5) DEFAULT NULL COMMENT '宽度',
  `height` smallint(5) DEFAULT NULL COMMENT '高度',
  `supplier` tinyint(2) NOT NULL COMMENT 'cdn 服务商 1.qiniu',
  `url` varchar(255) NOT NULL COMMENT 'cdn url',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8


CREATE TABLE `banners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` varchar(200) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `status` tinyint(2) DEFAULT 1,
  `weight` tinyint(2) DEFAULT 0,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

alter table projects add column `weight` tinyint(2) DEFAULT 0 after status;
alter table banners add column `weight` tinyint(2) DEFAULT 0 after status;
