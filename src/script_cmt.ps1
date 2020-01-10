# this script will commit the changes

param([Int32]$Y=19,
[Int32]$M=12,
[Int32]$D=21,
[Int32]$I=12,
[String]$F='1003.cpp',
[String]$Fn='README.md',
[String]$Txt = 'Dont Stop'
)

$GIT_COMMITTER_DATE = "$Y-$M-$D 12:$i:00"
$GIT_AUTHOR_DATE = "$Y-$M-$D 12:$i:00"

GIT add $F -f
GIT commit --date="$Y-$M-$D 12:$I:01" -m  " $Y-$M-$D -$Txt"