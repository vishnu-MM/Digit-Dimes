/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - digit_dimes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`digit_dimes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `digit_dimes`;

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cart_id`,`pid`,`user_id`,`qty`) values 
(2,2,12,2),
(23,2,0,1),
(24,2,0,1),
(25,12,13,1),
(26,2,13,1);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category-id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) DEFAULT NULL,
  `man_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`category-id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category-id`,`category`,`man_lid`) values 
(1,'laptop',2),
(2,'Phones',2),
(7,'Ear phone',2),
(8,'Smart Phones',11),
(9,'phone case',2);

/*Table structure for table `compalint` */

DROP TABLE IF EXISTS `compalint`;

CREATE TABLE `compalint` (
  `comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `pid` int(50) DEFAULT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `compalint` */

insert  into `compalint`(`comp_id`,`user_lid`,`complaint`,`status`,`replay`,`date`,`pid`) values 
(1,13,'Not Working','replyed','okk vroii','2022-11-07',NULL),
(2,102,'boot loop','pending','okk','2022-12-29',NULL),
(3,102,'still not working','replyed','okk ','2022-12-15',NULL),
(4,16,'hi','pending','pending','2023-01-11',NULL),
(5,13,'haii','replyed','this is wrong!!!!\r\n','2023-02-18',NULL),
(6,0,'not working','pending','pending','2023-02-18',NULL),
(7,13,'dey','pending','pending','2023-02-22',NULL),
(8,13,'worst battery life','pending','pending','2023-02-22',16224),
(9,13,'worst display ever','pending','pending','2023-02-22',2),
(10,13,'worst product ever','pending','pending','2023-02-24',0),
(11,0,'what a pain','pending','pending','2023-02-24',0);

/*Table structure for table `deliverry_assign` */

DROP TABLE IF EXISTS `deliverry_assign`;

CREATE TABLE `deliverry_assign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `deliverry_assign` */

insert  into `deliverry_assign`(`assign_id`,`order_id`,`staff_id`,`status`) values 
(1,1,4,'p');

/*Table structure for table `delivery_rating` */

DROP TABLE IF EXISTS `delivery_rating`;

CREATE TABLE `delivery_rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `assign_id` int(11) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `delivery_rating` */

insert  into `delivery_rating`(`rating_id`,`assign_id`,`rating`,`date`,`review`) values 
(1,1,'Wonderfull','2022-11-12','Wonderfull');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin@a','admin','admin'),
(3,'yadu@gmail.com','987654321','staff'),
(4,'y@gmail.com','987654321','staff'),
(8,'yadhu@gmail.com','987654','staff'),
(9,'vishnuofficial@gmail.com','6238439691','staff'),
(11,'vishnu@gmail.com','1234','manufacture'),
(12,'mh@gmail.com','9685746351','staff'),
(13,'a','a','user'),
(15,'sachu@','sachu','user'),
(16,'bob','Y','user'),
(17,'jw@e','987','manufacture'),
(18,'jw@e','987','manufacture');

/*Table structure for table `manufacturer` */

DROP TABLE IF EXISTS `manufacturer`;

