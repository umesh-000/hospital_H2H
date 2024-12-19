-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: my_hospital
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `landmark` varchar(150) NOT NULL,
  `lat` varchar(250) NOT NULL,
  `lng` varchar(250) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `addresses_customer_id_105f3d7e_fk_customers_id` (`customer_id`),
  CONSTRAINT `addresses_customer_id_105f3d7e_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (2,'123 Main Street, Springfield','Near Central Park','37.7749','-122.4194',1,'2024-12-06 12:05:19.822029','2024-12-06 12:05:19.822029',2);
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_image` varchar(100) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `admin_user_id_8a7d8779_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'',1);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `all_users`
--

DROP TABLE IF EXISTS `all_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_users`
--

LOCK TABLES `all_users` WRITE;
/*!40000 ALTER TABLE `all_users` DISABLE KEYS */;
INSERT INTO `all_users` VALUES (1,'pbkdf2_sha256$600000$fMIz9tPcvfnh8yciQP7pXR$TbjrRQD7c4Sh9SeTf7tD3DUKEAxnrbQYEyfhWvQSzvU=','2024-12-16 06:41:28.122574',0,'admin','','','admin@gmail.com',0,1,'2024-11-18 13:20:59.534183','admin','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(5,'pbkdf2_sha256$600000$t5aPlEu0H7CLxCs6yshmK1$U0KYxmffQVzy0rbiGYR5dUQut0fWeCUMWTMba8FgG4E=','2024-12-10 13:03:47.031142',0,'bhandari','','','pugejapad@mailinator.com',0,1,'2024-11-19 09:55:15.429272','hospital','2024-11-28 07:32:09.178985','2024-11-29 04:53:16.717420'),(6,'pbkdf2_sha256$600000$ODJ48p5J6phgUXTCpF23cg$TzZmyxfR9k24wdlmszANc1oEJxuWt2sRvjKb7tje8aw=',NULL,0,'apollo','','','gyfo@mailinator.com',0,1,'2024-11-19 10:45:59.501655','hospital','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(8,'pbkdf2_sha256$600000$oQgeDHsNPdyIPsMq3jT9kY$tvBN3/KWxsN5dujXedi0VfNcHRf26DfuVvwOjygMX7s=',NULL,0,'test','Ora ','','hec@mailinator.com',0,1,'2024-11-20 08:08:15.362415','doctor','2024-11-28 07:32:09.178985','2024-12-02 12:43:41.982962'),(10,'pbkdf2_sha256$600000$d467u66taTn9sw6ACcOndg$1WMb8JPghULEGBDCBTuJ4ZcfVUzfiYNKO/wJ8pmLxAw=','2024-12-10 12:43:12.411564',0,'bazidexepi','Myles Bradley','','mofigic@mailinator.com',0,1,'2024-11-20 13:29:09.855189','doctor','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(13,'pbkdf2_sha256$600000$OXIajqaDb7Di39bLwuvdVT$OJwevK6SXiY/EvjWHgE5m7SIaJ0d05/11rGgAKR0N20=',NULL,0,'fefyfyn','','','tiwe@mailinator.com',0,1,'2024-11-25 07:12:14.824551','lab','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(14,'pbkdf2_sha256$600000$Jy2WkjiU4JvLXE1ftMIPQd$CQSnd2CMereeos72/193bAGWzz7COTwys6hSZq+bNhg=',NULL,0,'josopoku','','','lytycaveta@mailinator.com',0,1,'2024-11-25 08:21:00.426975','lab','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(24,'pbkdf2_sha256$600000$MUYkomySM8VWblaG6YXUu7$NgX20SwM+SCaZlP4naVT+sgOP21lHCCS3q4Z576oPJY=',NULL,0,'rosyke','','','cezezixu@mailinator.com',0,1,'2024-11-26 11:49:52.494449','lab','2024-11-28 07:32:09.178985','2024-11-28 07:32:09.522711'),(28,'pbkdf2_sha256$600000$uZgiPZhwsBTyhERm5OYxTa$ygRwV2FbPgCJ/0KZQ5RJ0W0oACLJaZISgXBvkRuV+8Y=',NULL,0,'umesh@gmail.com','','','umesh@gmail.com',0,1,'2024-11-29 11:38:09.842842','customer','2024-11-29 11:38:09.842842','2024-12-05 07:25:16.298362'),(30,'pbkdf2_sha256$600000$n7uuOYfVi0w3KN2ZdhQewC$0ENzQZNMaoK0aMVkTehVB8gH5fpU4ClGSoalKbjDq/I=','2024-12-10 13:28:36.499982',0,'umeshlab','','','umeshlab@gmail.com',0,1,'2024-12-10 12:55:02.267466','lab','2024-12-10 12:55:02.267466','2024-12-10 12:55:02.267466');
/*!40000 ALTER TABLE `all_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `all_users_groups`
--

DROP TABLE IF EXISTS `all_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_users_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `all_users_groups_user_id_group_id_91f65cde_uniq` (`user_id`,`group_id`),
  KEY `all_users_groups_group_id_0a6d6741_fk_auth_group_id` (`group_id`),
  CONSTRAINT `all_users_groups_group_id_0a6d6741_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `all_users_groups_user_id_baa434a7_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_users_groups`
--

