<?php
session_start();
include "connection.php";
if(isset($_POST['sub']))
{
    $uname=$_POST['uname'];
    $pass=$_POST['pass'];
    $sql="select * from student where user ='$uname' and pass = '$pass'";
    $res=mysqli_query($c,$sql);
    
    if(mysqli_num_rows($res)!= 0){

        $_SESSION['uname']=$uname;
        header("location:profile.php");
    }
    else{

        echo "<script>alert('No such user exist');
         location.href='login.php';
        </script>";

    }
}

// foreach($res as $r)
    // {
    //     if($r['name']==$uname && $r['password']==$pass)
    //     {
    //         $_SESSION['uname']=$uname;
    //         header("location:profile.php");
    //     }
    //     else{
    //         echo "No such user<br>";
    //         echo "<a href='login.php'><button>Login</button></a>";
    //     }
    // }
