#write a bash script to reverse a string using 'for'
read -p "Enter a string: " str
len=${#str}
rev=""
for (( i=$len-1; i>=0; i-- ))
do
  rev="$rev${str:$i:1}"
done
echo "Reversed string: $rev"