LOCK TABLES `all_users_groups` WRITE;
/*!40000 ALTER TABLE `all_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `all_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `all_users_user_permissions`
--

DROP TABLE IF EXISTS `all_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `all_users_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `all_users_user_permissions_user_id_permission_id_225ac33b_uniq` (`user_id`,`permission_id`),
  KEY `all_users_user_permi_permission_id_299e3286_fk_auth_perm` (`permission_id`),
  CONSTRAINT `all_users_user_permi_permission_id_299e3286_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `all_users_user_permissions_user_id_f4013e11_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `all_users_user_permissions`
--

LOCK TABLES `all_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `all_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `all_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allergies`
--

DROP TABLE IF EXISTS `allergies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allergies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allergies`
--

LOCK TABLES `allergies` WRITE;
/*!40000 ALTER TABLE `allergies` DISABLE KEYS */;
INSERT INTO `allergies` VALUES (2,'Soy',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000'),(3,'Seafood',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000'),(4,'Nuts',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000'),(5,'Eggs',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000'),(6,'Fish',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000'),(7,'Gluten',NULL,1,'2024-12-04 17:08:44.000000','2024-12-04 17:08:44.000000');
/*!40000 ALTER TABLE `allergies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_module`
--

DROP TABLE IF EXISTS `app_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_module` (
  `id` int NOT NULL AUTO_INCREMENT,
  `module_name` varchar(150) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_module`
--

LOCK TABLES `app_module` WRITE;
/*!40000 ALTER TABLE `app_module` DISABLE KEYS */;
INSERT INTO `app_module` VALUES (1,'Hospital',1,'2024-11-27 13:32:27.000000','2024-11-27 13:32:27.000000'),(2,'Doctor',1,'2024-11-27 13:32:27.000000','2024-11-27 13:32:27.000000'),(3,'Laboratory',1,'2024-11-27 13:32:27.000000','2024-11-27 13:32:27.000000');
/*!40000 ALTER TABLE `app_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=221 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Token',6,'add_token'),(22,'Can change Token',6,'change_token'),(23,'Can delete Token',6,'delete_token'),(24,'Can view Token',6,'view_token'),(25,'Can add Token',7,'add_tokenproxy'),(26,'Can change Token',7,'change_tokenproxy'),(27,'Can delete Token',7,'delete_tokenproxy'),(28,'Can view Token',7,'view_tokenproxy'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add hospital',9,'add_hospital'),(34,'Can change hospital',9,'change_hospital'),(35,'Can delete hospital',9,'delete_hospital'),(36,'Can view hospital',9,'view_hospital'),(37,'Can add laboratory',10,'add_laboratory'),(38,'Can change laboratory',10,'change_laboratory'),(39,'Can delete laboratory',10,'delete_laboratory'),(40,'Can view laboratory',10,'view_laboratory'),(41,'Can add hospital image',11,'add_hospitalimage'),(42,'Can change hospital image',11,'change_hospitalimage'),(43,'Can delete hospital image',11,'delete_hospitalimage'),(44,'Can view hospital image',11,'view_hospitalimage'),(45,'Can add doctor details',12,'add_doctordetails'),(46,'Can change doctor details',12,'change_doctordetails'),(47,'Can delete doctor details',12,'delete_doctordetails'),(48,'Can view doctor details',12,'view_doctordetails'),(49,'Can add customer',13,'add_customer'),(50,'Can change customer',13,'change_customer'),(51,'Can delete customer',13,'delete_customer'),(52,'Can view customer',13,'view_customer'),(53,'Can add admin',14,'add_admin'),(54,'Can change admin',14,'change_admin'),(55,'Can delete admin',14,'delete_admin'),(56,'Can view admin',14,'view_admin'),(57,'Can add ward',15,'add_ward'),(58,'Can change ward',15,'change_ward'),(59,'Can delete ward',15,'delete_ward'),(60,'Can view ward',15,'view_ward'),(61,'Can add bed',16,'add_bed'),(62,'Can change bed',16,'change_bed'),(63,'Can delete bed',16,'delete_bed'),(64,'Can view bed',16,'view_bed'),(65,'Can add bed status',17,'add_bedstatus'),(66,'Can change bed status',17,'change_bedstatus'),(67,'Can delete bed status',17,'delete_bedstatus'),(68,'Can view bed status',17,'view_bedstatus'),(69,'Can add hospital service',18,'add_hospitalservice'),(70,'Can change hospital service',18,'change_hospitalservice'),(71,'Can delete hospital service',18,'delete_hospitalservice'),(72,'Can view hospital service',18,'view_hospitalservice'),(73,'Can add hospital department',19,'add_hospitaldepartment'),(74,'Can change hospital department',19,'change_hospitaldepartment'),(75,'Can delete hospital department',19,'delete_hospitaldepartment'),(76,'Can view hospital department',19,'view_hospitaldepartment'),(77,'Can add hospital facility',20,'add_hospitalfacility'),(78,'Can change hospital facility',20,'change_hospitalfacility'),(79,'Can delete hospital facility',20,'delete_hospitalfacility'),(80,'Can view hospital facility',20,'view_hospitalfacility'),(81,'Can add specialist category',21,'add_specialistcategory'),(82,'Can change specialist category',21,'change_specialistcategory'),(83,'Can delete specialist category',21,'delete_specialistcategory'),(84,'Can view specialist category',21,'view_specialistcategory'),(85,'Can add symptom',22,'add_symptom'),(86,'Can change symptom',22,'change_symptom'),(87,'Can delete symptom',22,'delete_symptom'),(88,'Can view symptom',22,'view_symptom'),(89,'Can add hospital doctors',23,'add_hospitaldoctors'),(90,'Can change hospital doctors',23,'change_hospitaldoctors'),(91,'Can delete hospital doctors',23,'delete_hospitaldoctors'),(92,'Can view hospital doctors',23,'view_hospitaldoctors'),(93,'Can add clinic category',24,'add_cliniccategory'),(94,'Can change clinic category',24,'change_cliniccategory'),(95,'Can delete clinic category',24,'delete_cliniccategory'),(96,'Can view clinic category',24,'view_cliniccategory'),(97,'Can add doctor clinics',25,'add_doctorclinics'),(98,'Can change doctor clinics',25,'change_doctorclinics'),(99,'Can delete doctor clinics',25,'delete_doctorclinics'),(100,'Can view doctor clinics',25,'view_doctorclinics'),(101,'Can add doctor banner',26,'add_doctorbanner'),(102,'Can change doctor banner',26,'change_doctorbanner'),(103,'Can delete doctor banner',26,'delete_doctorbanner'),(104,'Can view doctor banner',26,'view_doctorbanner'),(105,'Can add Lab Tag',27,'add_labtag'),(106,'Can change Lab Tag',27,'change_labtag'),(107,'Can delete Lab Tag',27,'delete_labtag'),(108,'Can view Lab Tag',27,'view_labtag'),(109,'Can add service',28,'add_service'),(110,'Can change service',28,'change_service'),(111,'Can delete service',28,'delete_service'),(112,'Can view service',28,'view_service'),(113,'Can add lab banner',29,'add_labbanner'),(114,'Can change lab banner',29,'change_labbanner'),(115,'Can delete lab banner',29,'delete_labbanner'),(116,'Can view lab banner',29,'view_labbanner'),(117,'Can add lab service',30,'add_labservice'),(118,'Can change lab service',30,'change_labservice'),(119,'Can delete lab service',30,'delete_labservice'),(120,'Can view lab service',30,'view_labservice'),(121,'Can add lab package',31,'add_labpackage'),(122,'Can change lab package',31,'change_labpackage'),(123,'Can delete lab package',31,'delete_labpackage'),(124,'Can view lab package',31,'view_labpackage'),(125,'Can add Lab Staff',32,'add_labstaff'),(126,'Can change Lab Staff',32,'change_labstaff'),(127,'Can delete Lab Staff',32,'delete_labstaff'),(128,'Can view Lab Staff',32,'view_labstaff'),(129,'Can add app module',33,'add_appmodule'),(130,'Can change app module',33,'change_appmodule'),(131,'Can delete app module',33,'delete_appmodule'),(132,'Can view app module',33,'view_appmodule'),(133,'Can add offer banner',34,'add_offerbanner'),(134,'Can change offer banner',34,'change_offerbanner'),(135,'Can delete offer banner',34,'delete_offerbanner'),(136,'Can view offer banner',34,'view_offerbanner'),(137,'Can add banner',35,'add_banner'),(138,'Can change banner',35,'change_banner'),(139,'Can delete banner',35,'delete_banner'),(140,'Can view banner',35,'view_banner'),(141,'Can add module banner',36,'add_modulebanner'),(142,'Can change module banner',36,'change_modulebanner'),(143,'Can delete module banner',36,'delete_modulebanner'),(144,'Can view module banner',36,'view_modulebanner'),(145,'Can add module offer banner',34,'add_moduleofferbanner'),(146,'Can change module offer banner',34,'change_moduleofferbanner'),(147,'Can delete module offer banner',34,'delete_moduleofferbanner'),(148,'Can view module offer banner',34,'view_moduleofferbanner'),(149,'Can add Expert Talk',37,'add_experttalk'),(150,'Can change Expert Talk',37,'change_experttalk'),(151,'Can delete Expert Talk',37,'delete_experttalk'),(152,'Can view Expert Talk',37,'view_experttalk'),(153,'Can add bed booking',38,'add_bedbooking'),(154,'Can change bed booking',38,'change_bedbooking'),(155,'Can delete bed booking',38,'delete_bedbooking'),(156,'Can view bed booking',38,'view_bedbooking'),(157,'Can add blog',39,'add_blog'),(158,'Can change blog',39,'change_blog'),(159,'Can delete blog',39,'delete_blog'),(160,'Can view blog',39,'view_blog'),(161,'Can add Help Desk Query',40,'add_helpdeskquery'),(162,'Can change Help Desk Query',40,'change_helpdeskquery'),(163,'Can delete Help Desk Query',40,'delete_helpdeskquery'),(164,'Can view Help Desk Query',40,'view_helpdeskquery'),(165,'Can add reminder category',41,'add_remindercategory'),(166,'Can change reminder category',41,'change_remindercategory'),(167,'Can delete reminder category',41,'delete_remindercategory'),(168,'Can view reminder category',41,'view_remindercategory'),(169,'Can add reminder',42,'add_reminder'),(170,'Can change reminder',42,'change_reminder'),(171,'Can delete reminder',42,'delete_reminder'),(172,'Can view reminder',42,'view_reminder'),(173,'Can add allergy',43,'add_allergy'),(174,'Can change allergy',43,'change_allergy'),(175,'Can delete allergy',43,'delete_allergy'),(176,'Can view allergy',43,'view_allergy'),(177,'Can add medication',44,'add_medication'),(178,'Can change medication',44,'change_medication'),(179,'Can delete medication',44,'delete_medication'),(180,'Can view medication',44,'view_medication'),(181,'Can add Feedback',45,'add_feedback'),(182,'Can change Feedback',45,'change_feedback'),(183,'Can delete Feedback',45,'delete_feedback'),(184,'Can view Feedback',45,'view_feedback'),(185,'Can add customer insurance',46,'add_customerinsurance'),(186,'Can change customer insurance',46,'change_customerinsurance'),(187,'Can delete customer insurance',46,'delete_customerinsurance'),(188,'Can view customer insurance',46,'view_customerinsurance'),(189,'Can add family member',47,'add_familymember'),(190,'Can change family member',47,'change_familymember'),(191,'Can delete family member',47,'delete_familymember'),(192,'Can view family member',47,'view_familymember'),(193,'Can add address',48,'add_address'),(194,'Can change address',48,'change_address'),(195,'Can delete address',48,'delete_address'),(196,'Can view address',48,'view_address'),(197,'Can add customer wallet history',49,'add_customerwallethistory'),(198,'Can change customer wallet history',49,'change_customerwallethistory'),(199,'Can delete customer wallet history',49,'delete_customerwallethistory'),(200,'Can view customer wallet history',49,'view_customerwallethistory'),(201,'Can add Doctor Booking',50,'add_doctorbooking'),(202,'Can change Doctor Booking',50,'change_doctorbooking'),(203,'Can delete Doctor Booking',50,'delete_doctorbooking'),(204,'Can view Doctor Booking',50,'view_doctorbooking'),(205,'Can add Notification',51,'add_notification'),(206,'Can change Notification',51,'change_notification'),(207,'Can delete Notification',51,'delete_notification'),(208,'Can view Notification',51,'view_notification'),(209,'Can add FCM Notification',52,'add_fcmnotification'),(210,'Can change FCM Notification',52,'change_fcmnotification'),(211,'Can delete FCM Notification',52,'delete_fcmnotification'),(212,'Can view FCM Notification',52,'view_fcmnotification'),(213,'Can add Lab Order',53,'add_laborders'),(214,'Can change Lab Order',53,'change_laborders'),(215,'Can delete Lab Order',53,'delete_laborders'),(216,'Can view Lab Order',53,'view_laborders'),(217,'Can add Lab Order Item',54,'add_laborderitems'),(218,'Can change Lab Order Item',54,'change_laborderitems'),(219,'Can delete Lab Order Item',54,'delete_laborderitems'),(220,'Can view Lab Order Item',54,'view_laborderitems');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banners`
--

DROP TABLE IF EXISTS `banners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `link` varchar(250) DEFAULT NULL,
  `position` varchar(50) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `app_module_id` int NOT NULL,
  `banner` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `banners_app_module_id_d5e155a5_fk_App_module_id` (`app_module_id`),
  CONSTRAINT `banners_app_module_id_d5e155a5_fk_App_module_id` FOREIGN KEY (`app_module_id`) REFERENCES `app_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banners`
--

LOCK TABLES `banners` WRITE;
/*!40000 ALTER TABLE `banners` DISABLE KEYS */;
INSERT INTO `banners` VALUES (2,'','top',1,'2024-11-27 11:49:37.370066','2024-11-27 12:19:26.185643',1,'banners/logo_PyhUMhh.png'),(3,'https://www.kunoqezelo.cm','top',1,'2024-11-27 11:58:45.087103','2024-12-03 11:56:25.222565',2,'banners/logo_Yug1JS3.png'),(4,'https://www.nuqy.in','top',1,'2024-11-27 12:21:13.718015','2024-11-27 12:21:33.590741',3,'banners/user-removebg-preview.png');
/*!40000 ALTER TABLE `banners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bed_bookings`
--

DROP TABLE IF EXISTS `bed_bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bed_bookings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ward_type` varchar(255) NOT NULL,
  `bed_type` varchar(255) NOT NULL,
  `booking_type` varchar(255) NOT NULL,
  `patient_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `age` int unsigned NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `emergency_contact` varchar(20) DEFAULT NULL,
  `blood_group` varchar(10) NOT NULL,
  `medical_history` longtext,
  `booking_reason` varchar(255) NOT NULL,
  `insurance_info` longtext,
  `admission_date` date NOT NULL,
  `discharge_date` date DEFAULT NULL,
  `booking_date` datetime(6) NOT NULL,
  `time_slot` time(6) DEFAULT NULL,
  `notes` longtext,
  `status` varchar(15) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  `doctor_assigned_id` bigint DEFAULT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bed_bookings_customer_id_1279b1ec_fk_customers_id` (`customer_id`),
  KEY `bed_bookings_doctor_assigned_id_d7c02d79_fk_doctors_id` (`doctor_assigned_id`),
  KEY `bed_bookings_hospital_id_999a5640_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `bed_bookings_customer_id_1279b1ec_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `bed_bookings_doctor_assigned_id_d7c02d79_fk_doctors_id` FOREIGN KEY (`doctor_assigned_id`) REFERENCES `doctors` (`id`),
  CONSTRAINT `bed_bookings_hospital_id_999a5640_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`),
  CONSTRAINT `bed_bookings_chk_1` CHECK ((`age` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bed_bookings`
--

LOCK TABLES `bed_bookings` WRITE;
/*!40000 ALTER TABLE `bed_bookings` DISABLE KEYS */;
INSERT INTO `bed_bookings` VALUES (4,'General Ward','Single Bed','clinic_visit','Umesh Kumar','umesh@gmail.com',25,'9864939226','Neeraj, 9887934512','AB+','Diabetes, Hypertension','Scheduled Surgery','XYZ Health Insurance, Policy #123456789','2024-12-12',NULL,'2024-07-16 18:30:00.000000','13:00:00.000000','Requires special monitoring for blood sugar levels.','in_progress','2024-12-12 07:39:25.738908','2024-12-12 09:53:25.403972',2,NULL,3),(5,'General Ward','Single Bed','clinic_visit','Umesh Prajapati','umesh@example.com',25,'9864939226','Neeraj, 9887934512','AB+','Diabetes, Hypertension','Scheduled Surgery','XYZ Health Insurance, Policy #123456789','2024-12-12',NULL,'2024-12-16 18:30:00.000000','12:45:00.000000','Requires special monitoring for blood sugar levels.','in_progress','2024-12-12 07:57:36.828000','2024-12-12 07:57:36.828997',2,NULL,3),(6,'General Ward','Single Bed','clinic_visit','Umesh Prajapati','umesh@example.com',25,'9864939226','Neeraj, 9887934512','AB+','Diabetes, Hypertension','Scheduled Surgery','XYZ Health Insurance, Policy #123456789','2024-12-12',NULL,'2024-12-16 18:30:00.000000','12:45:00.000000','Requires special monitoring for blood sugar levels.','in_progress','2024-12-12 07:59:24.739720','2024-12-12 07:59:24.739720',2,NULL,3),(7,'General Ward','Single Bed','clinic_visit','Umesh Prajapati','umesh@example.com',25,'9864939226','Neeraj, 9887934512','AB+','Diabetes, Hypertension','Scheduled Surgery','XYZ Health Insurance, Policy #123456789','2024-12-12',NULL,'2024-12-16 18:30:00.000000','12:45:00.000000','Requires special monitoring for blood sugar levels.','in_progress','2024-12-12 07:59:52.337409','2024-12-12 07:59:52.337409',2,NULL,3);
/*!40000 ALTER TABLE `bed_bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bed_status`
--

DROP TABLE IF EXISTS `bed_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bed_status` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `bed_id` bigint DEFAULT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bed_status_bed_id_fe2bfb7a_fk_beds_id` (`bed_id`),
  KEY `bed_status_hospital_id_d315ccb0_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `bed_status_bed_id_fe2bfb7a_fk_beds_id` FOREIGN KEY (`bed_id`) REFERENCES `beds` (`id`),
  CONSTRAINT `bed_status_hospital_id_d315ccb0_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bed_status`
--

LOCK TABLES `bed_status` WRITE;
/*!40000 ALTER TABLE `bed_status` DISABLE KEYS */;
INSERT INTO `bed_status` VALUES (1,1,'2024-11-19 12:00:20.450980','2024-11-19 12:09:42.764841',4,4),(3,0,'2024-11-19 12:13:58.036102','2024-11-19 12:13:58.036102',4,3);
/*!40000 ALTER TABLE `bed_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beds`
--

DROP TABLE IF EXISTS `beds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beds` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bed_type` varchar(100) NOT NULL,
  `bed_count` int NOT NULL,
  `sale_price` decimal(10,2) NOT NULL,
  `sale_bed_price` decimal(10,2) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hospital_id` bigint DEFAULT NULL,
  `ward_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `beds_hospital_id_bc3d25e9_fk_hospitals_id` (`hospital_id`),
  KEY `beds_ward_id_f6024cbf_fk_wards_id` (`ward_id`),
  CONSTRAINT `beds_hospital_id_bc3d25e9_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`),
  CONSTRAINT `beds_ward_id_f6024cbf_fk_wards_id` FOREIGN KEY (`ward_id`) REFERENCES `wards` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beds`
--

LOCK TABLES `beds` WRITE;
/*!40000 ALTER TABLE `beds` DISABLE KEYS */;
INSERT INTO `beds` VALUES (3,'General',10,800.00,1000.00,1,'2024-11-19 11:28:55.068844','2024-11-19 11:35:58.185551',4,1),(4,'ICU',10,800.00,1000.00,1,'2024-11-19 11:36:16.696853','2024-11-19 11:36:16.696853',4,3);
/*!40000 ALTER TABLE `beds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blogs`
--

DROP TABLE IF EXISTS `blogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blogs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `video` varchar(500) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs`
--

LOCK TABLES `blogs` WRITE;
/*!40000 ALTER TABLE `blogs` DISABLE KEYS */;
INSERT INTO `blogs` VALUES (1,'Join Care2Home as doctor','India, Bengaluru, 24th August 2022: Practo’s hospital management system, Insta, trusted by 1500+ healthcare centres globally, today announced its transition to SaaS model to drive more value, efficiency, flexibility and scalability for its partner clinics and hospitals. \r\n\r\nThe development, part of the company’s holistic growth and profitability strategy, is expected to impact the topline positively, with a 25% increase in healthcare centres. With this move, the company aims to improve its integration, enabling timely upgrades and greater ease of use, at 4x lesser costs as compared to conventional IT infrastructures. \r\n\r\nInsta’s ambitious expansion path includes going deeper into the Middle East and Indian markets by providing for local needs. It will also enable hospitals to improve operational efficiency by 20-25% with minimal revenue leakage.\r\n\r\n Post-acquisition in 2015 by Practo, Insta has grown 368% in terms of the number of hospitals and clinics using the service and is clocking a 25-30% revenue growth year-on-year, over the last two to three years. Due to consistent on-demand service and highly automated systems, the retention rate for the business has been 92% – one of the highest in the industry. \r\n\r\nInsta is associated with hospitals like Apollo Health and Lifestyle, Ovum, Bansal, Omni Hospitals in India and Emirates Healthcare, Right Health, Etihad Airways Medical Centre, VPS- Lifeline, VPS-Lifecare, Valiant Clinic in UAE amongst others. \r\n\r\nSpeaking on this development, Abhinav Lal, Co-founder and Chief Technology Officer, Practo said, “We remain committed to our goal of balancing growth with profitability. While our consumer business continues to grow, our B2B business is turning profitable. This transition to SaaS is a strategic step in that direction. It helps us anticipate revenues, shorten sales lifecycle, and deepen integration, thus, creating a more predictable ecosystem for both growth and profitability. We are the leaders in the Middle East market and will continue to invest in that market, to grow both market and revenue share. The India market is ripe for SaaS; it provides much-needed agility that healthcare players are looking for, thus, giving us the confidence of further expansion, in a shorter period of time.”\r\n\r\nSpeaking on Practo’s software, Vikas Kumar, CEO, Insta, said, “SaaS-based cloud solutions have many advantages over traditional systems, such as lower costs, better data security and interoperability, and easier access to information and data sharing. The convenience, agility and cost-optimisation offered by Insta will ultimately contribute to creating a more connected health infrastructure in India and abroad. This is a true example of building in India, for India and the world.” \r\n\r\nDiscussing the impact of Insta by Practo, Sudha Kamalnath, Chief Operating Officer, Sagar Chandramma Hospitals, Bangalore said, “We have been working with Insta for over 7+ years now and have been using the software across our centres. The move to SaaS has helped improve our efficiency by 85% and reduced inventory leakage by 95%. Overall, we are seeing improved collaboration between different departments and streamlined processes, which has helped us serve our patients better.”\r\n\r\nLike many other industries, Covid-19 has put a spotlight on the need for the adoption of healthcare systems to SaaS-based models. And the cloud computing market in healthcare is estimated to reach $51.9 billion by 2024. The adoption of cloud-based solutions also helps healthcare organisations to cut down on the unnecessary expenditure of maintaining legacy IT systems while providing greater collaboration for better patient care.','blog_images/4642a8f387560c4eaa0ba769f88ed659.jpg','https://vimeo.com/444676094',1,'2024-12-03 18:15:38.071984','2024-12-04 05:29:37.141656'),(3,'7 Foods That Reduce Bloating—and 5 That Cause It','If you feel uncomfortably bloated after meals, it might be time to look at the types of foods you are eating. We asked a nutritionist for the top foods that lead to bloat, plus the seven best foods you should eat to reduce uncomfortable bloat and gas.\r\n\r\n01\r\nof 13\r\nWorst: Broccoli, Cabbage, and Kale\r\nKale, broccoli, and cabbage are cruciferous vegetables and contain raffinose—a sugar that remains undigested until bacteria in your gut ferment it. That produces gas and makes you bloat. However, eating them more often can actually help in the long run. \"Consistently eating nutrient-rich, high-fiber foods leads to having a stronger, healthier digestive system that\'s less prone to bloating,\" said Cynthia Sass, RD, Health contributing nutrition editor.\r\n\r\nSo keep eating the green veggies, but limit your portions. And if you absolutely can\'t part ways with even a gram of kale, steam it: \"Cooking any vegetable softens the fiber and shrinks the portion as some of the water cooks out, so it takes up less space in the GI tract,\" Sass said. It won\'t eliminate or prevent bloating altogether, but it may make your veggies easier to digest.\r\n\r\n02\r\nof 13\r\nWorst: Legumes\r\nBeans—along with lentils, soybeans, and peas— are known as gas-causing foods. Although they contain more than enough protein, they also contain sugars and fibers that our bodies can\'t absorb. So when legumes reach the large intestine, your gut bacteria take the lead and feast on them. This process leads to gas, which can balloon your waist.\r\n\r\nCombine legumes with easily digestible whole grains, like rice or quinoa. Your body will eventually get used to them. \"If you eat fruits, veggies, nuts, whole grains, and beans often, they won\'t bother you as much as if you eat them sporadically,\" Sass said.\r\n\r\n03\r\nof 13\r\nWorst: Dairy\r\nIf you feel gassy after a few slices of cheese or a bowl of cereal with milk, you may be lactose intolerant—which means your body lacks the necessary enzymes to break down lactose (the sugar found in dairy products). When that occurs, according to a June 2022 Mbio study, it can cause gas to form in the GI tract, which may trigger bloating.\r\n\r\nSo before all that gas gets to you, steer clear of dairy products and opt for the many lactose-free or nondairy alternatives out there. The American Gastroenterological Association (AGA) also suggested the use of lactase tablets like Lactaid, which help people digest foods that contain lactose.\r\n\r\n04\r\nof 13\r\nWorst: Apples\r\nHigh in fiber, apples also contain fructose and sorbitol, sugars found in fruits that many people can\'t tolerate, Sass said—which leads to gas and the inevitable puffy feeling.\r\n\r\nApples are a great snack, however, so don\'t give up on them altogether. \"Eating apples specifically has been linked to a lower risk of heart disease and respiratory problems, including asthma, bronchitis, and emphysema,\" Sass explained. Eat them in moderation and separately from meals, and time your eating right: \"If you\'ll be wearing a form-fitting outfit or bathing suit, you might not want to reach for an apple,\" Sass said. Other fruits that bloat are pears, peaches, and prunes.\r\n\r\n05\r\nof 13\r\nWorst: Salty Foods\r\nEating high-sodium foods can trigger water retention, which can balloon you up, Sass said.\r\n\r\nAvoiding sodium isn\'t as simple as not using the saltshaker, however. The CDC reported that about 90% of Americans consume more sodium than is recommended for a healthy diet (2,300 mg per day for most people, and 1,500 mg for adults over 50, plus people with diabetes, high blood pressure, and high risk of hypertension).\r\n\r\nSodium sneaks its way into most processed and packaged foods, including soups, breads, and these other surprisingly salty fast foods. That makes it very difficult to avoid. When and if you do end up eating a lot of salty food, drink a lot of water to help flush out the salt.\r\n\r\n06\r\nof 13\r\nBest: Cucumber\r\nPeople use cucumbers to reduce puffiness under their eyes—and you can eat them to do the same thing for your belly. The vegetable contains quercetin, a flavonoid antioxidant that helps reduce swelling, Sass said.\r\n\r\n\"Cucumbers have been shown to inhibit the activity of pro-inflammatory enzymes,\" Sass added. So slice it up and eat it as is, or swap sugary drinks with a glass of cucumber water.\r\n\r\n07\r\nof 13\r\nBest: Bananas\r\nFoods rich in potassium—like bananas, plus avocados, kiwis, oranges, and pistachios—prevent water retention by regulating sodium levels in your body and can thus reduce salt-induced bloating. Bananas also have soluble fiber, which can relieve or prevent constipation.\r\n\r\n\"Bloating can also be caused by constipation,\" Sass said. \"If you\'re not able to eliminate waste in the GI tract, you become \'backed up\' so to speak, which can lead to a bloated look.\"\r\n\r\n08\r\nof 13\r\nBest: Papaya\r\nAccording to a December 2020 IOP Conference Series: Earth and Environmental Science paper, papain (the enzyme in papaya) helps break down proteins in your GI system, which makes digestion easier. Sass said that the tropical fruit also has anti-inflammatory properties, as well as fibers that support a strong digestive tract. Eat papaya whole and fresh or blended into a smoothie.\r\n\r\n09\r\nof 13\r\nBest: Asparagus\r\nAsparagus is an anti-bloating superfood: It helps you to urinate, which flushes all that excess water to relieve any discomfort and bloat.\r\n\r\nIt also contains prebiotics, which help support the growth of \"good\" bacteria, according to Sass. This helps maintain a healthy balance in your digestive system to prevent or reduce gas.\r\n\r\nFinally, the vegetable contains soluble and insoluble fibers, which helps promote overall digestive health.\r\n\r\n10\r\nof 13\r\nBest: Yogurt With Probiotics\r\nProbiotics, which are good bacteria in your gut, help regulate digestion and champion the overall health of your digestive tract. You can take probiotic supplements, but you may as well get a breakfast out of it. So eat your bloat away with yogurt that has active cultures. If you want to add some sweetness, use a little honey, jam, or granola.\r\n\r\n11\r\nof 13\r\nBest: Fennel Seeds\r\nFennel does wonders for your digestive tract—especially since you can gain benefits from multiple parts of the vegetable. The seeds have a compound that relaxes GI spasms, which allows gas to pass and relieve bloating, Sass said. You can also chew on the seeds directly or sip on a fennel tea at the end of a meal.\r\n\r\n12\r\nof 13\r\nBest: Ginger\r\nGinger contains the digestive enzyme zingibain. which helps your digestive system break down protein. The compound potentially helps food be digested more easily, reducing bloat, gas, or constipation.\r\n\r\nIf you already feel bloated, you probably don\'t want to eat—so instead, sip homemade ginger tea: Steep a few slices of sliced ginger in a mug of hot water for five to 10 minutes.\r\n\r\n13\r\nof 13\r\nBest: Peppermint and Chamomile Teas\r\nIf you\'re feeling puffy after dinner, you can sip on a hot cup of peppermint or chamomile tea. Both kinds relax GI muscles, per an April 2020 Journal of Medicinal Plants Studies article, to help dissipate the gas that causes your stomach to bloat. Aside from improving digestion, chamomile can also soothe and relax, which can help ease any sort of stomach discomfort.','blog_images/5dd00758a52b9a386ac08fd7b07dade6.jpeg','https://vimeo.com/444676094',1,'2024-12-03 18:27:17.076264','2024-12-04 06:12:16.648757'),(4,'Home Remedies to Relieve Heartburn','Heartburn is a painful or burning sensation that may occur just below or behind the breast bone.¹\r\n\r\nMore than 60 million people in America experience heartburn at least once a month. It is most commonly caused by acid reflux or a chronic condition called gastroesophageal reflux disease (GERD).²\r\n\r\nHome remedies may help relieve symptoms of heartburn or prevent them from occurring. Learn more about these remedies, as well as when to see a doctor.\r\n\r\nAt-Home Heartburn Remedies to Try\r\nIt is possible to treat mild cases of heartburn at home. Some remedies may help relieve this symptom when it occurs and may help prevent it from occurring at all. Here are some strategies that may provide relief:\r\n\r\nElevate the Bed\r\nThe National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) advises waiting two to three hours after eating a meal before lying down.³\r\n\r\nSleeping with your head raised may also help avoid heartburn. Raising the head 6 inches higher than the stomach can help stop food from traveling up the esophagus.²\r\n\r\nThis can be achieved by using a wedge pillow under the mattress, or using blocks or bricks to raise the legs of the bed at the head of the bed. Using extra pillows may not be effective as it is easy to slip off of them during the night.\r\n\r\nChew Gum\r\nChewing gum may be an easy way to help relieve mild cases of heartburn.\r\n\r\nWhen a person chews gum, saliva is produced. Saliva contains enzymes which makes it slightly alkaline. When saliva is swallowed, this can help reduce heartburn, explains the Gastrointestinal (GI) Society/Canadian Society of Intestinal Research.⁵ A small, older study in the Journal of Dental Research backs that up. It found that chewing sugar-free gum for 30 minutes after eating can reduce reflux, a common cause of heartburn.⁶,²\r\n\r\nHowever, the the GI Society says consuming too much artificially sweetened gum may cause diarrhea in some people. Ingesting air while chewing gum can also lead to gas and bloating. It is best to chew gum in moderation to avoid issues like flatulence.⁶ It\'s also best to avoid spearmint and peppermint gum. Mint can relax the ring of muscles connecting the esophagus to the stomach, called the lower esophageal sphincter, allowing stomach contents to back up.⁶,⁸\r\n\r\nTake an Antacid\r\nIn some cases, a healthcare provider may recommend antacids to treat heartburn that is mild. These should not be used every day or in the event of severe symptoms, unless advised by a doctor.³\r\n\r\nAntacids can be purchased over the counter. They may cause side effects like constipation or diarrhea.⁹\r\n\r\nAvoid Trigger Foods\r\nSome people who experience heartburn may find that certain foods can trigger their symptoms or worsen symptoms.\r\n\r\nThe NIDDK says that in some cases, a healthcare provider may recommend reducing intake of these foods or avoiding them all together.¹⁰\r\n\r\nFoods that have been identified as potential triggers include:¹⁰\r\n\r\nSpicy foods\r\nFoods high in fat\r\nMint\r\nCoffee\r\nChocolate\r\nAlcohol\r\nCitrus fruits\r\nTomatoes\r\nDrink Milk\r\nDrinking a glass of cold milk may help assist with relieving symptoms of heartburn, but views on this are mixed.\r\n\r\nMilk and dairy are not on the list of \"trigger foods\" that the American College of Gastroenterology advises people with heartburn to avoid.¹¹ And while he GI Society notes that the alkaline effects of milk may make it a soothing beverage, it can also make things worse. The fat and protein in milk may cause heartburn to become worse during digestion.⁵\r\n\r\nAn alternative is calcium-based over-the-counter remedies, like Tums, which offer the same benefits.³\r\n\r\nConsider Taking Baking Soda\r\nBaking soda may be an easily accessible at home remedy for heartburn, but it should be used in moderation.⁹\r\n\r\nBaking soda (sodium bicarbonate) is alkaline and may help neutralize acidity. Some research suggests that it is safe to use occasionally, but overuse can result in alkalosis. This can result in symptoms like vomiting, nausea, muscle spasms and confusion. Baking soda is also high in sodium which may interfere with the absorption of some medications.⁵\r\n\r\nReduce Belly Fat\r\nHaving an excessive amount of fat in the abdominal area is one of biggest risk factors for heartburn.¹¹\r\n\r\nLosing weight is a good idea if you are overweight or obese. Obesity leads to an increase in pressure in the stomach, which in turn pushes the contents of the stomach into the esophagus, which can cause heartburn.¹¹\r\n\r\nGERD (gastroesophageal reflux disease) is a serious form of acid reflux which causes heartburn. In some people who are overweight, symptoms of GERD will vanish when the person loses 10 to 15 pounds.¹\r\n\r\nQuit Smoking and Stop Using Tobacco\r\nQuitting smoking if you smoke is an effective way to help reduce symptoms of heartburn.⁴\r\n\r\nIt is also a good idea to stop using any other tobacco products. Chemicals found in both cigarettes and tobacco can weaken the muscles located at the lower part of the esophagus (the lower esophageal sphincter). When this happens, food or acid from the stomach can travel into the esophagus, causing heartburn.⁴\r\n\r\nTry Gingerroot\r\nGinger can help a variety of gastrointestinal complaints like nausea or stomach ache. It may also help reduce acid reflux, which can cause heartburn. But it should be used in moderation.⁵\r\n\r\nSome research suggests that it might reduce the production of acid in the stomach, but more research is needed in this area.⁵\r\n\r\nChange Your Clothing\r\nClothes that are tight around the waist can squeeze the stomach in. This may force food back up the esophagus, causing acid reflux and heartburn.¹\r\n\r\nWearing loose clothing and avoiding belts that are tight around the waist may help reduce symptoms of heartburn.¹\r\n\r\nWhen to See a Healthcare Provider\r\nIt is important to treat heartburn, as reflux may damage the esophageal lining.¹¹\r\n\r\nYou should see a doctor immediately if you have heartburn and:¹\r\n\r\nYou have a crushing, burning, squeezing or pressure like feeling in the chest (this may indicate a heart attack)\r\nYou have black or maroon stools\r\nYou are vomiting up blood or what looks like coffee grounds\r\nYou should also call your healthcare provider if you have heartburn and:\r\n\r\nIt occurs often\r\nIt won\'t go away with self-care after a few weeks\r\nSymptoms worsen with antacids\r\nYou believe a medication may be causing the heartburn\r\nYou are losing weight unintentionally\r\nYou are having difficulties with swallowing\r\nYou are wheezing\r\nYou have a cough that won\'t go away\r\nRecap\r\nHeartburn can be uncomfortable, but there are a number of home remedies that may help. Sleeping with the head elevated, taking antacids, chewing gum, avoiding trigger foods, and losing abdominal fat, among other things, may help relieve or prevent symptoms. If you are experience concerning symptoms like vomiting up blood or black stools, you should see a doctor immediately.','blog_images/58e266b8778fec12962e3f759675b029.jpeg','',1,'2024-12-04 05:12:01.387446','2024-12-04 05:31:23.890739'),(5,'Can Sleeping Pills Make Acid Reflux Worse? The Answer Isn\'t Cut and Dry','Although some people downplay its importance (ie I\'ll sleep when I\'m dead), sleep is necessary to live. It also affects your health. According to the Centers for Disease Control and Prevention (CDC), sleep disturbances have been linked to several chronic conditions, including type 2 diabetes, heart disease, and depression. Sleep deprivation can be a cause of motor vehicle accidents, and sleep quality is related to your quality of life in general.\r\n\r\nDespite its importance, many people have trouble sleeping—in the US, insomnia affects up to one-third of the adult population. And if you\'re one of the ones running on fumes, in desperate need of sleep, you might turn to a sleep aid to help get the Zzzs you need.\r\n\r\nYou wouldn\'t be alone. In a 2017-2018 CDC survey, 8.2% of American adults reported using a sleep aid at least four times during the previous week. But if you\'re one of the millions of people who have gastroesophageal reflux disease (GERD), could popping that sleeping pill make your GERD worse?\r\n\r\nThe Study That Made Headlines\r\nAccording to the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK), about 20% of the US population has GERD, which occurs when the muscles (collectively referred to as the lower esophageal sphincter) between the esophagus and stomach are weak or relax inappropriately. This allows the acid contents in the stomach to back up—or \"reflux\"—into the esophagus, typically causing heartburn and other symptoms.\r\n\r\nIn 2009, a study by researchers at Thomas Jefferson University Hospital in Philadelphia made headlines when they found that people taking the popular sleep aid Ambien (zolpidem) snoozed through nighttime reflux instead of arousing from slumber for the second or two it takes to swallow.\r\n\r\nSwallowing is the body\'s natural defense against the backwash of stomach acids that can bathe the esophagus at night. \"[Swallowing] protects your esophagus because you neutralize the acid with saliva, which is rich in bicarbonate,\" explained lead study author Anthony J DiMarino, MD, Dorrance H Hamilton professor of medicine at Jefferson Medical University and the chair of the hospital\'s Division of Gastroenterology and Hepatology.\r\n\r\nOver Time Acid Can Damage the Esophagus\r\nAt the time the study was published, Donald O. Castell, MD, a former professor of medicine at the Medical University of South Carolina, said that the study was \"extremely important\" for GERD patients. \"It sends a definite warning that serious levels of acid reflux can occur without detection after a sleeping aid and that the prolonged acid exposure has the potential to produce injury to the esophageal lining that might not otherwise occur,\" stated Dr. Castell.\r\n\r\nIf left untreated, long-term acid reflux can damage the cells lining the esophagus, leading to, among other things, a precancerous condition known as Barrett\'s esophagus—which, in turn, increases the risk of esophageal cancer. Although the study showed that sleeping pills might increase nighttime exposure to stomach acid, it\'s not clear if they increase the risk of Barrett\'s esophagus or other conditions—Ambien is only recommended for short-term use and the study sample was small and short (just two nights).\r\n\r\nHowever, it may have been the first study to systematically examine the effect of taking a sleep aid on nocturnal acid exposure, said Dr. Castell.\r\n\r\nNext Page: Acid reflux lasted much longer\r\n\r\nWhat Have Other Studies Shown?\r\nIt\'s important to remember that one study can\'t always stand on its own. That\'s why different researchers test theories over and over again, trying to replicate the same or similar results.\r\n\r\nFor example, in a 2016 study published in the Journal of Clinical Gastroenterology, researchers tested the use of Rozerem (ramelteon) in people with GERD to see if their symptoms of heartburn improved. Symptoms did improve, and since Rozerem and Ambien are similar in their action on the body, it calls into question the results of the 2009 study.\r\n\r\nOther studies have also shown improvement in GERD symptoms. A 2021 study published in the journal BMC Gastroenterology tested various ways to improve sleep quality in people with functional dyspepsia (aka indigestion) and included people with GERD. Their hope was to improve participants\' overall quality of life by using sleep aids to improve sleep quality. The type of insomnia the participants experienced determined which of the three different sleep aids they received—one of them being Ambien. Study results showed that sleep aids not only reduced sleep disturbance, they also helped reduce GI symptoms, including reflux.\r\n\r\nAnd a 2021 review of the literature that looked at several studies regarding GERD and sleep disturbance determined that \"treatment directed towards GERD can improve sleep experience, and treatment directed to improve sleep can improve GERD symptoms.\"\r\n\r\nSo since the 2009 study, several other studies have shown opposite results. What do these conflicting results mean?\r\n\r\n\"It means that in patients with GERD who have sleep issues, their management needs to be addressed in a heightened way if they are in need of these types of sleep aids,\" said Philip O Katz, MD, Director of Motility Laboratories for the Division of Gastroenterology at the Jay Monahan Center for Gastrointestinal Health at Weill Cornell Medicine.\r\n\r\nHow Can You Limit Acid Reflux at Night?\r\nIf you experience nighttime reflux, talk to your healthcare provider about your symptoms. Are you having trouble sleeping too? They may want to start you on medication for the reflux or insomnia—or adjust the ones you\'re already on. Elevating the head of your bed four to six inches can help with nighttime reflux as well. Experts also recommend:\r\n\r\nAvoiding alcohol and spicy, fatty, or acidic foods that trigger heartburn\r\nEating smaller meals\r\nNot eating close to bedtime\r\nLosing weight if needed\r\nWearing loose-fitting clothes\r\nWhile studies are mixed in their results, more of them do seem to point to sleep aids being helpful in both helping you sleep better and reducing the symptoms of GERD. Like anything, though, pay attention to your body and work with your healthcare provider to figure out what works best for you.','blog_images/009d60c09c4ab39c98d861e5680c1c2b.webp','',1,'2024-12-04 05:25:29.993618','2024-12-04 05:32:10.593091'),(7,'You know  Wearing a Face Mask Reduce Oxygen—and Can It Increase CO2 Levels?','With the Centers for Disease Control and Prevention (CDC) recommendation to wear a face mask to help prevent the spread of COVID-19, some people felt that wearing a mask reduced their intake of oxygen—or forced them to breathe in their own carbon dioxide. This left them feeling faint, light-headed, or \"smothered.\" They were also concerned about how dangerous this might be, and how less oxygen and more carbon dioxide might affect their health.\r\n\r\nOne driver who crashed his SUV into a pole in Lincoln Park, New Jersey, on April 23, 2020, actually blamed his collision on his mask. He told police he passed out because he\'d been wearing an N95 mask for too long. Initially, the investigating officers believed him, writing in a Facebook post that he was the only person in the car and passed out due to \"insufficient oxygen intake/excessive carbon dioxide intake.\"\r\n\r\nThe post was shared more than 2,700 times and received hundreds of comments, with a few sharing their own experiences of feeling smothered by this type of mask. The police department later updated their post, stating that they didn\'t know \"with 100% certainty\" that \"excessive wearing\" of an N95 mask was a contributing factor to the accident. They added that \"it is certainly possible that some other medical reason could\'ve contributed to the driver passing out.\"\r\n\r\n 18 Places Where You Can Still Buy Face Masks\r\nSo is it possible that wearing a face mask to prevent the spread of COVID-19 could cause someone to build up so much carbon dioxide and get so little oxygen that they pass out—or worse? Carbon dioxide is a natural by-product of the body\'s respiration process, something we all breathe in and out every day. How harmful can it be?\r\n\r\nIn rare cases, it can actually be pretty dangerous, according to the National Institutes of Health (NIH). They say that inhaling high levels of carbon dioxide (CO2) may be life-threatening. Hypercapnia (carbon dioxide toxicity) can also cause headache, vertigo, double vision, inability to concentrate, tinnitus (hearing a noise, like a ringing or buzzing, that\'s not caused by an outside source), seizures, or suffocation due to displacement of air.\r\n\r\nBut the emphasis here should be on high levels. \"It has to be a pretty high concentration to be capable of causing harm,\" Bill Carroll, PhD, an adjunct professor of chemistry at Indiana University, Bloomington, told Health. \"CO2 is present in the atmosphere at a level of about 0.04%. It is dangerous in an atmosphere when it is greater than about 10%.\"\r\n\r\nIt\'s also possible to have too little CO2. \"This is when you exhale too fast or too often,\" said Carroll. \"If you hold your breath, you wind up with too much CO2. The core issue is that CO2 regulates the pH of the blood—too much CO2 and the blood becomes too acidic; too little and it becomes too basic (alkaline). In either case, your body detects the change in acidity and you pass out, which is the body\'s way of saying, \'please stop fooling with me and breathe normally.\'\"\r\n\r\n What Is the Best Material for a Reusable Face Mask? Here\'s What an Expert Says\r\nWhen it comes to face masks, we know they\'re not all made equally. The extent to which a mask could affect CO2 levels depends on what it\'s made of and how tightly it fits.\r\n\r\n\"If you put a plastic bag over your head and tie it tight around your neck, no coronavirus could get in, but neither could any oxygen and you would suffocate, so we obviously don\'t recommend that,\" said Carroll. \"I think it\'s highly unlikely that you would pass out from a lack of oxygen with a cloth mask, which generally doesn\'t fit tightly to your face. When you exhale or inhale, air can go around the mask as well through the pores in the material. This is why a cloth mask does not absolutely protect you from inhaling the virus, but by disturbing your exhalation flow it tends to protect those around you from aerosols in your breath.\"\r\n\r\nCarroll doubted that any cloth face covering would ever fit against the face so tight that someone would pass out from a lack of oxygen. \"You\'d take it off because it\'s uncomfortable well before that happens,\" he said.\r\n\r\nBut what about the guy in the New Jersey car crash? After all, he was wearing an N95 mask, not just a regular cloth mask.\r\n\r\n\"Someone wearing an N95 mask for a prolonged period of time may have alterations in their blood chemistry that could lead to changes in level of consciousness if severe,\" infectious disease expert Amesh A. Adalja, MD, senior scholar at the Johns Hopkins Center for Health Security in Maryland, told Health. But it\'s most likely to happen to those already predisposed to breathing difficulties, such as smokers, obese people, or individuals with COPD or emphysema.\r\n\r\n If Your Face Mask Hurts Your Ears, Try These Genius Hacks to Prevent Irritation\r\nKelli Randell, MD, an internist and medical advisor at Aeroflow Healthcare, told Health that prolonged use of any face mask, including the N95 respirator, has not been shown to cause carbon dioxide toxicity in healthy people. \"Because breathing is slightly harder with a mask, I do recommend that people who suffer from severe COPD or other lung diseases that make breathing difficult carefully consider the use of face masks,\" said Dr. Randell.\r\n\r\nDr. Adalja added that the N95 respirator is a type of personal protective equipment (PPE) designed to protect health care workers and the patients they care for. \"It\'s uncomfortable to wear, and it does restrict your breathing,\" said Dr. Adalja. \"When I wear one to take care of patients I try to keep it on only for as long as I have to.\"\r\n\r\nThe bottom line? The CDC recommends you \"wear a mask with the best fit, protection, and comfort for you.\" The agency also provides guidelines to help you decide when to wear a mask and what type to consider—like if you\'re sick and have to be around other people or if you\'re caring for someone who\'s ill (in which case, they state that a respirator will provide the most protection). If you feel like your airways are cut off while wearing a mask, consider other possible causes, such as a panic attack, which can trigger sudden feelings of suffocation and breathlessness.\r\n\r\nThe information in this story is accurate as of press time. However, as the situation surrounding COVID-19 continues to evolve, it\'s possible that some data have changed since publication. While Health is trying to keep our stories as up-to-date as possible, we also encourage readers to stay informed on news and recommendations for their own communities by using the CDC, WHO, and their local public health department as resources.\r\n\r\nTo get our top stories delivered to your inbox, sign up for the Healthy Living newsletter','blog_images/0a3b3e2c1d40cb8a44a651d9b576edd6.webp','',1,'2024-12-04 05:33:03.605223','2024-12-04 05:33:03.605223'),(8,'The Role of Hydration in Your Health and Wellness','Water is the elixir of life, and its significance cannot be overstated. Hydration is fundamental to maintaining optimal health and wellness. It plays a pivotal role in nearly every bodily function, from regulating body temperature to supporting digestion and cognitive function. In this blog, we will delve into the multifaceted role of hydration in your overall well-being and explore some unique aspects of how staying adequately hydrated can impact your life.\r\n\r\nChapter 1: The Body\'s H2O Balance\r\n\r\nWater is the primary component of the human body, constituting approximately 60% of an adult\'s body weight. This fact alone underscores its importance. Maintaining the delicate balance of water in the body is essential for several reasons.\r\n\r\n1.1 Temperature Regulation\r\n\r\nOne of the most critical functions of water is to regulate body temperature. When you exercise or encounter high temperatures, your body sweats to cool down. Sweating releases heat as moisture evaporates from your skin\'s surface, helping to maintain your core temperature within a safe range.\r\n\r\n1.2 Digestion and Nutrient Absorption\r\n\r\nHydration is vital for digestion and the absorption of nutrients. Water assists in breaking down food in the stomach, facilitating the movement of nutrients through the digestive tract. It also helps prevent constipation by keeping the stool soft and easy to pass.','blog_images/3ab7b42d7988ec9f60e5937192ebdf3c.jpg','',1,'2024-12-04 05:33:52.044399','2024-12-04 05:33:52.044399');
/*!40000 ALTER TABLE `blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clinic_category`
--

DROP TABLE IF EXISTS `clinic_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clinic_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinic_category`
--

LOCK TABLES `clinic_category` WRITE;
/*!40000 ALTER TABLE `clinic_category` DISABLE KEYS */;
INSERT INTO `clinic_category` VALUES (2,'test clinic cat',1,'2024-11-23 11:27:09.140303','2024-11-23 11:28:12.668268'),(3,'Vet care',1,'2024-11-23 11:35:54.543891','2024-11-23 11:35:54.543891');
/*!40000 ALTER TABLE `clinic_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_insurances`
--

DROP TABLE IF EXISTS `customer_insurances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_insurances` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `insurance_company_id` int DEFAULT NULL,
  `insurance_company_name` varchar(255) DEFAULT NULL,
  `insurance_type` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_insurances_customer_id_c421d898_fk_customers_id` (`customer_id`),
  CONSTRAINT `customer_insurances_customer_id_c421d898_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_insurances`
--

LOCK TABLES `customer_insurances` WRITE;
/*!40000 ALTER TABLE `customer_insurances` DISABLE KEYS */;
INSERT INTO `customer_insurances` VALUES (4,1,'Star Health Insurance','Health Insurance','2024-12-05','2024-12-30','2024-12-05 10:53:56.934306','2024-12-05 10:53:56.934306',2);
/*!40000 ALTER TABLE `customer_insurances` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_wallet_histories`
--

DROP TABLE IF EXISTS `customer_wallet_histories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_wallet_histories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `transaction_type` varchar(20) NOT NULL,
  `amount` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  `transaction_type_choices` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_wallet_histories_customer_id_9b135c69_fk_customers_id` (`customer_id`),
  CONSTRAINT `customer_wallet_histories_customer_id_9b135c69_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_wallet_histories`
--

LOCK TABLES `customer_wallet_histories` WRITE;
/*!40000 ALTER TABLE `customer_wallet_histories` DISABLE KEYS */;
INSERT INTO `customer_wallet_histories` VALUES (1,'Customer added amount','credit',100,'2024-12-11 12:12:07.927503','2024-12-11 12:12:07.927503',2,'customer added amount'),(2,'Customer added amount','credit',100,'2024-12-11 12:23:27.280995','2024-12-11 12:23:27.280995',2,'customer added amount'),(3,'Sed soluta voluptatu','debit',100,'2024-12-15 10:50:31.942129','2024-12-15 10:50:31.942129',2,'deducted amount'),(4,'testing\r\n','credit',500,'2024-12-15 10:51:37.791052','2024-12-15 10:51:37.791052',2,'refund amount');
/*!40000 ALTER TABLE `customer_wallet_histories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `pre_existing_disease` longtext,
  `blood_group` varchar(10) DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `wallet` double NOT NULL,
  `overall_ratings` double NOT NULL,
  `no_of_ratings` int NOT NULL,
  `status` int NOT NULL,
  `dob` date DEFAULT NULL,
  `age` double DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `weight` varchar(20) DEFAULT NULL,
  `emergency_contact_no` varchar(255) DEFAULT NULL,
  `allergies` varchar(255) DEFAULT NULL,
  `current_medications` varchar(255) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `phone_number` (`phone_number`),
  CONSTRAINT `customers_user_id_28f6c6eb_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (2,'Umesh Prajapati','9887939268','customers/profiles/geriatric_services.png',NULL,'AB+','M',200,0,0,1,'1997-01-31',NULL,'6','80',NULL,NULL,NULL,28);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_all_users_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (14,'accounts','admin'),(13,'accounts','customer'),(12,'accounts','doctordetails'),(9,'accounts','hospital'),(11,'accounts','hospitalimage'),(10,'accounts','laboratory'),(8,'accounts','user'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'authtoken','token'),(7,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(48,'H2H_admin','address'),(43,'H2H_admin','allergy'),(33,'H2H_admin','appmodule'),(35,'H2H_admin','banner'),(16,'H2H_admin','bed'),(38,'H2H_admin','bedbooking'),(17,'H2H_admin','bedstatus'),(39,'H2H_admin','blog'),(24,'H2H_admin','cliniccategory'),(46,'H2H_admin','customerinsurance'),(49,'H2H_admin','customerwallethistory'),(26,'H2H_admin','doctorbanner'),(50,'H2H_admin','doctorbooking'),(25,'H2H_admin','doctorclinics'),(37,'H2H_admin','experttalk'),(47,'H2H_admin','familymember'),(52,'H2H_admin','fcmnotification'),(45,'H2H_admin','feedback'),(40,'H2H_admin','helpdeskquery'),(19,'H2H_admin','hospitaldepartment'),(23,'H2H_admin','hospitaldoctors'),(20,'H2H_admin','hospitalfacility'),(18,'H2H_admin','hospitalservice'),(29,'H2H_admin','labbanner'),(54,'H2H_admin','laborderitems'),(53,'H2H_admin','laborders'),(31,'H2H_admin','labpackage'),(30,'H2H_admin','labservice'),(32,'H2H_admin','labstaff'),(27,'H2H_admin','labtag'),(44,'H2H_admin','medication'),(36,'H2H_admin','modulebanner'),(34,'H2H_admin','moduleofferbanner'),(51,'H2H_admin','notification'),(42,'H2H_admin','reminder'),(41,'H2H_admin','remindercategory'),(28,'H2H_admin','service'),(21,'H2H_admin','specialistcategory'),(22,'H2H_admin','symptom'),(15,'H2H_admin','ward'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-18 12:13:16.799825'),(2,'contenttypes','0002_remove_content_type_name','2024-11-18 12:13:16.972236'),(3,'auth','0001_initial','2024-11-18 12:13:17.538791'),(4,'auth','0002_alter_permission_name_max_length','2024-11-18 12:13:17.674000'),(5,'auth','0003_alter_user_email_max_length','2024-11-18 12:13:17.687992'),(6,'auth','0004_alter_user_username_opts','2024-11-18 12:13:17.700833'),(7,'auth','0005_alter_user_last_login_null','2024-11-18 12:13:17.713309'),(8,'auth','0006_require_contenttypes_0002','2024-11-18 12:13:17.721320'),(9,'auth','0007_alter_validators_add_error_messages','2024-11-18 12:13:17.738295'),(10,'auth','0008_alter_user_username_max_length','2024-11-18 12:13:17.753418'),(11,'auth','0009_alter_user_last_name_max_length','2024-11-18 12:13:17.767925'),(12,'auth','0010_alter_group_name_max_length','2024-11-18 12:13:17.809900'),(13,'auth','0011_update_proxy_permissions','2024-11-18 12:13:17.829888'),(14,'auth','0012_alter_user_first_name_max_length','2024-11-18 12:13:17.845881'),(15,'accounts','0001_initial','2024-11-18 12:13:19.796010'),(16,'admin','0001_initial','2024-11-18 12:13:20.071847'),(17,'admin','0002_logentry_remove_auto_add','2024-11-18 12:13:20.100833'),(18,'admin','0003_logentry_add_action_flag_choices','2024-11-18 12:13:20.139100'),(19,'authtoken','0001_initial','2024-11-18 12:13:20.321487'),(20,'authtoken','0002_auto_20160226_1747','2024-11-18 12:13:20.436419'),(21,'authtoken','0003_tokenproxy','2024-11-18 12:13:20.445169'),(22,'authtoken','0004_alter_tokenproxy_options','2024-11-18 12:13:20.456017'),(23,'sessions','0001_initial','2024-11-18 12:13:20.534410'),(24,'accounts','0002_remove_customer_email_remove_doctordetails_email_and_more','2024-11-18 13:02:00.779517'),(25,'accounts','0003_hospital_city','2024-11-19 07:14:27.151550'),(26,'H2H_admin','0001_initial','2024-11-19 10:01:48.871958'),(27,'accounts','0004_alter_hospitalimage_table','2024-11-19 10:58:19.953169'),(28,'H2H_admin','0002_alter_ward_table_bed','2024-11-19 10:58:20.481751'),(29,'H2H_admin','0003_bedstatus','2024-11-19 11:41:10.085549'),(30,'H2H_admin','0004_hospitalservice','2024-11-19 12:17:33.133690'),(31,'H2H_admin','0005_alter_hospitalservice_table','2024-11-19 12:33:28.740240'),(32,'H2H_admin','0006_hospitaldepartment','2024-11-19 12:58:12.897549'),(33,'H2H_admin','0007_hospitalfacility','2024-11-19 13:23:29.005331'),(34,'H2H_admin','0008_specialistcategory','2024-11-20 05:32:42.071643'),(35,'H2H_admin','0009_symptom','2024-11-20 06:11:17.653949'),(36,'accounts','0005_doctordetails_specialist','2024-11-20 07:17:46.180397'),(37,'accounts','0006_doctordetails_join_date','2024-11-20 07:35:58.548132'),(38,'H2H_admin','0010_hospitaldoctors','2024-11-23 10:11:45.857404'),(39,'H2H_admin','0011_cliniccategory','2024-11-23 11:12:39.903707'),(40,'H2H_admin','0012_alter_cliniccategory_status','2024-11-23 11:19:12.237927'),(41,'H2H_admin','0013_doctorclinics','2024-11-23 11:43:49.664361'),(42,'H2H_admin','0014_doctorbanner','2024-11-23 12:43:54.979519'),(43,'H2H_admin','0015_labtag_service_labservice_labbanner','2024-11-25 07:19:58.122566'),(44,'H2H_admin','0016_labstaff_labpackage','2024-11-25 08:42:23.712544'),(45,'H2H_admin','0017_appmodule_offerbanner_modulebanner_banner','2024-11-27 07:58:00.660268'),(46,'H2H_admin','0018_rename_offerbanner_moduleofferbanner_and_more','2024-11-27 08:52:43.675848'),(47,'H2H_admin','0019_remove_banner_banners_and_more','2024-11-27 09:21:06.434771'),(48,'accounts','0007_remove_customer_created_at_and_more','2024-11-28 07:32:09.663327'),(49,'H2H_admin','0020_experttalk','2024-11-28 10:00:34.232934'),(50,'H2H_admin','0021_bedbooking','2024-11-30 11:18:12.608109'),(51,'H2H_admin','0022_alter_bedbooking_status','2024-11-30 12:43:36.250762'),(52,'H2H_admin','0023_alter_experttalk_doctor','2024-12-03 06:18:28.881967'),(53,'H2H_admin','0024_blog','2024-12-03 17:47:08.137339'),(54,'H2H_admin','0025_helpdeskquery','2024-12-04 07:31:48.229829'),(55,'H2H_admin','0026_remindercategory_reminder','2024-12-04 10:34:51.790877'),(56,'H2H_admin','0027_allergy','2024-12-04 11:36:03.860919'),(57,'H2H_admin','0028_medication','2024-12-04 12:02:08.962819'),(58,'H2H_admin','0029_feedback','2024-12-04 13:37:03.022817'),(59,'H2H_admin','0030_alter_reminder_status','2024-12-05 09:15:27.156664'),(60,'H2H_admin','0031_customerinsurance','2024-12-05 09:46:22.274157'),(61,'H2H_admin','0032_familymember','2024-12-05 12:26:19.780282'),(62,'H2H_admin','0033_address','2024-12-06 11:46:13.086983'),(63,'H2H_admin','0034_customerwallethistory','2024-12-11 11:12:06.836231'),(64,'H2H_admin','0035_remove_customerwallethistory_wallet_type_and_more','2024-12-11 11:23:11.552017'),(65,'H2H_admin','0036_customerwallethistory_transaction_type_choices_and_more','2024-12-11 12:18:10.020660'),(66,'H2H_admin','0037_doctorbooking','2024-12-12 10:29:01.447632'),(67,'H2H_admin','0038_alter_doctorbooking_clinic','2024-12-12 11:59:08.033639'),(68,'H2H_admin','0039_notification','2024-12-13 09:47:29.342695'),(69,'H2H_admin','0040_fcmnotification','2024-12-13 10:48:07.396791'),(73,'H2H_admin','0041_laborders_laborderitems','2024-12-14 09:05:43.293964'),(74,'H2H_admin','0042_alter_doctorbooking_status','2024-12-14 09:35:01.461064');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6alwsctcmatdcoi5vncu8muvtnj66wq4','.eJxVjssOwiAURP-FtSE8S-vSvd9ALtyL1AckpV0Z_10xXeh2zszkPJmHbc1-a7T4GdmRSXb4zQLEG5UO8ArlUnmsZV3mwHuF77Txc0W6n_bu30GGlj_rpCarAYJKEZ0CpBRt1BIoOQjaDg7lJAxaEqSlHZ0x42CCEkZTsCJ2K8DHXL6S8vUG_mQ8Lg:1tDd0W:tdEtSgY6lRWbKYHna-e_CLCwrnGDEk4O6zVQO0P1Dqs','2024-12-04 05:12:04.256940'),('7grly0c8vmysw3b22vqo6x4bhtcgyga0','.eJxVjEEOwiAQRe_C2hCgMxRcuvcMZAaoVA0kpV0Z765NutDtf-_9lwi0rSVsPS9hTuIsBiVOvyNTfOS6k3SnemsytrouM8tdkQft8tpSfl4O9--gUC_fOhoGILITokHnVaKovFIwIfMw6oEJwEawDsloUN6BRWPNmBxnbZwW7w_uiDbT:1tL0I0:t2C-M8fxy5bMU5UCzTHlSNXvvPrGmmS06NPTmMrhhDw','2024-12-24 13:28:36.515004'),('a6blnmo2hve1rdz19x0dvvwtscjjua7c','e30:1tD1qt:CubXbA3URb4MvxQqUX7hCJH9OeW-NoKMF297szs3flo','2024-12-02 13:31:39.882961'),('ab7y4565scrw4osmnf2h4vws1uutqwxq','e30:1tFYE8:EmZH6J47sgzhju5pXwESc3HIgoXxGsIgG0k7QG7eal0','2024-12-09 12:30:04.764924'),('bi1b7iodqn724l9gn79l7ejasilcshjv','.eJxVjssOwiAURP-FtSE8S-vSvd9ALtyL1AckpV0Z_10xXeh2zszkPJmHbc1-a7T4GdmRSXb4zQLEG5UO8ArlUnmsZV3mwHuF77Txc0W6n_bu30GGlj_rpCarAYJKEZ0CpBRt1BIoOQjaDg7lJAxaEqSlHZ0x42CCEkZTsCJ2K8DHXL6S8vUG_mQ8Lg:1tGvSY:kJs0KQDlWNB8SnPy9EnxtPuDrO6f2Xr4mLoAm0n6f1o','2024-12-13 07:30:38.120199'),('d4oho2z3uskns36zpwjun5k0qgurcybe','.eJxVjssOwiAURP-FtSE8S-vSvd9ALtyL1AckpV0Z_10xXeh2zszkPJmHbc1-a7T4GdmRSXb4zQLEG5UO8ArlUnmsZV3mwHuF77Txc0W6n_bu30GGlj_rpCarAYJKEZ0CpBRt1BIoOQjaDg7lJAxaEqSlHZ0x42CCEkZTsCJ2K8DHXL6S8vUG_mQ8Lg:1tKvSE:u9WwfnA03gRaF3S5jkxMygMta5K-1fvEBuastlAAiEc','2024-12-24 08:18:50.289625'),('n9awov5thpbunonp5u90zq1d7vt6j15u','.eJxVjssOwiAURP-FtSE8S-vSvd9ALtyL1AckpV0Z_10xXeh2zszkPJmHbc1-a7T4GdmRSXb4zQLEG5UO8ArlUnmsZV3mwHuF77Txc0W6n_bu30GGlj_rpCarAYJKEZ0CpBRt1BIoOQjaDg7lJAxaEqSlHZ0x42CCEkZTsCJ2K8DHXL6S8vUG_mQ8Lg:1tIVNi:U-0czuHURYA_plYfCnrhlaDatWWxsQF8Vff5iHK_zcw','2024-12-17 16:04:10.840664'),('q0iu431pg81glx7vlo40gdf29e5ec87a','e30:1tD1nY:ONtm8BEkBXbCXr0r3O0dAx6LgkjqyHZrOVPbcp2U71s','2024-12-02 13:28:12.658598'),('r0fuzjr5ihr0d2pb2n087d0fre207kbg','.eJxVjssOwiAURP-FtSE8S-vSvd9ALtyL1AckpV0Z_10xXeh2zszkPJmHbc1-a7T4GdmRSXb4zQLEG5UO8ArlUnmsZV3mwHuF77Txc0W6n_bu30GGlj_rpCarAYJKEZ0CpBRt1BIoOQjaDg7lJAxaEqSlHZ0x42CCEkZTsCJ2K8DHXL6S8vUG_mQ8Lg:1tDGGi:1SFRdH0tyu5x17EJdIOUI7OoQfUqUu7gfCRqxk8ngWE','2024-12-03 04:55:16.639102');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_bookings`
--

DROP TABLE IF EXISTS `doctor_bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_bookings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `booking_number` varchar(50) DEFAULT NULL,
  `booking_for` varchar(10) DEFAULT NULL,
  `patient_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `age` int DEFAULT NULL,
  `contact_number` varchar(255) DEFAULT NULL,
  `emergency_contact` varchar(255) DEFAULT NULL,
  `blood_group` varchar(255) NOT NULL,
  `medical_history` longtext,
  `current_symptoms` varchar(255) DEFAULT NULL,
  `booking_date` date DEFAULT NULL,
  `time_slot` time(6) DEFAULT NULL,
  `consultation_charge` decimal(10,2) DEFAULT NULL,
  `base_rate` decimal(10,2) DEFAULT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `additional_charges` decimal(10,2) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `final_total` decimal(10,2) DEFAULT NULL,
  `payment_mode` varchar(50) DEFAULT NULL,
  `notes` longtext,
  `status` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `clinic_id` bigint DEFAULT NULL,
  `customer_id` bigint NOT NULL,
  `doctor_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `doctor_bookings_customer_id_5fbe37e7_fk_customers_id` (`customer_id`),
  KEY `doctor_bookings_doctor_id_b84dff6f_fk_doctors_id` (`doctor_id`),
  KEY `doctor_bookings_clinic_id_9860378b_fk_doctor_clinics_id` (`clinic_id`),
  CONSTRAINT `doctor_bookings_clinic_id_9860378b_fk_doctor_clinics_id` FOREIGN KEY (`clinic_id`) REFERENCES `doctor_clinics` (`id`),
  CONSTRAINT `doctor_bookings_customer_id_5fbe37e7_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `doctor_bookings_doctor_id_b84dff6f_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_bookings`
--

LOCK TABLES `doctor_bookings` WRITE;
/*!40000 ALTER TABLE `doctor_bookings` DISABLE KEYS */;
INSERT INTO `doctor_bookings` VALUES (1,'DOC-933836','self','John ','john.doe@example.com',25,'123456','0987654321','AB+','testing','Fever','2024-12-15','21:44:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'online','Need to discuss chronic back pain','pending','2024-12-12 11:59:48.118024','2024-12-15 12:19:52.888970',2,2,2),(2,'DOC-905280','self','John Doe','john.doe@example.com',30,'1234567890','0987654321','O+','None','Fever','2024-08-05','13:00:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'online','Need to discuss chronic back pain','cancelled','2024-12-12 12:00:33.685441','2024-12-14 12:27:35.423626',2,2,3),(3,'DOC-483600','self','John Doe','john.doe@example.com',30,'1234567890','0987654321','O+','None','Fever','2024-08-05','13:00:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'online','Need to discuss chronic back pain','pending','2024-12-12 12:01:03.854890','2024-12-12 12:01:03.854890',3,2,3),(4,'DOC-759054','self','umesh prajapati','john.doe@example.com',30,'1234567890','0987654321','O+','None','Fever','2024-12-15','13:00:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'online','Need to discuss chronic back pain','pending','2024-12-12 12:01:59.385824','2024-12-12 12:01:59.385824',3,2,3),(5,'DOC-347813','self','umesh prajapati','umesh@gmail.com',30,'1234567890','0987654321','O+','None','Fever','2024-12-15','13:00:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'online','Need to discuss chronic back pain','pending','2024-12-12 12:02:13.726271','2024-12-12 12:02:13.726271',3,2,3),(6,'DOC-476027','self','umesh prajapati','umesh@gmail.com',30,'9993324010','7894001500','AB+','None','Fever','2024-12-15','13:00:00.000000',400.00,400.00,0.00,0.00,0.00,400.00,400.00,'cash','Need to discuss chronic back pain','pending','2024-12-12 12:02:58.357990','2024-12-12 12:02:58.357990',3,2,3);
/*!40000 ALTER TABLE `doctor_bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_clinics`
--

DROP TABLE IF EXISTS `doctor_clinics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_clinics` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `clinic_name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `consultation_minutes` varchar(10) NOT NULL,
  `start_time` time(6) DEFAULT NULL,
  `end_time` time(6) DEFAULT NULL,
  `status` int NOT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `clinic_category_id` bigint DEFAULT NULL,
  `doctor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `doctor_clinics_clinic_category_id_2f2626f4_fk_clinic_category_id` (`clinic_category_id`),
  KEY `doctor_clinics_doctor_id_8481e11b_fk_doctors_id` (`doctor_id`),
  CONSTRAINT `doctor_clinics_clinic_category_id_2f2626f4_fk_clinic_category_id` FOREIGN KEY (`clinic_category_id`) REFERENCES `clinic_category` (`id`),
  CONSTRAINT `doctor_clinics_doctor_id_8481e11b_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_clinics`
--

LOCK TABLES `doctor_clinics` WRITE;
/*!40000 ALTER TABLE `doctor_clinics` DISABLE KEYS */;
INSERT INTO `doctor_clinics` VALUES (2,'Vivian','8756301200','diparydere@mailinator.com','Quasi','20','08:00:00.000000','17:00:00.000000',1,22.7196,75.860681,'2024-11-23 12:30:21.434205','2024-12-03 07:19:04.454335',3,2),(3,'Gisela Mcneil','8521001020','lyvofo@mailinator.com','Eos corporis id vol','30','11:05:00.000000','18:00:00.000000',1,22.719063481859006,75.85483447322031,'2024-11-23 12:33:28.478340','2024-12-03 07:20:17.818971',2,3);
/*!40000 ALTER TABLE `doctor_clinics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dr_name` varchar(255) NOT NULL,
  `dr_unique_code` varchar(50) NOT NULL,
  `qualification` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `experience` int unsigned NOT NULL,
  `profile_status` varchar(1) NOT NULL,
  `consultation_fee` decimal(10,2) NOT NULL,
  `profile_img` varchar(100) DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  `sub_specialist` varchar(100) DEFAULT NULL,
  `additional_qualification` longtext,
  `rating` decimal(3,2) NOT NULL,
  `overall_ratings` double NOT NULL,
  `document_update_status` int NOT NULL,
  `document_approve_status` varchar(1) NOT NULL,
  `online_status` varchar(1) NOT NULL,
  `medical_license` varchar(100) NOT NULL,
  `institution` varchar(255) NOT NULL,
  `graduation_year` int unsigned NOT NULL,
  `dob` date NOT NULL,
  `wallet` double NOT NULL,
  `earnings` double NOT NULL,
  `description` longtext,
  `is_recommended` varchar(1) NOT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `medical_license_doc` varchar(100) DEFAULT NULL,
  `certification` varchar(100) DEFAULT NULL,
  `other` varchar(100) DEFAULT NULL,
  `hospital_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `specialist_id` bigint DEFAULT NULL,
  `join_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dr_unique_code` (`dr_unique_code`),
  UNIQUE KEY `medical_license` (`medical_license`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `doctors_hospital_id_96f18c1c_fk_hospitals_id` (`hospital_id`),
  KEY `doctors_specialist_id_6ffc57e2_fk_specialist_categories_id` (`specialist_id`),
  CONSTRAINT `doctors_hospital_id_96f18c1c_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`),
  CONSTRAINT `doctors_specialist_id_6ffc57e2_fk_specialist_categories_id` FOREIGN KEY (`specialist_id`) REFERENCES `specialist_categories` (`id`),
  CONSTRAINT `doctors_user_id_480f6e79_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`),
  CONSTRAINT `doctors_chk_1` CHECK ((`experience` >= 0)),
  CONSTRAINT `doctors_chk_2` CHECK ((`graduation_year` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (2,'Ora ','Dr28073','Neque ex ','7845123266','F',3,'P',80.00,'doctors/doctor_profiles/Dr._Aisha_Khan.jpg','1',NULL,'Ex in ',0.00,0,0,'P','F','MP0','Ut am',2001,'2003-06-17',0,0,'Id dolor magna ut du','Y','doctors/doctor_documents/Dr.Mohit_Bhandari.png','doctors/doctor_documents/ankur.jpg','doctors/doctor_documents/Dr.Mohit_Bhandari_ibLzzt5.png','doctors/doctor_documents/Dr._Aisha_Khan.jpg',NULL,8,3,'2004-11-18 18:30:00.000000'),(3,'Myles Bradley','Dr60824','Laborum mollitia dol','9630410852','F',3,'P',20.00,'doctors/doctor_profiles/Dr._Aisha_Khan_vhA0PiW.jpg','1',NULL,'Ea ut in in velit cu',0.00,0,0,'P','F','676','Repudiandae sunt ex',1984,'1976-08-02',0,0,'Debitis id praesenti','Y','doctors/doctor_documents/rs-new-logo.webp','doctors/doctor_documents/star-health-logo_JDSlxhY.webp','doctors/doctor_documents/logo-min_UpRd8AZ.webp','doctors/doctor_documents/HDFC_logo_ky8qqOD.webp',NULL,10,5,'1980-02-12 18:30:00.000000');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dr_banners`
--

DROP TABLE IF EXISTS `dr_banners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dr_banners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `link` varchar(255) DEFAULT NULL,
  `banner` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `doctor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dr_banners_doctor_id_1b792aad_fk_doctors_id` (`doctor_id`),
  CONSTRAINT `dr_banners_doctor_id_1b792aad_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dr_banners`
--

LOCK TABLES `dr_banners` WRITE;
/*!40000 ALTER TABLE `dr_banners` DISABLE KEYS */;
INSERT INTO `dr_banners` VALUES (1,'https://www.niriwapojo.co','doctors/banners/worker-avatar-icon-orange-worker.png','T',1,'2024-11-23 12:59:54.088373','2024-11-23 13:02:56.901467',3),(3,'','doctors/banners/outpatient_services.png','B',1,'2024-12-03 07:44:33.932736','2024-12-03 07:44:33.932736',2),(4,'','doctors/banners/cardiology_services.png','T',1,'2024-12-03 07:44:49.847874','2024-12-03 07:44:49.847874',2),(5,'','doctors/banners/geriatric_services.png','B',1,'2024-12-03 07:45:20.827776','2024-12-03 07:45:20.827776',3);
/*!40000 ALTER TABLE `dr_banners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expert_talks`
--

DROP TABLE IF EXISTS `expert_talks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expert_talks` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `doctor_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `expert_talks_doctor_id_a893ad2a_fk_doctors_id` (`doctor_id`),
  CONSTRAINT `expert_talks_doctor_id_a893ad2a_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expert_talks`
--

LOCK TABLES `expert_talks` WRITE;
/*!40000 ALTER TABLE `expert_talks` DISABLE KEYS */;
INSERT INTO `expert_talks` VALUES (3,'Nihil quia irure ut ','2024-11-28 10:46:11.279147','2024-12-03 06:19:41.952903',2),(4,'Doloribus repellendu','2024-11-28 10:46:17.207909','2024-11-28 10:46:17.207909',3);
/*!40000 ALTER TABLE `expert_talks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family_members`
--

DROP TABLE IF EXISTS `family_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family_members` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `age` int DEFAULT NULL,
  `relation` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile_no` varchar(15) DEFAULT NULL,
  `is_minor` tinyint(1) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `blood_group` varchar(20) DEFAULT NULL,
  `medical_history` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `family_members_customer_id_f0f4201d_fk_customers_id` (`customer_id`),
  CONSTRAINT `family_members_customer_id_f0f4201d_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family_members`
--

LOCK TABLES `family_members` WRITE;
/*!40000 ALTER TABLE `family_members` DISABLE KEYS */;
INSERT INTO `family_members` VALUES (1,'umesh','prajapati','1999-07-20',NULL,'son','umesh@gmail.com','9157672460',0,'M','AB+','','2024-12-05 13:07:07.151417','2024-12-05 13:28:46.950344',2);
/*!40000 ALTER TABLE `family_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fcm_notifications`
--

DROP TABLE IF EXISTS `fcm_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fcm_notifications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slug` varchar(50) NOT NULL,
  `customer_title` varchar(100) NOT NULL,
  `customer_description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fcm_notifications`
--

LOCK TABLES `fcm_notifications` WRITE;
/*!40000 ALTER TABLE `fcm_notifications` DISABLE KEYS */;
INSERT INTO `fcm_notifications` VALUES (1,'bed_booking_confirmed','Booking Confirmed','Your bed booking has been confirmed.','2024-12-13 12:57:48.262650','2024-12-13 12:57:48.262650'),(2,'bed_booking_cancelled','Booking Cancelled','Your bed booking has been cancelled.','2024-12-13 12:59:11.603090','2024-12-13 13:24:59.462634'),(22,'bed_booking_checked_in','Checked In','You have successfully checked in.','2024-12-13 13:01:10.433032','2024-12-13 13:01:10.433032'),(23,'bed_booking_checked_out','Checked Out','You have successfully checked out.','2024-12-13 13:01:44.824400','2024-12-13 13:01:44.824400'),(24,'bed_booking_no_show','No Show','You did not show up for your bed booking.','2024-12-13 13:02:19.728601','2024-12-13 13:02:19.728601'),(25,'bed_booking_in_progress','Booking In Progress','Your patient treatment is in progress.','2024-12-13 13:02:43.774771','2024-12-13 13:02:43.774771'),(26,'bed_booking_completed','Booking Completed','Your bed booking has been completed.','2024-12-13 13:03:11.442028','2024-12-13 13:03:11.442028'),(27,'lab_booking_success','Booking Success','Your lab test has been booked successfully.','2024-12-13 13:04:01.186596','2024-12-13 13:04:01.186596'),(28,'lab_booking_confirmed','Booking Confirmed','Your lab test booking has been confirmed.','2024-12-13 13:04:30.264607','2024-12-13 13:04:30.265607'),(29,'lab_booking_cancelled','Booking Cancelled','Your lab test booking has been cancelled.','2024-12-13 13:04:59.974552','2024-12-13 13:04:59.974552'),(30,'lab_booking_completed','Booking Completed','Your lab test booking has been completed.','2024-12-13 13:05:33.919269','2024-12-13 13:05:33.919346'),(31,'lab_booking_pending','Booking Pending','Your lab test booking is pending confirmation.','2024-12-13 13:06:03.439575','2024-12-13 13:06:03.439575'),(32,'lab_booking_order_placed','Order Placed','Your lab test order was successfully placed.','2024-12-13 13:06:29.341217','2024-12-13 13:06:29.341217'),(33,'lab_booking_collective_person_assigned','Collective Person Assigned','Collective Person Assigned','2024-12-13 13:07:32.480206','2024-12-13 13:07:32.480206'),(34,'lab_booking_on_progress','On Progress','Your sample was collected, your order is in progress.','2024-12-13 13:08:01.545003','2024-12-13 13:08:01.545003'),(35,'lab_booking_report_ready_to_dispatch','Report Ready To Dispatch','Your report is ready to dispatch.','2024-12-13 13:08:29.146237','2024-12-13 13:08:29.146237'),(36,'lab_booking_cancelled_by_customer','Cancelled By Customer','Your order was cancelled by the customer.','2024-12-13 13:09:27.825973','2024-12-13 13:09:27.825973'),(37,'lab_booking_cancelled_by_laboratory','Cancelled By Laboratory','Your order was cancelled by the laboratory.','2024-12-13 13:10:08.414937','2024-12-13 13:10:08.414937'),(38,'rewards','Reward Earned','You have earned {points} cashback points! Thank you for booking with us.','2024-12-13 13:10:41.099781','2024-12-13 13:10:41.099781');
/*!40000 ALTER TABLE `fcm_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `rating` double DEFAULT NULL,
  `admin_approved` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  `doctor_id` bigint DEFAULT NULL,
  `hospital_id` bigint DEFAULT NULL,
  `lab_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_customer_id_a1653a67_fk_customers_id` (`customer_id`),
  KEY `feedback_doctor_id_e2060f22_fk_doctors_id` (`doctor_id`),
  KEY `feedback_hospital_id_c0e203a8_fk_hospitals_id` (`hospital_id`),
  KEY `feedback_lab_id_63d10d2a_fk_laboratories_id` (`lab_id`),
  CONSTRAINT `feedback_customer_id_a1653a67_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `feedback_doctor_id_e2060f22_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  CONSTRAINT `feedback_hospital_id_c0e203a8_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`),
  CONSTRAINT `feedback_lab_id_63d10d2a_fk_laboratories_id` FOREIGN KEY (`lab_id`) REFERENCES `laboratories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,'Umesh',5,1,'2024-12-04 17:40:00.731515','2024-12-14 05:30:14.136676',2,2,NULL,NULL);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `help_desk_queries`
--

DROP TABLE IF EXISTS `help_desk_queries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `help_desk_queries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `help_desk_queries_customer_id_e2a7b22d_fk_customers_id` (`customer_id`),
  CONSTRAINT `help_desk_queries_customer_id_e2a7b22d_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help_desk_queries`
--

LOCK TABLES `help_desk_queries` WRITE;
/*!40000 ALTER TABLE `help_desk_queries` DISABLE KEYS */;
INSERT INTO `help_desk_queries` VALUES (3,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 08:17:02.888735','2024-12-04 08:17:02.889735',NULL),(5,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 08:18:55.060518','2024-12-04 08:18:55.060518',NULL),(6,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 08:24:50.767141','2024-12-04 08:24:50.768146',NULL),(7,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:08:26.923152','2024-12-04 09:08:26.923152',NULL),(8,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:13:11.632411','2024-12-04 09:13:11.632411',NULL),(9,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:27:04.412142','2024-12-04 09:27:04.412142',NULL),(10,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:27:23.872742','2024-12-04 09:27:23.872742',NULL),(11,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:27:47.070394','2024-12-04 09:27:47.070394',NULL),(12,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:30:48.621518','2024-12-04 09:30:48.622517',NULL),(13,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:42:47.314031','2024-12-04 09:42:47.314031',NULL),(14,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:46:04.162629','2024-12-04 09:46:04.163630',NULL),(15,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:46:49.345892','2024-12-04 09:46:49.345892',NULL),(16,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:47:23.294893','2024-12-04 09:47:23.294893',NULL),(17,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:49:38.892205','2024-12-04 09:49:38.892205',NULL),(19,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:52:12.157675','2024-12-04 09:52:12.157675',NULL),(20,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:53:11.757395','2024-12-04 09:53:11.757395',NULL),(21,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:53:28.475475','2024-12-04 09:53:28.475475',NULL),(23,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:54:23.565013','2024-12-04 09:54:23.565013',NULL),(24,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 09:58:29.229820','2024-12-04 09:58:29.229820',2),(25,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 10:02:06.977777','2024-12-04 10:02:06.977777',NULL),(26,'umesh prajapati','umesh@gmail.com','i have issue in booking.','2024-12-04 10:02:22.541267','2024-12-04 10:02:22.541267',2);
/*!40000 ALTER TABLE `help_desk_queries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_department`
--

DROP TABLE IF EXISTS `hospital_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `department_name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_department_hospital_id_e5830e0a_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `hospital_department_hospital_id_e5830e0a_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_department`
--

LOCK TABLES `hospital_department` WRITE;
/*!40000 ALTER TABLE `hospital_department` DISABLE KEYS */;
INSERT INTO `hospital_department` VALUES (3,'hospital/department_images/cardiology.png','Cardiology','CardiologyCardiologyCardiologyCardiologyCardiology','2024-11-19 13:14:40.631649','2024-11-19 13:20:25.881279',4),(4,'hospital/department_images/neurology.png','Neurology','NeurologyNeurologyNeurologyNeurologyNeurologyNeurologyNeurologyNeurologyNeurologyNeurology','2024-11-19 13:15:02.866762','2024-11-19 13:15:02.866762',4);
/*!40000 ALTER TABLE `hospital_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_doctors`
--

DROP TABLE IF EXISTS `hospital_doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_doctors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `unique_code` varchar(100) NOT NULL,
  `join_date` date NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `doctor_id` bigint DEFAULT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_doctors_doctor_id_65f9f8cc_fk_doctors_id` (`doctor_id`),
  KEY `hospital_doctors_hospital_id_55eb4b87_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `hospital_doctors_doctor_id_65f9f8cc_fk_doctors_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`id`),
  CONSTRAINT `hospital_doctors_hospital_id_55eb4b87_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_doctors`
--

LOCK TABLES `hospital_doctors` WRITE;
/*!40000 ALTER TABLE `hospital_doctors` DISABLE KEYS */;
INSERT INTO `hospital_doctors` VALUES (2,'Dr60824','2024-11-23',1,'2024-11-23 10:44:01.613310','2024-11-23 10:48:42.222988',3,3);
/*!40000 ALTER TABLE `hospital_doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_facility`
--

DROP TABLE IF EXISTS `hospital_facility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_facility` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `icon` varchar(100) DEFAULT NULL,
  `facility` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hospital_facility_hospital_id_9d76b251_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `hospital_facility_hospital_id_9d76b251_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_facility`
--

LOCK TABLES `hospital_facility` WRITE;
/*!40000 ALTER TABLE `hospital_facility` DISABLE KEYS */;
INSERT INTO `hospital_facility` VALUES (3,'hospital/facility_icons/dermatology.png','Diagnostic Imaging','2024-11-20 05:24:58.257444','2024-11-30 10:36:16.089031',3);
/*!40000 ALTER TABLE `hospital_facility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_images`
--

DROP TABLE IF EXISTS `hospital_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `hospital_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_hospitalimage_hospital_id_c1c01bf3_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `accounts_hospitalimage_hospital_id_c1c01bf3_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_images`
--

LOCK TABLES `hospital_images` WRITE;
/*!40000 ALTER TABLE `hospital_images` DISABLE KEYS */;
INSERT INTO `hospital_images` VALUES (13,'hospital/hospital_images/keiko-marsh/AF1QipMJ-DPDDc3hQexu-7GEcJTxSVJ5.webp',3),(14,'hospital/hospital_images/keiko-marsh/AF1QipNvmb_jZxEB-s6DLiCLFAI4FrHa.webp',3),(15,'hospital/hospital_images/keiko-marsh/AF1QipOBKZ3sk_rYpiUcHRcoHtGNWhPu.webp',3),(16,'hospital/hospital_images/keiko-marsh/AF1QipPFbXABufUAKyPT9fC4EBHqeu4D.webp',3),(17,'hospital/hospital_images/apollo-hospital/AF1QipN6hldEFB42cR8RcOFSz0nxqAx3.webp',4),(18,'hospital/hospital_images/apollo-hospital/AF1QipOlVkfUnpXZGhRKGuQYxxYO7PC.webp',4),(19,'hospital/hospital_images/apollo-hospital/AF1QipPBvKhQVfKwgSSwmxwttF6XRV9t.webp',4),(20,'hospital/hospital_images/apollo-hospital/AF1QipPES9iHJ4iVIulHDxCTG-qaWzI5.webp',4);
/*!40000 ALTER TABLE `hospital_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital_service`
--

DROP TABLE IF EXISTS `hospital_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital_service` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `service_name` varchar(255) NOT NULL,
  `service_icon` varchar(100) DEFAULT NULL,
  `starting_from` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `H2H_admin_hospitalservice_hospital_id_31de3ed5_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `H2H_admin_hospitalservice_hospital_id_31de3ed5_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital_service`
--

LOCK TABLES `hospital_service` WRITE;
/*!40000 ALTER TABLE `hospital_service` DISABLE KEYS */;
INSERT INTO `hospital_service` VALUES (1,'Laboratory Services','hospital/service_icons/laboratory_services.png','test','2024-11-19 12:41:49.481516','2024-11-19 12:41:49.481516',4),(3,'Cardiology Services','hospital/service_icons/cardiology_services_H0EO8qV.png','Modi ut numquam elig','2024-11-19 12:52:19.786392','2024-11-19 12:52:19.786392',3);
/*!40000 ALTER TABLE `hospital_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospitals`
--

DROP TABLE IF EXISTS `hospitals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospitals` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hospital_name` varchar(255) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `open_time` time(6) DEFAULT NULL,
  `close_time` time(6) DEFAULT NULL,
  `website_url` varchar(200) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `status` int NOT NULL,
  `is_recommended` int NOT NULL,
  `address` longtext,
  `description` longtext,
  `hospital_image` varchar(100) DEFAULT NULL,
  `hospital_logo` varchar(100) DEFAULT NULL,
  `overall_ratings` double NOT NULL,
  `no_of_ratings` int NOT NULL,
  `wallet` double NOT NULL,
  `user_id` bigint NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `hospitals_user_id_b634178f_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospitals`
--

LOCK TABLES `hospitals` WRITE;
/*!40000 ALTER TABLE `hospitals` DISABLE KEYS */;
INSERT INTO `hospitals` VALUES (3,'Bhandari Hospital And Research Center | BHRC','7869406981','22.753667734824685','75.88576786039033','22:59:00.000000','06:02:00.000000','https://www.fulojemu.org.au','hospital',1,1,'Explicabo Deserunt ','Voluptate reiciendis','hospital/hospital_images/AF1QipMJ-DPDDc3hQexu-7GEcJTxSVJ5.webp','hospital/hospital_logos/Bandari-hos-Logo_CLJQlAI.webp',0,0,0,5,'Sint incididunt ut '),(4,'Apollo Hospital','8529781030','22.731707746313205','75.8892410559233','23:20:00.000000','21:52:00.000000','https://www.tydofusylerev.cc','hospital',1,1,'Sunt occaecat offici','Similique odit et ve','hospital/hospital_images/AF1QipN6hldEFB42cR8RcOFSz0nxqAx3.webp','hospital/hospital_logos/Apollo-hos_logo.webp',0,0,0,6,'Sit omnis voluptatem');
/*!40000 ALTER TABLE `hospitals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_banners`
--

DROP TABLE IF EXISTS `lab_banners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_banners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `link` varchar(250) DEFAULT NULL,
  `banner` varchar(100) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `laboratory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_banners_laboratory_id_d364e455_fk_laboratories_id` (`laboratory_id`),
  CONSTRAINT `lab_banners_laboratory_id_d364e455_fk_laboratories_id` FOREIGN KEY (`laboratory_id`) REFERENCES `laboratories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_banners`
--

LOCK TABLES `lab_banners` WRITE;
/*!40000 ALTER TABLE `lab_banners` DISABLE KEYS */;
INSERT INTO `lab_banners` VALUES (2,'https://www.majac.com.au','laboratory/lab_banners/user-removebg-preview.png',1,'2024-11-25 08:34:59.652118','2024-11-25 08:34:59.652118',3),(3,'https://www.dopuxaxibupovew.mobi','laboratory/lab_banners/logo_hKX4bue.png',1,'2024-11-25 08:38:04.962103','2024-11-25 08:38:04.962103',3);
/*!40000 ALTER TABLE `lab_banners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_order_items`
--

DROP TABLE IF EXISTS `lab_order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_order_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` int NOT NULL,
  `item_name` varchar(150) NOT NULL,
  `price` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_order_items_order_id_ee0cc90d_fk_lab_orders_id` (`order_id`),
  CONSTRAINT `lab_order_items_order_id_ee0cc90d_fk_lab_orders_id` FOREIGN KEY (`order_id`) REFERENCES `lab_orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_order_items`
--

LOCK TABLES `lab_order_items` WRITE;
/*!40000 ALTER TABLE `lab_order_items` DISABLE KEYS */;
INSERT INTO `lab_order_items` VALUES (1,1,'MRI Test',500,'2024-12-14 09:09:44.644787','2024-12-14 09:09:44.644787',1);
/*!40000 ALTER TABLE `lab_order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_orders`
--

DROP TABLE IF EXISTS `lab_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_orders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(150) NOT NULL,
  `patient_dob` date NOT NULL,
  `patient_gender` varchar(10) NOT NULL,
  `address_id` int NOT NULL,
  `promo_id` int NOT NULL,
  `discount` double NOT NULL,
  `tax` double NOT NULL,
  `sub_total` double NOT NULL,
  `total` double NOT NULL,
  `special_instruction` varchar(250) DEFAULT NULL,
  `payment_mode` int NOT NULL,
  `booking_type` int NOT NULL,
  `items` longtext NOT NULL,
  `status` int NOT NULL,
  `created_by` int DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `appointment_time` time(6) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  `appointment_date` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  `lab_id` bigint NOT NULL,
  `lab_staff_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_orders_customer_id_460fd88a_fk_customers_id` (`customer_id`),
  KEY `lab_orders_lab_id_250d52d9_fk_laboratories_id` (`lab_id`),
  KEY `lab_orders_lab_staff_id_cc16b90d_fk_lab_staff_id` (`lab_staff_id`),
  CONSTRAINT `lab_orders_customer_id_460fd88a_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `lab_orders_lab_id_250d52d9_fk_laboratories_id` FOREIGN KEY (`lab_id`) REFERENCES `laboratories` (`id`),
  CONSTRAINT `lab_orders_lab_staff_id_cc16b90d_fk_lab_staff_id` FOREIGN KEY (`lab_staff_id`) REFERENCES `lab_staff` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_orders`
--

LOCK TABLES `lab_orders` WRITE;
/*!40000 ALTER TABLE `lab_orders` DISABLE KEYS */;
INSERT INTO `lab_orders` VALUES (1,'umesh','1997-01-31','male',1,1,500,200,2000,2000,NULL,1,1,'',4,NULL,NULL,'10:00:00.000000','lab/reports/download_8gzmEe5.pdf','2023-08-05','2024-12-14 09:09:44.620435','2024-12-14 09:21:00.321369',2,3,3);
/*!40000 ALTER TABLE `lab_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_packages`
--

DROP TABLE IF EXISTS `lab_packages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_packages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lab_specialization` varchar(100) DEFAULT NULL,
  `package_name` varchar(150) NOT NULL,
  `test_preparation` longtext,
  `package_img` varchar(100) DEFAULT NULL,
  `expected_delivery` varchar(50) NOT NULL,
  `lab_price` decimal(10,2) NOT NULL,
  `sale_price` decimal(10,2) NOT NULL,
  `promote` int NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `lab_id` bigint NOT NULL,
  `lab_service_id` bigint NOT NULL,
  `lab_tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_packages_lab_id_75a6c2ca_fk_laboratories_id` (`lab_id`),
  KEY `lab_packages_lab_service_id_bd2f3d00_fk_lab_services_id` (`lab_service_id`),
  KEY `lab_packages_lab_tag_id_e64c8806_fk_lab_tags_id` (`lab_tag_id`),
  CONSTRAINT `lab_packages_lab_id_75a6c2ca_fk_laboratories_id` FOREIGN KEY (`lab_id`) REFERENCES `laboratories` (`id`),
  CONSTRAINT `lab_packages_lab_service_id_bd2f3d00_fk_lab_services_id` FOREIGN KEY (`lab_service_id`) REFERENCES `lab_services` (`id`),
  CONSTRAINT `lab_packages_lab_tag_id_e64c8806_fk_lab_tags_id` FOREIGN KEY (`lab_tag_id`) REFERENCES `lab_tags` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_packages`
--

LOCK TABLES `lab_packages` WRITE;
/*!40000 ALTER TABLE `lab_packages` DISABLE KEYS */;
INSERT INTO `lab_packages` VALUES (2,'general_practice','Ila Bowen','Sed nihil dicta aspe','laboratory/packages/worker-avatar-icon-orange-worker.png','Quos ut facere totam',647.00,660.00,0,1,'2024-11-25 10:29:34.156991','2024-12-06 10:35:48.787262',2,2,2),(3,'cardiac_diagnostics','Kendall Mccullough','Rerum quo sit non q','laboratory/packages/logo_dOIR4ax.png','Ipsa illo labore cu',304.00,51.00,1,1,'2024-11-25 10:29:47.600679','2024-12-06 10:35:57.709622',2,3,4);
/*!40000 ALTER TABLE `lab_packages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_services`
--

DROP TABLE IF EXISTS `lab_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_services` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_emergency_service` tinyint(1) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `laboratory_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lab_services_laboratory_id_55c3a390_fk_laboratories_id` (`laboratory_id`),
  KEY `lab_services_service_id_63bfc1ed_fk_services_id` (`service_id`),
  CONSTRAINT `lab_services_laboratory_id_55c3a390_fk_laboratories_id` FOREIGN KEY (`laboratory_id`) REFERENCES `laboratories` (`id`),
  CONSTRAINT `lab_services_service_id_63bfc1ed_fk_services_id` FOREIGN KEY (`service_id`) REFERENCES `services` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_services`
--

LOCK TABLES `lab_services` WRITE;
/*!40000 ALTER TABLE `lab_services` DISABLE KEYS */;
INSERT INTO `lab_services` VALUES (2,0,1,'2024-11-25 08:14:51.743258','2024-11-25 08:22:05.745933',3,4),(3,0,1,'2024-11-25 08:24:15.657953','2024-11-25 08:24:15.658953',3,2);
/*!40000 ALTER TABLE `lab_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_staff`
--

DROP TABLE IF EXISTS `lab_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(150) NOT NULL,
  `profile_img` varchar(100) DEFAULT NULL,
  `qualification` varchar(255) NOT NULL,
  `experience` int unsigned NOT NULL,
  `staff_type` varchar(20) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `laboratory_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `lab_staff_laboratory_id_33bc5fd8_fk_laboratories_id` (`laboratory_id`),
  CONSTRAINT `lab_staff_laboratory_id_33bc5fd8_fk_laboratories_id` FOREIGN KEY (`laboratory_id`) REFERENCES `laboratories` (`id`),
  CONSTRAINT `lab_staff_chk_1` CHECK ((`experience` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_staff`
--

LOCK TABLES `lab_staff` WRITE;
/*!40000 ALTER TABLE `lab_staff` DISABLE KEYS */;
INSERT INTO `lab_staff` VALUES (2,'Akeem Dickerson','8852147890','dide@mailinator.com','laboratory/staff_profiles/user-removebg-preview.png','Non deleniti laborum',5,'sample_collector',1,'2024-11-25 09:11:08.184940','2024-11-25 09:11:08.184940',3),(3,'Kato Buchanan','9876524012','dyrywyz@mailinator.com','','Quod eaque ipsum qu',5,'technician',1,'2024-11-25 09:11:50.251178','2024-11-25 09:11:50.251178',2);
/*!40000 ALTER TABLE `lab_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_tags`
--

DROP TABLE IF EXISTS `lab_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(150) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_tags`
--

LOCK TABLES `lab_tags` WRITE;
/*!40000 ALTER TABLE `lab_tags` DISABLE KEYS */;
INSERT INTO `lab_tags` VALUES (2,'Alexis Brennan',1,'2024-11-25 07:35:40.746222','2024-11-25 07:35:40.746222'),(3,'Orson Brennan',1,'2024-11-25 07:35:47.829173','2024-11-25 07:36:10.104655'),(4,'Simone Buckley',0,'2024-11-25 07:35:54.134425','2024-11-25 07:35:54.134425'),(5,'Nerea Mueller',1,'2024-11-25 07:36:01.159456','2024-11-25 07:36:16.645441');
/*!40000 ALTER TABLE `lab_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laboratories`
--

DROP TABLE IF EXISTS `laboratories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laboratories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lab_name` varchar(150) NOT NULL,
  `address` longtext NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `description` longtext NOT NULL,
  `lab_image` varchar(100) DEFAULT NULL,
  `status` int NOT NULL,
  `city` varchar(100) NOT NULL,
  `postal_code` varchar(20) NOT NULL,
  `state_province` varchar(100) NOT NULL,
  `alternate_number` varchar(15) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `operating_hours` varchar(100) NOT NULL,
  `specializations` varchar(100) DEFAULT NULL,
  `insurance_accepted` longtext,
  `payment_methods` varchar(50) NOT NULL,
  `emergency_services` int NOT NULL,
  `home_sample_collection` int NOT NULL,
  `report_delivery_options` varchar(20) NOT NULL,
  `accreditations_certifications` longtext,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `lab_commission` decimal(5,2) NOT NULL,
  `promote` int NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `laboratories_user_id_39c062ab_fk_all_users_id` FOREIGN KEY (`user_id`) REFERENCES `all_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratories`
--

LOCK TABLES `laboratories` WRITE;
/*!40000 ALTER TABLE `laboratories` DISABLE KEYS */;
INSERT INTO `laboratories` VALUES (2,'Lydia Banks','Voluptatem Reprehen','9650025100','Qui do ut autem qui ','worker-avatar-icon-orange-worker.png',1,'Lorem laborum est it','Et culpa deserunt p','Expedita quia magnam','8521478520','https://www.viqupun.biz','2','general_practice','Deleniti maxime duci','Credit Card',1,0,'Email',NULL,22.73206287528731,75.87770710068718,30.00,0,13),(3,'Brian Boyle','Velit tenetur iste ','9632584002','Atque expedita nesci','logo.png',1,'Omnis facere et numq','Irure non deserunt o','Et pariatur Harum a','8520023510','https://www.goma.tv','6','general_practice','Tempora laborum dolo','Cash',1,1,'Physical Copy',NULL,22.716816225475938,75.8699244260788,50.00,0,14),(4,'Louis Stokes','Ut voluptatum animi','7085600230','Veniam voluptatem c','user_p9ttlS5.png',1,'Neque id animi vol','456878','Fugiat amet non au','8003669012','https://www.dyl.mobi','2','cardiac_diagnostics','Vel molestiae volupt','Credit Card',1,0,'Physical Copy',NULL,22.72021454992609,75.85546199063897,100.00,1,24),(5,'Umesh Lab','testing','8575003201','yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy','4642a8f387560c4eaa0ba769f88ed659.jpg',1,'Indore','450054','mp','9254100302','https://www.luxu.cm','2','cardiac_diagnostics','yyyyyyyyyyyyeerererytgdddddddddddddddddddddfg','Cash',1,0,'Email',NULL,22.718081880968427,75.86537003517152,30.00,1,30);
/*!40000 ALTER TABLE `laboratories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medications`
--

DROP TABLE IF EXISTS `medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medications`
--

LOCK TABLES `medications` WRITE;
/*!40000 ALTER TABLE `medications` DISABLE KEYS */;
INSERT INTO `medications` VALUES (1,'Ketosteril 2.5MG Tab 100`s',NULL,1,'2024-12-04 17:35:16.000000','2024-12-04 17:35:16.000000'),(2,'Onglyza 5MG Tab 28`s',NULL,1,'2024-12-04 17:35:16.000000','2024-12-04 17:35:16.000000'),(3,'Forxiga 5MG Tab 28`s',NULL,1,'2024-12-04 17:35:16.000000','2024-12-04 17:35:16.000000'),(4,'Galvus 50MG Tab 28`s',NULL,1,'2024-12-04 17:35:16.000000','2024-12-04 17:35:16.000000'),(5,'Actapro 100MG Tab 10`s',NULL,1,'2024-12-04 17:35:16.000000','2024-12-04 17:35:16.000000');
/*!40000 ALTER TABLE `medications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module_offer_banners`
--

DROP TABLE IF EXISTS `module_offer_banners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `module_offer_banners` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `link` varchar(250) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `app_module_id` int NOT NULL,
  `banner` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `module_offer_banners_app_module_id_29653cda_fk_App_module_id` (`app_module_id`),
  CONSTRAINT `module_offer_banners_app_module_id_29653cda_fk_App_module_id` FOREIGN KEY (`app_module_id`) REFERENCES `app_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_offer_banners`
--

LOCK TABLES `module_offer_banners` WRITE;
/*!40000 ALTER TABLE `module_offer_banners` DISABLE KEYS */;
INSERT INTO `module_offer_banners` VALUES (2,'',1,'2024-11-27 13:19:07.356549','2024-11-27 13:31:59.340956',2,'banners/outpatient_services.png'),(3,'https://www.fezolovoj.tv',1,'2024-11-27 13:19:22.422305','2024-11-27 13:32:14.876132',3,'banners/cardiology_services.png'),(4,'',1,'2024-11-27 13:20:24.845430','2024-11-27 13:30:23.878131',1,'banners/lab_banner_1.png');
/*!40000 ALTER TABLE `module_offer_banners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `status` smallint NOT NULL,
  `meta` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `app_module_id` int DEFAULT NULL,
  `customer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `notifications_app_module_id_f52c705e_fk_app_module_id` (`app_module_id`),
  KEY `notifications_customer_id_f298cc62_fk_customers_id` (`customer_id`),
  CONSTRAINT `notifications_app_module_id_f52c705e_fk_app_module_id` FOREIGN KEY (`app_module_id`) REFERENCES `app_module` (`id`),
  CONSTRAINT `notifications_customer_id_f298cc62_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'Booking Successful','Your bed booking has been confirmed successfully. Please check your booking details in the app.',NULL,'success',0,'{\"severity\": \"low\"}','2024-12-13 15:35:37.000000','2024-12-13 15:35:37.000000',1,2),(2,'Appointment Reminder','Your appointment with Dr. is scheduled.',NULL,'reminder',1,'{\"priority\": \"high\"}','2024-12-13 15:35:37.000000','2024-12-13 15:35:37.000000',2,2),(3,'Lab Order Confirmation','Your lab order has been successfully placed. You will receive updates once the results are ready.',NULL,'confirmation',0,'{\"priority\": \"medium\"}','2024-12-13 15:35:37.000000','2024-12-13 15:35:37.000000',3,2);
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reminder_categories`
--

DROP TABLE IF EXISTS `reminder_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reminder_categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reminder_categories`
--

LOCK TABLES `reminder_categories` WRITE;
/*!40000 ALTER TABLE `reminder_categories` DISABLE KEYS */;
INSERT INTO `reminder_categories` VALUES (1,'Appointment Reminder',1,'2024-12-04 16:09:20.000000','2024-12-04 16:09:20.000000'),(2,'Test Reminder',1,'2024-12-04 16:09:20.000000','2024-12-04 16:09:20.000000');
/*!40000 ALTER TABLE `reminder_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reminders`
--

DROP TABLE IF EXISTS `reminders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reminders` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext,
  `reminder_date` datetime(6) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reminders_category_id_27aefbc7_fk_reminder_categories_id` (`category_id`),
  KEY `reminders_customer_id_36affe93_fk_customers_id` (`customer_id`),
  CONSTRAINT `reminders_category_id_27aefbc7_fk_reminder_categories_id` FOREIGN KEY (`category_id`) REFERENCES `reminder_categories` (`id`),
  CONSTRAINT `reminders_customer_id_36affe93_fk_customers_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reminders`
--

LOCK TABLES `reminders` WRITE;
/*!40000 ALTER TABLE `reminders` DISABLE KEYS */;
INSERT INTO `reminders` VALUES (2,'Lab Test Reminder','Blood test for cholesterol','2024-12-11 09:00:00.000000',1,'2024-12-04 09:05:00.000000','2024-12-05 09:14:32.405103',2,2),(3,'Doctor Appointment','Reminder to visit the doctor at 5 PM.','2024-08-31 18:30:00.000000',1,'2024-12-04 13:29:10.615526','2024-12-04 13:29:10.615526',1,2),(4,'Doctor testing','Reminder to visit the doctor at 5 PM.','2024-08-31 18:30:00.000000',0,'2024-12-05 11:34:29.261114','2024-12-05 11:51:55.578303',2,2);
/*!40000 ALTER TABLE `reminders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `service_name` varchar(150) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (2,'Olympia Marquez',1,'2024-11-25 07:55:02.394100','2024-11-25 07:55:02.394100'),(3,'Tatiana Daugherty',0,'2024-11-25 07:55:12.868733','2024-11-25 07:55:12.868733'),(4,'Juliet Frederick',1,'2024-11-25 07:55:21.718422','2024-11-25 07:55:21.718422');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialist_categories`
--

DROP TABLE IF EXISTS `specialist_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialist_categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL,
  `category_image` varchar(100) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialist_categories`
--

LOCK TABLES `specialist_categories` WRITE;
/*!40000 ALTER TABLE `specialist_categories` DISABLE KEYS */;
INSERT INTO `specialist_categories` VALUES (2,'General','specialist_category_images/general_kofosdF.png',1,'2024-11-20 06:04:06.180701','2024-11-20 06:04:06.180701'),(3,'Gastrointestinal','specialist_category_images/gastrointestinal.png',1,'2024-11-20 06:04:23.004771','2024-11-20 06:04:23.004771'),(4,'Urinary','specialist_category_images/urinary.png',1,'2024-11-20 06:05:02.200249','2024-11-20 06:05:02.200249'),(5,'Cardiovascular','specialist_category_images/cardiovascular.png',1,'2024-11-20 06:08:40.068870','2024-11-20 06:08:40.068870');
/*!40000 ALTER TABLE `specialist_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `symptoms`
--

DROP TABLE IF EXISTS `symptoms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `symptoms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `symptom_name` varchar(255) NOT NULL,
  `symptom_image` varchar(100) DEFAULT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `specialist_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `symptoms_specialist_id_978a46fe_fk_specialist_categories_id` (`specialist_id`),
  CONSTRAINT `symptoms_specialist_id_978a46fe_fk_specialist_categories_id` FOREIGN KEY (`specialist_id`) REFERENCES `specialist_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `symptoms`
--

LOCK TABLES `symptoms` WRITE;
/*!40000 ALTER TABLE `symptoms` DISABLE KEYS */;
INSERT INTO `symptoms` VALUES (2,'Night sweats','symptoms_images/night_sweats.png',1,'2024-11-20 06:35:38.400096','2024-11-20 06:35:52.384265',2);
/*!40000 ALTER TABLE `symptoms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wards`
--

DROP TABLE IF EXISTS `wards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wards` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ward_name` varchar(255) NOT NULL,
  `status` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `hospital_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `H2H_admin_ward_hospital_id_8343bff0_fk_hospitals_id` (`hospital_id`),
  CONSTRAINT `H2H_admin_ward_hospital_id_8343bff0_fk_hospitals_id` FOREIGN KEY (`hospital_id`) REFERENCES `hospitals` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wards`
--

LOCK TABLES `wards` WRITE;
/*!40000 ALTER TABLE `wards` DISABLE KEYS */;
INSERT INTO `wards` VALUES (1,'General',1,'2024-11-19 10:20:10.702124','2024-11-19 10:49:11.926151',4),(3,'ICCU',1,'2024-11-19 10:54:05.079513','2024-11-19 10:54:05.079513',4);
/*!40000 ALTER TABLE `wards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-19 16:24:48
