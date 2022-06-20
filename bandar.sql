-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2022 at 08:57 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bandar`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(11) NOT NULL,
  `hotel_name` varchar(55) NOT NULL,
  `city_name` varchar(55) NOT NULL,
  `room_price` varchar(100) DEFAULT NULL,
  `advance_booking_time` varchar(100) DEFAULT NULL,
  `booking_id` varchar(100) DEFAULT NULL,
  `booked_by` varchar(100) DEFAULT NULL,
  `booking_date` varchar(100) DEFAULT NULL,
  `currency` varchar(100) DEFAULT NULL,
  `additional_services_price` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `hotel_name`, `city_name`, `room_price`, `advance_booking_time`, `booking_id`, `booked_by`, `booking_date`, `currency`, `additional_services_price`, `user_id`) VALUES
(3, 'Fort Contenantal', 'Berlin', '2810', '60', '925424AB6', 'Bandar', '2022-06-15', 'PKR', '10', 2),
(4, 'KGF', 'Berlin', '697.5', '30', '1B291181B', 'Bandar', '2022-06-15', 'QAR', '67.5', 2);

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `hotel_id` int(11) NOT NULL,
  `hotel_name` varchar(55) NOT NULL,
  `city_name` varchar(100) DEFAULT NULL,
  `rooms_capicity` varchar(100) DEFAULT NULL,
  `off_peak_season_room_price` varchar(100) DEFAULT NULL,
  `peak_season_room_price` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`hotel_id`, `hotel_name`, `city_name`, `rooms_capicity`, `off_peak_season_room_price`, `peak_season_room_price`) VALUES
(1, 'Park Inn', 'Berlin', '120', '70', '140'),
(3, 'Fort Contenantal', 'Berlin', '120', '70', '140'),
(4, 'Contental Hotel', 'Madrid', '130', '60', '160'),
(5, 'Pearl Continental', 'Madrid', '130', '60', '160'),
(6, 'KGF', 'Berlin', '120', '70', '140');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `password` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'Admin', 'admin@gmail.com', 'sha256$GX1YXKXoDbBlBxO0$7a364b717dc2046ed0df29e4bcb0e40a976038e4bb4b7e99aaf1c185c825a497'),
(2, 'Bandar', 'bandar@gmail.com', 'sha256$6wvce6EkITlx8HQH$bbb54ec4fcf9ac208cb0582a6c92847b8a38de19c6b9b86b8bafcb972b7d5884');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`hotel_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hotel`
--
ALTER TABLE `hotel`
  MODIFY `hotel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
