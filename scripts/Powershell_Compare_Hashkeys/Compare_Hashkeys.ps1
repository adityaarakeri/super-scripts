$Algorithm = $args[0]
$file = $args[1]
$hash = $args[2]
$MyHash = (Get-FileHash $file -Algorithm $Algorithm).Hash

if($MyHash -eq $hash){
	echo "Hashes are identical!"
}else{
	echo "Hashes are NOT identical!"
}