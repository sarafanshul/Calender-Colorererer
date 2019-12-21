# # a million commits
# for Y in {2019..2020}
# do
#   mkdir $Y
#   cd $Y
#   for M in {02..12}
#   do
#     mkdir $M
#     cd $M
#     for D in {01..31}
#     do
#       mkdir $D
#       cd $D
#       for i in {01..5}
#       do
#         echo "$i on $M/$D/$Y" > commit.md
#         export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
#         export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
#         git add commit.md -f
#         git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
#       done
#       cd ../
#     done
#     cd ../
#   done
#   cd ../
# done
# git push origin master
# git rm -rf 20**
# git rm -rf 19**
# git commit -am "cleanup"
# git push origin master

# a million commits

RANDOM = $$
for Y in {2019..2019}
do
  mkdir $Y
  cd $Y
  for M in {01..12}
  do
    mkdir $M
    cd $M
    for D in {01..29}
    do
      mkdir $D
      cd $D
      for i in {1..12}
      do
        if [ $(( (10#$M + 10#$D) % 5 )) == 1 ]
        then
          if [ $(( 10#$RANDOM % 2)) == 0 ]
          then
            echo "$i on $M/$D/$Y" > commit.md
            export GIT_COMMITTER_DATE="$Y-$M-$D 12:$i:00"
            export GIT_AUTHOR_DATE="$Y-$M-$D 12:$i:00"
            git add commit.md -f
            git commit --date="$Y-$M-$D 12:0$i:00" -m "$i on $M $D $Y"
          else
            echo "left on $i , $M/$D/$Y"
          fi
        else
          echo "left on $i , $M/$D/$Y"
        fi
      done
      cd ../
    done
    cd ../
  done
  cd ../
done
git push origin master
git rm -rf 20**
git commit -am "cleanup"
git push origin master