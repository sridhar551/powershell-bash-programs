
$foo = Read-Host -Prompt 'Input your string'

function firstRepeatedChar {
	Param($foo)
	$foo = $foo.toCharArray()
	$arr = [System.Collections.ArrayList]@()
	foreach ($i in $foo){
		
		if($i -in $arr){
			return $i
		}
		else{
			$arrayID =$arr.Add($i)
		}
	}
	return "There is no repeated characters"	
}

firstRepeatedChar($foo)

function firstReccuringCharacter {
	Param($foo)
	$h=@()
	for($i=0; $i -lt $foo.length; $i++){
		if ($foo.IndexOf($foo[$i]) -ne $foo.LastIndexOf($foo[$i])){
			
			return $foo[$i]
		}
	}
	return "No results found"		
}

firstReccuringCharacter($foo)


