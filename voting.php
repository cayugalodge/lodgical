<html>
<head>
	<title>Cast your votes</title>
	
</head>
<body>
<h2>Hello: cast your votes on a sliding scale from 0 to 3</h2>
<h3> Once you click submit you will move to the results page and will be able to see the current results.</h3>
<form action="results.php" method="post">
<?php
$names_array = file('names.txt');
foreach($names_array as $name){
	echo $name .'<input type="range" name='."$name" .'min = "0" max="3" value="0"> <br/>'  ;
}
?>
		<input type="submit">

	</form>
</body>
</html>