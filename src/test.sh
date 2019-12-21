# # RANDOM = $$
# # for i in `seq 10`
# # do
# # 	if [ $(( 10#$RANDOM % 2)) == 0 ]
# # 	then
# # 		echo $RANDOM
# # 	else
# # 		echo "not"
# # 	fi
# # done
# # $ cat myscript
# #!/bin/bash
# echo "First arg: $1"
# echo "Second arg: $2"
# # $ ./myscript hello world
# # First arg: hello
# # Second arg: world