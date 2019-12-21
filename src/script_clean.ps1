# this script pushes the commits and remove all the dump
git push origin master
git rm -rf 20**
git commit -am "cleanup"
git push origin master