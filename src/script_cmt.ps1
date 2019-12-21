# this script will commit the changes

param([Int32]$Y=19,
[Int32]$M=12,
[Int32]$D=21,
[Int32]$I=12,
[String]$F='1.txt'
)

$GIT_COMMITTER_DATE
$GIT_AUTHOR_DATE
GIT add $F -f
GIT commit --date="$Y-$M-$D 12:$I:01" -m "committed on $Y-$M-$D for output dump"