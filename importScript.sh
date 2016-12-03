rm -rf data/databases/graph.db
bin/neo4j-import \
--into data/databases/graph.db \
--id-type string \
--nodes:User import/users.csv \
--nodes:Subreddit import/subreddits.csv \
--nodes:Comment import/comments.csv \
--relationships:POSTED_ON import/comments_subreddits_rel.csv \
--relationships:POSTED_BY import/comments_users_rel.csv \