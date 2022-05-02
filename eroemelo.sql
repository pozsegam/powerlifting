-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2020. Nov 29. 15:52
-- Kiszolgáló verziója: 10.4.16-MariaDB
-- PHP verzió: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `eroemelo`
--
CREATE DATABASE IF NOT EXISTS `eroemelo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `eroemelo`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `biral`
--

DROP TABLE IF EXISTS `biral`;
CREATE TABLE IF NOT EXISTS `biral` (
  `VERSENYnev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `BIROszemelyi_szam` varchar(30) COLLATE utf8_hungarian_ci NOT NULL,
  `VERSENYdatum` date NOT NULL,
  PRIMARY KEY (`VERSENYnev`,`BIROszemelyi_szam`,`VERSENYdatum`),
  KEY `fk1_versenytbiral` (`VERSENYnev`,`VERSENYdatum`),
  KEY `fk2_biroSzemelyiSzama` (`BIROszemelyi_szam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `biral`
--

INSERT INTO `biral` (`VERSENYnev`, `BIROszemelyi_szam`, `VERSENYdatum`) VALUES
('APF Intro to Powerlifting Meet', '09808MW', '2019-03-20'),
('Arnold Classic Europe', '810274PO', '2019-08-10'),
('European Classic Masters Powerlifting', '37047AS', '2019-07-23'),
('European University Cup', '369285FD', '2018-05-10'),
('GPC European Championships', '582456HG', '2016-06-12'),
('World Championships', '369285FD', '2015-08-20'),
('World Cup WPC', '09808MW', '2017-11-11');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `biro`
--

DROP TABLE IF EXISTS `biro`;
CREATE TABLE IF NOT EXISTS `biro` (
  `szemelyi_szam` varchar(30) COLLATE utf8_hungarian_ci NOT NULL,
  `nev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  PRIMARY KEY (`szemelyi_szam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `biro`
--

INSERT INTO `biro` (`szemelyi_szam`, `nev`) VALUES
('09808MW', 'Németh Tamás'),
('369285FD', 'Tyler Marsh'),
('37047AS', 'Szepezdi János'),
('582456HG', 'Bailey Palmer'),
('810274PO', 'Harry Harrison'),
('932831RT', 'Kolbaszos Samuel');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `edzo`
--

DROP TABLE IF EXISTS `edzo`;
CREATE TABLE IF NOT EXISTS `edzo` (
  `EDZOszemelyi_szam` varchar(30) COLLATE utf8_hungarian_ci NOT NULL,
  `nev` varchar(50) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `szuletesi_ido` date DEFAULT NULL,
  `nemzetiseg` varchar(20) COLLATE utf8_hungarian_ci DEFAULT NULL,
  PRIMARY KEY (`EDZOszemelyi_szam`),
  KEY `EDZOszemelyi_szam` (`EDZOszemelyi_szam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `edzo`
--

INSERT INTO `edzo` (`EDZOszemelyi_szam`, `nev`, `szuletesi_ido`, `nemzetiseg`) VALUES
('123469TR', 'Nagy János', '1967-12-05', 'HU'),
('134677OI', 'Michael Lawson', '1987-12-21', 'AU'),
('145345FS', 'Miklós Attila', '1949-10-28', 'HU'),
('624578HT', 'Terrell Buck', '1978-04-15', 'US'),
('625781WE', 'Tom Hudson', '1988-10-08', 'US'),
('652489AS', 'Kovács Péter', '1968-09-03', 'HU'),
('895673HG', 'Kyle John', '1976-04-04', 'US');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `megnyerte`
--

DROP TABLE IF EXISTS `megnyerte`;
CREATE TABLE IF NOT EXISTS `megnyerte` (
  `VERSENYnev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `VERSENYZOversenyzoID` int(5) NOT NULL,
  `VERSENYdatum` date NOT NULL,
  PRIMARY KEY (`VERSENYnev`,`VERSENYZOversenyzoID`,`VERSENYdatum`),
  KEY `fk1_versenyzoID` (`VERSENYZOversenyzoID`),
  KEY `fk2_versenyneve` (`VERSENYnev`,`VERSENYdatum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `megnyerte`
--

INSERT INTO `megnyerte` (`VERSENYnev`, `VERSENYZOversenyzoID`, `VERSENYdatum`) VALUES
('APF Intro to Powerlifting Meet', 207, '2019-03-20'),
('Arnold Classic Europe', 123, '2019-08-10'),
('European Classic Masters Powerlifting', 49, '2019-07-23'),
('European University Cup', 1, '2018-05-10'),
('GPC European Championships', 32, '2016-06-12'),
('Reykjavik International Games', 1, '2020-09-09'),
('World Championships', 49, '2015-08-20'),
('World Cup WPC', 96, '2017-11-11');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szovetseg`
--

DROP TABLE IF EXISTS `szovetseg`;
CREATE TABLE IF NOT EXISTS `szovetseg` (
  `nev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `letrehozasDatuma` date NOT NULL,
  PRIMARY KEY (`nev`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szovetseg`
--

INSERT INTO `szovetseg` (`nev`, `letrehozasDatuma`) VALUES
('Global Powerlifting Committee', '2014-01-01'),
('International Powerlifting Federation', '1971-01-01'),
('World Powerlifting Congress', '2009-01-01');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `verseny`
--

DROP TABLE IF EXISTS `verseny`;
CREATE TABLE IF NOT EXISTS `verseny` (
  `VERSENYnev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `SZOVETSEGnev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `VERSENYdatum` date NOT NULL,
  `helyszin` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `szponzor` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  `versenyzokSzama` int(4) NOT NULL,
  PRIMARY KEY (`VERSENYnev`,`VERSENYdatum`),
  KEY `fk1_nev` (`SZOVETSEGnev`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `verseny`
--

INSERT INTO `verseny` (`VERSENYnev`, `SZOVETSEGnev`, `VERSENYdatum`, `helyszin`, `szponzor`, `versenyzokSzama`) VALUES
('APF Intro to Powerlifting Meet', 'World Powerlifting Congress', '2019-03-20', 'Boston', 'Titan', 65),
('Arnold Classic Europe', 'International Powerlifting Federation', '2019-08-10', 'Bécs', 'Eleiko', 98),
('European Classic Masters Powerlifting', 'International Powerlifting Federation', '2019-07-23', 'Párizs', 'Redbull', 123),
('European University Cup', 'International Powerlifting Federation', '2018-05-10', 'Koppenhága', 'Hell', 76),
('GPC European Championships', 'Global Powerlifting Committee', '2016-06-12', 'Amszterdam', 'Elitefts', 45),
('Reykjavik International Games', 'International Powerlifting Federation', '2020-09-09', 'Reykjavik', 'SBD', 100),
('World Championships', 'Global Powerlifting Committee', '2015-08-20', 'Budapest', 'Under Armour', 116),
('World Cup WPC', 'World Powerlifting Congress', '2017-11-11', 'New York', 'Slingshot', 67),
('World University Powerlifting Cup', 'International Powerlifting Federation', '2020-05-20', 'Brüsszel', 'SBD', 98);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `versenyez`
--

DROP TABLE IF EXISTS `versenyez`;
CREATE TABLE IF NOT EXISTS `versenyez` (
  `VERSENYnev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `VERSENYversenyzoID` int(5) NOT NULL,
  `VERSENYdatum` date NOT NULL,
  PRIMARY KEY (`VERSENYnev`,`VERSENYversenyzoID`,`VERSENYdatum`),
  KEY `fk1_versenyez` (`VERSENYnev`,`VERSENYdatum`),
  KEY `fk2_versenyzoID` (`VERSENYversenyzoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `versenyez`
--

INSERT INTO `versenyez` (`VERSENYnev`, `VERSENYversenyzoID`, `VERSENYdatum`) VALUES
('APF Intro to Powerlifting Meet', 1, '2019-03-20'),
('APF Intro to Powerlifting Meet', 9, '2019-03-20'),
('APF Intro to Powerlifting Meet', 207, '2019-03-20'),
('Arnold Classic Europe', 1, '2019-08-10'),
('Arnold Classic Europe', 123, '2019-08-10'),
('Arnold Classic Europe', 207, '2019-08-10'),
('European Classic Masters Powerlifting', 49, '2019-07-23'),
('European Classic Masters Powerlifting', 123, '2019-07-23'),
('European Classic Masters Powerlifting', 207, '2019-07-23'),
('European University Cup', 1, '2018-05-10'),
('European University Cup', 9, '2018-05-10'),
('European University Cup', 32, '2018-05-10'),
('European University Cup', 207, '2018-05-10'),
('GPC European Championships', 1, '2016-06-12'),
('GPC European Championships', 32, '2016-06-12'),
('GPC European Championships', 49, '2016-06-12'),
('GPC European Championships', 207, '2016-06-12'),
('World Championships', 49, '2015-08-20'),
('World Championships', 96, '2015-08-20'),
('World Championships', 207, '2015-08-20'),
('World Cup WPC', 49, '2017-11-11'),
('World Cup WPC', 96, '2017-11-11'),
('World Cup WPC', 123, '2017-11-11');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `versenyzo`
--

DROP TABLE IF EXISTS `versenyzo`;
CREATE TABLE IF NOT EXISTS `versenyzo` (
  `versenyzoID` int(5) NOT NULL,
  `EDZOszemelyi_szam` varchar(30) COLLATE utf8_hungarian_ci DEFAULT NULL,
  `szemelyi_szam` varchar(10) COLLATE utf8_hungarian_ci NOT NULL,
  `szuletesi_ido` date NOT NULL,
  `nev` varchar(50) COLLATE utf8_hungarian_ci NOT NULL,
  `nem` varchar(5) COLLATE utf8_hungarian_ci NOT NULL,
  `nemzetiseg` varchar(20) COLLATE utf8_hungarian_ci NOT NULL,
  PRIMARY KEY (`versenyzoID`),
  KEY `EDZOszemelyi_szam` (`EDZOszemelyi_szam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `versenyzo`
--

INSERT INTO `versenyzo` (`versenyzoID`, `EDZOszemelyi_szam`, `szemelyi_szam`, `szuletesi_ido`, `nev`, `nem`, `nemzetiseg`) VALUES
(1, '123469TR', '153469PR', '2001-10-05', 'Horváth Bence', 'm', 'HU'),
(9, '895673HG', '953469PR', '1999-01-12', 'Madeleine Graham', 'f', 'US'),
(32, '652489AS', '343449TR', '1999-02-13', 'Magyar Ferenc', 'm', 'HU'),
(49, '625781WE', '251438FV', '1991-12-15', 'Isac Willis', 'm', 'US'),
(96, '134677OI', '223138AG', '1987-06-30', 'Kevin Lambton', 'm', 'CA'),
(123, '145345FS', '753479PM', '1989-07-12', 'Kerekes Juliska', 'f', 'HU'),
(207, '624578HT', '679032LG', '2000-08-12', 'Rosina Insigne', 'f', 'IT');

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `biral`
--
ALTER TABLE `biral`
  ADD CONSTRAINT `fk1_versenytbiral` FOREIGN KEY (`VERSENYnev`,`VERSENYdatum`) REFERENCES `verseny` (`VERSENYnev`, `VERSENYdatum`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `fk2_biroSzemelyiSzama` FOREIGN KEY (`BIROszemelyi_szam`) REFERENCES `biro` (`szemelyi_szam`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Megkötések a táblához `edzo`
--
ALTER TABLE `edzo`
  ADD CONSTRAINT `edzo_ibfk_1` FOREIGN KEY (`EDZOszemelyi_szam`) REFERENCES `versenyzo` (`EDZOszemelyi_szam`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Megkötések a táblához `megnyerte`
--
ALTER TABLE `megnyerte`
  ADD CONSTRAINT `fk1_versenyzoID` FOREIGN KEY (`VERSENYZOversenyzoID`) REFERENCES `versenyzo` (`versenyzoID`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `fk2_versenyneve` FOREIGN KEY (`VERSENYnev`,`VERSENYdatum`) REFERENCES `verseny` (`VERSENYnev`, `VERSENYdatum`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Megkötések a táblához `verseny`
--
ALTER TABLE `verseny`
  ADD CONSTRAINT `fk1_nev` FOREIGN KEY (`SZOVETSEGnev`) REFERENCES `szovetseg` (`nev`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Megkötések a táblához `versenyez`
--
ALTER TABLE `versenyez`
  ADD CONSTRAINT `fk1_versenyez` FOREIGN KEY (`VERSENYnev`,`VERSENYdatum`) REFERENCES `verseny` (`VERSENYnev`, `VERSENYdatum`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `fk2_versenyzoID` FOREIGN KEY (`VERSENYversenyzoID`) REFERENCES `versenyzo` (`versenyzoID`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