CREATE TABLE `manufacturer` (
  `man_id` int(11) NOT NULL AUTO_INCREMENT,
  `man_lid` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `propreitir_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`man_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `manufacturer` */

insert  into `manufacturer`(`man_id`,`man_lid`,`name`,`propreitir_name`,`email`,`phone`,`place`,`post`,`pin`,`latitude`,`longitude`,`status`,`passwd`) values 
(1,7,'Vineeth','vishnu','sjlkjljs@gmail.com','155286244','vadakara','nadapuram','673504','685221','543779','reject',NULL),
(2,5,'vyshak','sachu','nsbcusk@gmail.com','26435563543','kozhikode','purameri','673503','4843545','54643546','reject',NULL),
(3,9,'neeraj','amal','cnknxkn512@gmail.com','668465455','goa','kulu','141516','3451686484','3476315896','reject',NULL),
(4,10,'Vinu','suni','fufidjio@gmail.com','36652465','ddjfuif','kvbjsd','1446564','1516544','5646565','reject',NULL),
(5,2,'Sachu','Yadu','sachu@gmail.com',' 6238439691','Kannur','mahe','4321','85624','6524','reject',NULL),
(6,20,'apple','vishnu','6238439691','vishnu@gmail.com','usa','nyc','007','951753','753951','reject',NULL),
(7,18,'Motorola','Jhon wick','jw@e','9876543210','nyc','nyc','115599','86248624','48624862','approved','987'),
(8,NULL,'Company 1','Proprietor 1','c1@gmail.com','987654321','Place 1','Post 1','456123','580690470','412052306','pending','c1'),
(9,NULL,'Company 2','Proprietor 2','c2@gmail.com','9638527410','Place 2','Post 2','635241','751862953','953842751','pending','c2'),
(10,NULL,'Company 3','Proprietor 3','c3@gmail.com','9518462730','Place 3','Post 3','624153','753864219','357682419','pending','c3'),
(11,NULL,'Company 4','Propietor 4 ','c4@gmail.com','9685743521','Place 4','Post 4','684268','1573968426','842615739','pending','c4'),
(12,NULL,'Company 5','Proprietor 5','c5@gmail.com','9624853170','Place 5','Post 5','624853','9634568721','7414568293','pending','c5');

/*Table structure for table `order_main` */

DROP TABLE IF EXISTS `order_main`;

CREATE TABLE `order_main` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user-lid` int(11) DEFAULT NULL,
  `man_lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order_main` */

insert  into `order_main`(`order_id`,`user-lid`,`man_lid`,`date`,`amount`,`status`) values 
(1,13,2,'2022-11-12','2500','P');

/*Table structure for table `order_sub` */

DROP TABLE IF EXISTS `order_sub`;

CREATE TABLE `order_sub` (
  `osid` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`osid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order_sub` */

insert  into `order_sub`(`osid`,`order_id`,`pid`,`qty`) values 
(1,1,12,2);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `categort-id` int(11) DEFAULT NULL,
  `man_id` int(11) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `qty` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`pid`,`categort-id`,`man_id`,`product_name`,`price`,`description`,`qty`,`photo`) values 
(2,2,2,'lenovo ','99999','Ram = 6/8/12GB\r\nRom = 128/512 GB\r\nprocessor = Tens','1','/static/product/223623-133606.jpg'),
(12,8,11,'Pixel 6A','52.99','Ram = 6/8/12GB\r\nRom = 128/512 GB\r\nprocessor = Tens','500','/static/product/094722-224711.jpg');

/*Table structure for table `product_review` */

DROP TABLE IF EXISTS `product_review`;

CREATE TABLE `product_review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `user_lid` int(11) DEFAULT NULL,
  `review` varchar(500) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `product_review` */

insert  into `product_review`(`review_id`,`pid`,`user_lid`,`review`,`rating`,`date`) values 
(1,2,101,'nice product , very use full','4.7','2022-12-09'),
(2,12,102,'Battery is too bad','3.5','2022-12-01'),
(3,2,13,'Great product','4','2023-01-01'),
(4,0,13,'Powerful','3.0','2023-02-22'),
(5,0,13,'Good Choice','3.0','2023-02-22'),
(6,0,13,'Masterpiece','5.0','2023-02-22'),
(8,2,13,'best laptop ever','3.0','2023-03-18');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_` int(11) NOT NULL AUTO_INCREMENT,
  `staff-lid` int(11) DEFAULT NULL,
  `man-id` int(11) DEFAULT NULL,
  `sname` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_`,`staff-lid`,`man-id`,`sname`,`age`,`gender`,`place`,`post`,`pin`,`city`,`phone`,`email`) values 
(1,1,2,'Sachu','19','male','vatakara','Vatakara','1234','Vatakara','987456123','sachu@gmail.com'),
(3,4,2,'yadhu','20','Male','purameri','kallachi','643805','Trissur','987654321','y@gmail.com'),
(6,9,2,'Vishnu.MM','19','Male','Purameri','nadapuram','623504','Calicut','6238439691','vishnuofficial@gmail.com'),
(8,12,11,'mohan','36','Male','Kollam','thottakattukara','623844','kollam','9685746351','mh@gmail.com');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `naame` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_lid`,`naame`,`age`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(3,13,'Amal V','222','male','Vadakara','mukkali','6789501','987654678','amalv2255@gmail.com'),
(4,15,'Sachu Raveendran','20','male','vatakara','vatakara','623843','6238439691','sachu@'),
(5,16,'yedusankar c','19','male','vadakara ','purameri ','673504','8848089619','bob');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
