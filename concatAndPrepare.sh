#!/bin/bash

###
### Remove previously used files.
###

rm import/comments_users_rel.csv
rm import/comments_subreddits_rel.csv
rm import/comments.csv
rm import/users.csv
rm import/subreddits.csv
rm import/aux.csv

###
### Prepare the POSTED_BY relation file
###
echo ":START_ID(Comment),:END_ID(User)" > import/comments_users_rel.csv

# Cat all the POSTED_BY files into this file.
for file in import/POSTED_BY*.csv; do
	cat $file >> import/comments_users_rel.csv
	rm $file
done

# Debugging
wc -l import/comments_users_rel.csv

###
### Prepare the POSTED_ON relation file
###
echo ":START_ID(Comment),:END_ID(Subreddit)" > import/comments_subreddits_rel.csv

# Cat all the POSTED_ON files into this file.
for file in import/POSTED_ON*.csv; do
	cat $file >> import/comments_subreddits_rel.csv
	rm $file
done

# Debugging
wc -l import/comments_subreddits_rel.csv

###
### Prepare the users file.
###

# Create temporary file to sort stuff in.
touch import/aux.csv
rm import/aux.csv
touch import/aux.csv


for file in import/users0*csv; do
	cat $file >> import/aux.csv
	rm $file
done

for file in import/users1*csv; do
	cat $file >> import/aux.csv
	rm $file
done

# Touch so it's safe to remove.
# touch import/users.csv

# Insert header
echo "userId:ID(User)" > import/users.csv

# Sort and insert in the right file.
sort -u import/aux.csv >> import/users.csv

# Remove the temp file.
rm import/aux.csv

echo "Number of users:"
wc -l import/users.csv

###
### Prepare the subreddits file.
###

# Create temporary file to sort stuff in.
touch import/aux.csv


for file in import/Subreddits*.csv; do
	cat $file >> import/aux.csv
	rm $file
done

# Touch so it's safe to remove.
touch import/subreddits.csv
rm import/subreddits.csv

# Insert header
echo "subredditId:ID(Subreddit)" > import/subreddits.csv

# Sort and insert in the right file.
sort -u import/aux.csv >> import/subreddits.csv

# Remove the temp file.
rm import/aux.csv

echo "Number of Subreddits:"
wc -l import/subreddits.csv

###
### Prepare the comment files
###

touch import/comments.csv

# Insert header
echo "commentId:ID(Comment),created_utc,score,downs,body" > import/comments.csv

for file in import/comments0*.csv; do
	cat $file >> import/comments.csv
	rm $file
done

for file in import/comments1*.csv; do
	cat $file >> import/comments.csv
	rm $file
done

wc -l import/comments.csv 