<?php
$c=mysqli_connect("localhost","root","","user");
if(!$c)
{
    echo "connection failed".mysqli_connect_error();
    exit();
}
else
{
    echo "Sucessfull connection<br>";
}
?>