/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - zero_hunger
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`zero_hunger` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `zero_hunger`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `complaint` varchar(1000) DEFAULT NULL,
  `reply` varchar(1000) DEFAULT NULL,
  `complaint_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `distributor` */

DROP TABLE IF EXISTS `distributor`;

CREATE TABLE `distributor` (
  `distributor_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `distributor_name` varchar(100) DEFAULT NULL,
  `distributor_phone` varchar(100) DEFAULT NULL,
  `distributor_email` varchar(100) DEFAULT NULL,
  `distributor_place` varchar(100) DEFAULT NULL,
  `distributor_pincode` varchar(10) DEFAULT NULL,
  `distributor_district` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`distributor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `distributor` */

insert  into `distributor`(`distributor_id`,`login_id`,`distributor_name`,`distributor_phone`,`distributor_email`,`distributor_place`,`distributor_pincode`,`distributor_district`) values 
(1,3,'Achu','7890654321','achu@gmail.com','Enagandiyur','680613','Thrissur');

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `farmer_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `farmer_name` varchar(100) DEFAULT NULL,
  `farmer_place` varchar(100) DEFAULT NULL,
  `farmer_pincode` varchar(10) DEFAULT NULL,
  `farmer_dob` varchar(100) DEFAULT NULL,
  `farmer_phone` varchar(100) DEFAULT NULL,
  `farmer_email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`farmer_id`,`login_id`,`farmer_name`,`farmer_place`,`farmer_pincode`,`farmer_dob`,`farmer_phone`,`farmer_email`) values 
(1,2,'Arsha','Thrissur','680616','2001-08-11','9876543210','arsha@gmail.com'),
(2,4,'Minnu','Thrissur','680616','2005-06-07','9876543210','minnu@gmail.com');

/*Table structure for table `farmer_item` */

DROP TABLE IF EXISTS `farmer_item`;

CREATE TABLE `farmer_item` (
  `farmer_item_id` int(10) NOT NULL AUTO_INCREMENT,
  `farmer_id` int(10) DEFAULT NULL,
  `item_id` int(10) DEFAULT NULL,
  `farmer_item_stock` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`farmer_item_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `farmer_item` */

insert  into `farmer_item`(`farmer_item_id`,`farmer_id`,`item_id`,`farmer_item_stock`) values 
(1,1,2,'80'),
(3,1,1,'10');

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `item_id` int(10) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(100) DEFAULT NULL,
  `item_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `item` */

insert  into `item`(`item_id`,`item_name`,`item_price`) values 
(1,'Tomato','30'),
(2,'Rice','50');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'arsha','arsha123','farmer'),
(3,'achu','achu123','distributor'),
(4,'minnu','minnu123','farmer'),
(5,'chu','chu123','shelter');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `od_id` int(10) NOT NULL AUTO_INCREMENT,
  `om_id` int(10) DEFAULT NULL,
  `item_id` int(10) DEFAULT NULL,
  `od_quantity` varchar(100) DEFAULT NULL,
  `od_amount` varchar(100) DEFAULT NULL,
  `od_datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`od_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`od_id`,`om_id`,`item_id`,`od_quantity`,`od_amount`,`od_datetime`) values 
(2,1,2,'1','50 ','2025-01-27'),
(5,2,2,'2','50 ','2025-01-28'),
(6,3,2,'5','50','2025-01-31'),
(7,4,2,'10','50','2025-01-31');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `om_id` int(10) NOT NULL AUTO_INCREMENT,
  `distributor_id` int(10) DEFAULT NULL,
  `om_total` varchar(100) DEFAULT NULL,
  `om_datetime` varchar(100) DEFAULT NULL,
  `om_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`om_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`om_id`,`distributor_id`,`om_total`,`om_datetime`,`om_status`) values 
(1,1,'50','2025-01-27','paid'),
(2,1,'100','2025-01-28','paid'),
(3,1,'250','2025-01-31','paid'),
(4,1,'500','2025-01-31','paid');

/*Table structure for table `order_payment` */

DROP TABLE IF EXISTS `order_payment`;

CREATE TABLE `order_payment` (
  `payment_id` int(10) NOT NULL AUTO_INCREMENT,
  `om_id` int(10) DEFAULT NULL,
  `op_amount` varchar(100) DEFAULT NULL,
  `op_datetime` varchar(100) DEFAULT NULL,
  `op_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `order_payment` */

