<?php
        //Simple php api to get sensor data
                require"connect2.php";
                $temperature = $_GET["temp"];
                $humidity = $_GET["humi"];
                $time = $_GET["time"];
                $sensor = $_GET["sensor"];
                $ip = $_GET["ip"];
                $active = 1;

                $qery="INSERT INTO tbl_temp () VALUES ()";
                mysqli_query($con,$qery);

?>
