---
title: 求助，谁能描述sortedArrayUsingComparator是如何进行比较的？
date: 2014-12-18
origin: https://www.zhihu.com/question/27138646/answer/35401342
---
# 求助，谁能描述sortedArrayUsingComparator是如何进行比较的？

[知乎链接](https://www.zhihu.com/question/27138646/answer/35401342)

---------

谢邀。

手头没有Xcode，只能根据文档和我的揣测来回答。
根据[NSArray Class Reference](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/index.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingComparator):
> **sortedArrayUsingComparator:**
> Returns an array that lists the receiving array’s elements in **ascending** order, as determined by the comparison method specified by a given NSComparator Block.

也即，这个sortedArrayUsingComparator这个方法本身就是按递增的方式排序，而怎么定义递增，就看是Comparator怎么设计的了。
对于[Comparator的返回值](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Constants/index.html#//apple_ref/c/tdef/NSComparisonResult)文档有下面的说明：
> - NSOrderedAscending
>
> The left operand is **smaller **than the right operand.
>
> - NSOrderedSame
>
> The two operands are equal.
>
> - NSOrderedDescending
>
> The left operand is **greater** than the right operand.

如果你期望的是值小的在前而值大的在后，则可以在比较的时候返回NSOrderedAscending（-1），否则，就是NSOrderedDescending（1）。
而题主的代码，在判断的时候用的是**>（greater）**，返回的确是-1，得到的肯定是跟预期恰好相反的结果。

以上。