insert  into `order_payment`(`payment_id`,`om_id`,`op_amount`,`op_datetime`,`op_status`) values 
(1,2,'100','2025-01-30','paid'),
(2,3,'250','2025-01-31','paid'),
(3,4,'500','2025-01-31','paid');

/*Table structure for table `shelter` */

DROP TABLE IF EXISTS `shelter`;

CREATE TABLE `shelter` (
  `shelter_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `shelter_name` varchar(100) DEFAULT NULL,
  `shelter_phone` varchar(100) DEFAULT NULL,
  `shelter_email` varchar(100) DEFAULT NULL,
  `shelter_address` varchar(100) DEFAULT NULL,
  `shelter_capacity` varchar(100) DEFAULT NULL,
  `shelter_place` varchar(100) DEFAULT NULL,
  `shelter_pincode` varchar(100) DEFAULT NULL,
  `shelter_district` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`shelter_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `shelter` */

insert  into `shelter`(`shelter_id`,`login_id`,`type_id`,`shelter_name`,`shelter_phone`,`shelter_email`,`shelter_address`,`shelter_capacity`,`shelter_place`,`shelter_pincode`,`shelter_district`) values 
(1,5,2,'Chuhu','9876509812','chu@gmail.com','Xyz House','10','Thrissur','123456','Thrissur');

/*Table structure for table `shelter_type` */

DROP TABLE IF EXISTS `shelter_type`;

CREATE TABLE `shelter_type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `shelter_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `shelter_type` */

insert  into `shelter_type`(`type_id`,`shelter_type`) values 
(1,'Orphnage'),
(2,'Events'),
(3,'Hotel');

/*Table structure for table `surplus_food` */

DROP TABLE IF EXISTS `surplus_food`;

CREATE TABLE `surplus_food` (
  `surplus_id` int(10) NOT NULL AUTO_INCREMENT,
  `item_id` int(10) DEFAULT NULL,
  `quantity_details` varchar(100) DEFAULT NULL,
  `package_type` varchar(100) DEFAULT NULL,
  `expiration_date` varchar(100) DEFAULT NULL,
  `storage_requirement` varchar(100) DEFAULT NULL,
  `supplier_name` varchar(100) DEFAULT NULL,
  `supplier_phone` varchar(100) DEFAULT NULL,
  `storage_location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`surplus_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `surplus_food` */

insert  into `surplus_food`(`surplus_id`,`item_id`,`quantity_details`,`package_type`,`expiration_date`,`storage_requirement`,`supplier_name`,`supplier_phone`,`storage_location`) values 
(1,1,'3','carton','30-01-2025','keep refrigerated','ammu','1234567890','warehouse');

/*Table structure for table `surplus_request` */

DROP TABLE IF EXISTS `surplus_request`;

CREATE TABLE `surplus_request` (
  `request_id` int(10) NOT NULL AUTO_INCREMENT,
  `shelter_id` int(10) DEFAULT NULL,
  `surplus_id` int(10) DEFAULT NULL,
  `surplus_qty_details` varchar(100) DEFAULT NULL,
  `surpls_req_datetime` varchar(100) DEFAULT NULL,
  `surplus_req_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `surplus_request` */

insert  into `surplus_request`(`request_id`,`shelter_id`,`surplus_id`,`surplus_qty_details`,`surpls_req_datetime`,`surplus_req_status`) values 
(1,1,1,'2','2025-01-28','accept');

/*Table structure for table `tutorial` */

DROP TABLE IF EXISTS `tutorial`;

CREATE TABLE `tutorial` (
  `tutorial_id` int(10) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `file_path` varchar(1000) DEFAULT NULL,
  `file_type` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`tutorial_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tutorial` */

insert  into `tutorial`(`tutorial_id`,`title`,`description`,`file_path`,`file_type`) values 
(1,'donation','qqqqqqqqqqqq qqqqqqqqq','static/5cf82998-3a5c-4cde-b75f-45e3463f1561video.mp4','mp4');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
