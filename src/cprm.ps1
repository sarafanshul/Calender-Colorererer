param(
[String]$F = 'Codes'
)
$dr = $(get-location)
Move-Item "$dr\$F\main_dir" "$dr"
Move-Item "$dr\$F\.git" "$dr"
rm $F
