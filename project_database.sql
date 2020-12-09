-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: adventure_everest_team_treks_and_expedition
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `permit_no` int NOT NULL,
  `permit_date` varchar(50) NOT NULL,
  `bill_no` int NOT NULL,
  `member_name` varchar(50) NOT NULL,
  `member_passport_no` varchar(30) NOT NULL,
  `leader_name` varchar(50) NOT NULL,
  `leader_passport_no` varchar(30) NOT NULL,
  `permit_cost` int NOT NULL,
  `garbage_deposit` int NOT NULL DEFAULT '50000',
  `insurance` int NOT NULL DEFAULT '12800',
  PRIMARY KEY (`permit_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,'2000-09-09',1,'sanjiv','1234','ram','4321',1234,50000,12800),(2,'20/09/2020',5413,'1','2','asfd','1',2,50000,12800);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `climbing_permit`
--

DROP TABLE IF EXISTS `climbing_permit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `climbing_permit` (
  `permit_no` int NOT NULL AUTO_INCREMENT,
  `name_of_peak` varchar(50) NOT NULL,
  `height` varchar(30) NOT NULL,
  `climbing_period` varchar(50) NOT NULL,
  `trekking_route` varchar(200) NOT NULL,
  `leader_name` varchar(50) NOT NULL,
  `leader_country` varchar(50) NOT NULL,
  `leader_passport_no` varchar(50) NOT NULL,
  `leader_age` int NOT NULL,
  `leader_sex` varchar(10) NOT NULL,
  `member_name` varchar(50) NOT NULL,
  `member_country` varchar(50) NOT NULL,
  `member_passport_no` varchar(30) NOT NULL,
  `member_age` int NOT NULL,
  `member_sex` varchar(10) NOT NULL,
  `total_no_of_climbers` int NOT NULL,
  `name_of_trekking_company` varchar(200) NOT NULL,
  `name_of_sardar_or_guide` varchar(50) NOT NULL,
  `sardar_or_guide_reg_no` varchar(50) NOT NULL,
  `permit_date` date NOT NULL,
  `permit_cost` varchar(50) NOT NULL,
  PRIMARY KEY (`permit_no`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `climbing_permit`
--

LOCK TABLES `climbing_permit` WRITE;
/*!40000 ALTER TABLE `climbing_permit` DISABLE KEYS */;
INSERT INTO `climbing_permit` VALUES (1,'asdf','1','1','2','asfd','1','1',2,'Male','1','1','2',1,'Male',1,'2','1','1','2000-01-01','2'),(2,'amadablma','1','1','2','asfd','1','1',2,'Male','1','1','2',1,'Male',1,'2','1','1','2000-01-01','2');
/*!40000 ALTER TABLE `climbing_permit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peak`
--

DROP TABLE IF EXISTS `peak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peak` (
  `peak_id` int NOT NULL AUTO_INCREMENT,
  `peak_name` varchar(100) NOT NULL,
  `height` varchar(20) NOT NULL,
  `himalayan_range` varchar(200) NOT NULL,
  `district` varchar(50) NOT NULL,
  `caravan_route` varchar(200) NOT NULL,
  PRIMARY KEY (`peak_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peak`
--

LOCK TABLES `peak` WRITE;
/*!40000 ALTER TABLE `peak` DISABLE KEYS */;
INSERT INTO `peak` VALUES (3,'asdf','6111','Sagarmatha','Solukhumbhu','lukla-dingbouche\n\n');
/*!40000 ALTER TABLE `peak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL DEFAULT 'Employee',
  `password` varchar(50) NOT NULL,
  `confirm_password` varchar(50) NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES (2,'sanjiv','limbu','9800000000','Male','2000-07-01','bhojpur','sanjiv','sanjivlimbu@gmail.com','Admin','root','root'),(3,'asfd','asfd','4','Female','2000-02-02','asdf\n','asfd','afds','Employee','asfd','asf'),(4,'ram','nepali','9999','Male','2000-09-09','asdf\n','ram','ram@gmail.com','Admin','ram123','ram123');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-20 19:14:08
