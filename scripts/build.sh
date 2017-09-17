#!/bin/bash
#cd "`dirname "$0"`"
#cd ..

#mkdir -p /blog_github/_posts
#[ -e _resources ] && rm -rf *
#cd ..
rm -rf /blog_github/_posts/*

zim --export \
--format=html --template=Print \
--output=/blog_github/_posts --index-page=sitemap \
--recursive \
--overwrite \
~/git-dir/data_work

rm -rf /blog_github/_posts/company*
rm -rf /blog_github/_posts/COMMAND*
rm -rf sitemap.html
