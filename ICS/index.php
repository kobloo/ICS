<html>
<head>
<title>ICS Time Log</title>
</head>
<body>
<center><h1><?php echo "TIME: ".date("h:i");?></h1>
<form method = "post" action = "../cgi-bin/ICS/update.cgi">
<input type = "hidden" name = "Employee" value = "<?php echo htmlspecialchars($_GET['Employee']);?>" >  
<input type = "submit" name = "Action" value = "Clock In">
<input type = "submit" name = "Action" value = "Clock Out">
<input type = "submit" name = "Action" value = "Clear">
</form>
<center>
<?php echo htmlspecialchars($_GET['Employee']);?>
</body>
</html>


