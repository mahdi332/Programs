-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2024 at 11:09 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shoedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `adding`
--

CREATE TABLE `adding` (
  `product_code` int(11) DEFAULT NULL,
  `provider_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `assign`
--

CREATE TABLE `assign` (
  `discount_code` int(11) DEFAULT NULL,
  `product_code` int(11) DEFAULT NULL,
  `expire_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `phone_number` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `discount`
--

CREATE TABLE `discount` (
  `discount_code` int(11) NOT NULL,
  `discount_percent` float NOT NULL,
  `expiration_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `position` varchar(10) NOT NULL,
  `income` int(11) DEFAULT NULL,
  `phone_number` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `ID` int(11) NOT NULL,
  `payment_id` int(11) NOT NULL,
  `discount_code` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `name` varchar(50) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `phone_number` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`name`, `address`, `phone_number`) VALUES
('mahdi', 'inja', '09170097975');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_code` int(11) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `brand` varchar(10) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_code`, `type`, `brand`, `size`, `price`) VALUES
(1654, 'shoe', 'nike', '46', 20);

-- --------------------------------------------------------

--
-- Table structure for table `provide`
--

CREATE TABLE `provide` (
  `provider_code` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `provider`
--

CREATE TABLE `provider` (
  `company_registration_code` int(11) NOT NULL,
  `phone_number` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`company_registration_code`, `phone_number`) VALUES
(123, '09170097975');

-- --------------------------------------------------------

--
-- Table structure for table `shipping`
--

CREATE TABLE `shipping` (
  `tracking_code` int(11) NOT NULL,
  `s_date` date DEFAULT NULL,
  `r_date` date DEFAULT NULL,
  `transport_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shopcard`
--

CREATE TABLE `shopcard` (
  `product_code` int(11) NOT NULL,
  `p_status` tinyint(1) DEFAULT current_timestamp(),
  `order_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shopcard`
--

INSERT INTO `shopcard` (`product_code`, `p_status`, `order_date`) VALUES
(1654, 1, '2024-06-02 14:32:51');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `payment_id` int(11) NOT NULL,
  `type` varchar(10) DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transport`
--

CREATE TABLE `transport` (
  `transport_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adding`
--
ALTER TABLE `adding`
  ADD UNIQUE KEY `product_code` (`product_code`),
  ADD UNIQUE KEY `provider_id` (`provider_id`);

--
-- Indexes for table `assign`
--
ALTER TABLE `assign`
  ADD UNIQUE KEY `discount_code` (`discount_code`),
  ADD UNIQUE KEY `product_code` (`product_code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `phone_number` (`phone_number`);

--
-- Indexes for table `discount`
--
ALTER TABLE `discount`
  ADD PRIMARY KEY (`discount_code`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`),
  ADD KEY `phone_number` (`phone_number`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `payment_id` (`payment_id`),
  ADD KEY `discount_code` (`discount_code`);

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`phone_number`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_code`);

--
-- Indexes for table `provide`
--
ALTER TABLE `provide`
  ADD KEY `provider_code` (`provider_code`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `provider`
--
ALTER TABLE `provider`
  ADD PRIMARY KEY (`company_registration_code`),
  ADD KEY `phone_number` (`phone_number`);

--
-- Indexes for table `shipping`
--
ALTER TABLE `shipping`
  ADD PRIMARY KEY (`tracking_code`),
  ADD UNIQUE KEY `transport_id` (`transport_id`);

--
-- Indexes for table `shopcard`
--
ALTER TABLE `shopcard`
  ADD PRIMARY KEY (`product_code`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `transport`
--
ALTER TABLE `transport`
  ADD PRIMARY KEY (`transport_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adding`
--
ALTER TABLE `adding`
  ADD CONSTRAINT `adding_ibfk_1` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`),
  ADD CONSTRAINT `adding_ibfk_2` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`company_registration_code`);

--
-- Constraints for table `assign`
--
ALTER TABLE `assign`
  ADD CONSTRAINT `assign_ibfk_1` FOREIGN KEY (`discount_code`) REFERENCES `discount` (`discount_code`),
  ADD CONSTRAINT `assign_ibfk_2` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`);

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`phone_number`) REFERENCES `person` (`phone_number`);

--
-- Constraints for table `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`phone_number`) REFERENCES `person` (`phone_number`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`payment_id`) REFERENCES `transactions` (`payment_id`),
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`discount_code`) REFERENCES `discount` (`discount_code`);

--
-- Constraints for table `provide`
--
ALTER TABLE `provide`
  ADD CONSTRAINT `provide_ibfk_1` FOREIGN KEY (`provider_code`) REFERENCES `provider` (`company_registration_code`),
  ADD CONSTRAINT `provide_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_code`);

--
-- Constraints for table `provider`
--
ALTER TABLE `provider`
  ADD CONSTRAINT `provider_ibfk_1` FOREIGN KEY (`phone_number`) REFERENCES `person` (`phone_number`);

--
-- Constraints for table `shipping`
--
ALTER TABLE `shipping`
  ADD CONSTRAINT `shipping_ibfk_1` FOREIGN KEY (`transport_id`) REFERENCES `transport` (`transport_id`);

--
-- Constraints for table `shopcard`
--
ALTER TABLE `shopcard`
  ADD CONSTRAINT `shopcard_ibfk_1` FOREIGN KEY (`product_code`) REFERENCES `products` (`product_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
