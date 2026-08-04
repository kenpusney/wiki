---
title: 能否举出各种例子，关于 ruby 可以做一件事用很多方法？
date: 2015-12-31
origin: https://www.zhihu.com/question/39046714/answer/79427045
---
# 能否举出各种例子，关于 ruby 可以做一件事用很多方法？

[知乎链接](https://www.zhihu.com/question/39046714/answer/79427045)

---------

```rb
#; beginner's way
puts "hello"
puts "hello"
puts "hello"
puts "hello"
puts "hello"

#; python way
for i in 0..5
   puts "hello"
end

#; using block
5.times do
    puts "hello"
end

#; each
(["hello"] * 5).each do |item| 
    puts item
end

#; print
print "hello\n"*5
```
