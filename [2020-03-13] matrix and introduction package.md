---
layout:     post
title:      [2020-03-13] matrix and introduction package
subtitle:   開發者需要依這個手冊作爲編程基本方向
date:       2020-03-13
author:     GEo
catalog: true
tags:
    - Python
    - Numeric Analysis
    - Course
---

## Matrix operation     

```
# Two matrices are initialized by value
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
```

```
#  add()is used to add matrices , 矩陣相加 。 
>> print (np.add(x,y))

Addition of two matrices: 
[[ 8 10]
 [13 15]]
```

```
# subtract()is used to subtract matrices , 矩陣相減 。
>> print (np.subtract(x,y))

Subtraction of two matrices :
[[-6 -6]
 [-5 -5]]
```

```
# divide()is used to divide matrices
>> print (np.divide(x,y))

Matrix Division :
[[0.14285714 0.25      ]
 [0.44444444 0.5       ]]
```

```
>> print (np.multiply(x,y))

Multiplication of two matrices: 
[[ 7 16]
 [36 50]]
```

```
>> print (np.dot(x,y))

The product of two matrices :
[[25 28]
 [73 82]]
```

```
>> print (np.sqrt(x))

square root of x is :
[[1.         1.41421356]
 [2.         2.23606798]]
```

```
>> print (np.sum(y))

The summation of elements in y  :
34
```

```
print ("The column wise summation  : ")
>> print (np.sum(y,axis=0))

The column wise summation  :
[16 18]
```

```
>> print (np.sum(y,axis=1))

The row wise summation: 
[15 19]
```

```
# using "T" to transpose the matrix
>> print (x.T)

Matrix transposition :
[[1 4]
[2 5]]
```

``` Science python ``` 

下圖是scipy 子套件的領域 

<img src='pictures/course-scipy.png'>

## How to Start Scipy in Jupyter (Ipython notebook)

打開 git bash or cmd , 前提是本地沒有 ```scipy``` 套件 

```pip install scipy ```

``` import scipy as sp``` sp 是任意名稱 , 可以任意取 , 但以後要知道從哪裏捉 scipy 的函數 。

## Review 

https://docs.scipy.org/doc/scipy/reference/tutorial/general.html

