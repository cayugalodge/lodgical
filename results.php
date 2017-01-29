<html>
<head>
	<title>Results are in!</title>
	<style type="text/css"> p {max-width: 600px;} </style>
</head>
<body>
<h1> You Just Voted! </h1>
<h4><strong>DO NOT GO BACK TO THE LAST PAGE. IT WILL RUIN EVERYTHING</strong></h4>\
<?php
$names_array = array_keys($_POST);
$total_votes_used = array_sum($_POST);
echo "You placed a total of  <strong>". $total_votes_used ."</strong> votes";
//THis if statement decides how many votes each person can use.
if ($total_votes_used == 10 ) {
	foreach( $names_array as $name){
		$current_file = fopen($name.".txt","a");
		fwrite($current_file, $_POST[$name]."\n");
		fclose($current_file);
	}
}
	
?>
<form action="results.php" method="post">
	Commands: <input type="text" name="command"><br>
	<input type="submit">
</form>
<?php
$file_names_array = file('names.txt');
	if ($_POST["command"] == "end") {
		foreach( $file_names_array as $name){
	$name = trim($name);
	$filename = $name.'.txt';
	$score_array = file($filename);
	$total_score_current = array_sum($score_array);
	echo $name." has a total score of: ". $total_score_current. "</br>" ;
}
}
/*if ($_POST["command"] == "clear") {
	//attempting to clear files scores
	$names_array = file('names.txt');
		foreach( $names_array as $name){
			$name = trim($name);
			$filename = $name.'.txt';
			$current_file = fopen($fileneame, "w+");
			fwrite($current_file, "")
			fclose($filename);
	}
}*/
?>


<h2>Here is some light reading while you wait for others to vote and the next round to start:</h2>
<p>According to The Marx Neitchze Freud teacher: some native american languages replace our three temporal tenses (past present and future), with two tenses: things that are in my perception, and things that are not in my perception. The things that aren't inn my perception can include things that are behind me, my parents (who aren't here rn) things that could happen tomorrow and things that did happen thousands of years ago. Do you think that this linguistic difference would have effects on the scheduling of trains? Is our bizarely skewed conception of space a result of the need to mandate humanity through the construction of time, in order to force people to <a href="https://www.youtube.com/watch?v=5GL9JoH4Sws"> work work work work work work? </a></p>

<h3>Here is some not light reading</h3>
<h4>This is an except from Deep Green Resistance.. DGR as an organization is problamatic (transphobic and authoritarian) and I don't encourage following them.. But the book has some cool shit in it.</h4>
<p>The dominant culture—civilization—is killing the planet, and it is long past time for those of us who care about life on earth to begin taking the actions necessary to stop this culture from destroying every living being.
</br>
By now we all know the statistics and trends: 90 percent of the large fish in the oceans are gone, there is ten times as much plastic as phytoplankton in the oceans, 97 percent of native forests are destroyed, 98 percent of native grasslands are destroyed, amphibian populations are collapsing, migratory songbird populations are collapsing, mollusk populations are collapsing, fish populations are collapsing, and so on.
</br>
This culture destroys landbases. That’s what it does. When you think of Iraq, is the first thing that comes to mind cedar forests so thick that sunlight never touched the ground? One of the first written myths of this culture is about Gilgamesh deforesting the hills and valleys of Iraq to build a great city. The Arabian Peninsula used to be oak savannah. The Near East was heavily forested (we’ve all heard of the cedars of Lebanon). Greece was heavily forested. North Africa was heavily forested.
</br>
<strong>We’ll say it again: this culture destroys landbases.</strong>
</br>
And it won’t stop doing so because we ask nicely.
</br>
We don’t live in a democracy. And before you gasp at this blasphemy, ask yourself: Do governments better serve corporations or living beings? Does the judicial system hold CEOs accountable for their destructive, often murderous acts?
</br>
Here are a couple of riddles that aren’t very funny—Q: What do you get when you cross a long drug habit, a quick temper, and a gun? A: Two life terms for murder, earliest release date 2026. Q: What do you get when you cross two nation-states, a large corporation, forty tons of poison, and at least 8,000 dead human beings? A: Retirement, with full pay and benefits (Warren Anderson, CEO of Union Carbide, which caused the mass murder at Bhopal).
</br>
Do the rich face the same judicial system as you or I? Does life on earth have as much standing in a court as does a corporation?
</br>
We all know the answers to these questions.
</br>
And we know in our bones, if not our heads, that this culture will not undergo any sort of voluntary transformation to a sane and sustainable way of living. We—Aric, Lierre, and Derrick—have asked thousands upon thousands of people from all walks of life, from activists to students to people we meet on buses and planes, whether they believe this culture will undergo that voluntary transformation. Almost no one ever says yes.
</br>
If you care about life on this planet, and if you believe this culture won’t voluntarily cease to destroy it, how does that belief affect your methods of resistance?
</br>
Most people don’t know, because most people don’t talk about it.

</br>
<strong>We must put our bodies and our lives between the industrial system and life on this planet.</strong> We must start to fight back. Those who come after, who inherit whatever’s left of the world once this culture has been stopped—whether through peak oil, economic collapse, ecological collapse, or the efforts of brave women and men resisting in alliance with the natural world—are going to judge us by the health of the landbase, by what we leave behind. They’re not going to care how you or I lived our lives. They’re not going to care how hard we tried. They’re not going to care whether we were nice people. They’re not going to care whether we were nonviolent or violent.<strong> They’re not going to care whether we grieved the murder of the planet. They’re not going to care whether we were enlightened or not. They’re not going to care what sort of excuses we had to not act </strong>(e.g., “I’m too stressed to think about it,” or “It’s too big and scary,” or “I’m too busy,” or “But those in power will kill us if we effectively act against them,” or “If we fight back, we run the risk of becoming like they are,” or “But I recycled,” or any of a thousand other excuses we’ve all heard too many times). They’re not going to care how simply we lived. They’re not going to care how pure we were in thought or action. They’re not going to care if we became the change we wished to see. They’re not going to care whether we voted Democrat, Republican, Green, Libertarian, or not at all. They’re not going to care if we wrote really big books about it. They’re not going to care whether we had “compassion” for the CEOs and politicians running this deathly economy.
</br>
<strong>They’re going to care whether they can breathe the air and drink the water.</strong> We can fantasize all we want about some great turning, but if the people (including the nonhuman people) can’t breathe, it doesn’t matter.</p>
</body>
</html>