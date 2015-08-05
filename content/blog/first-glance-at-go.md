title:Golang
Date: 2015-07-31 20:00
Modified: 2015-07-31 20:00
Category: Golang
Tags: Programming, Tutorial
Slug: first-glance-at-go 
Authors: nullne
Summary: 
##Go

###语法差异
-  Variables and Constant
```go
package main

var s string = "initial"

func main() {
    var a, b int = 1, 2
    const n = 5000000
    f := float64(3.3)
} 
```
- For Loop
```go
    // classic initial/condition/after for loop 
    for j := 7; j <= 9; j++ {
        fmt.Println(j)
    }
    
    // most basic for loop
    i := 1
    for i <= 3 {
        fmt.Println(i)
        i = i + 1
    }
    
    // infinite loop
    for {
        fmt.Println("loop")
    }
```
- If/Else
- Switch
```go
    // use commas to separate multiple expression in the same case statement 
    switch time.Now().Weekday() {
    case time.Saturday, time.Sunday:
        fmt.Println("it's the weekend")
    default:
        fmt.Println("it's a weekday")
    }

    // alternate way to implement If/Else while without an expression
    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("it's before noon")
    default:
        fmt.Println("it's after noon")
    }

```
-  Array, Slices, Maps
```go
    var a [5]int
    s := make([]string, 3)
    m := make(map[string]int)
```
- Functions
    Do NOT support nested functions, function overload, function default parameter
    - multiple return values
    ```go
    func vals() (int, int) {
        return 3, 7
    }
    func main() {
        a, b = vals()
        _, b = vals()
    }
    ```

    - variadic function  
    ```go
    func sum(nums ...int) {
        fmt.Printlf(nums)
    }
    func main() {
        sum(1, 2, 3)
        nums := []int{1, 2, 3, 4}
        sum(nums...)
    }
    ```
    - Clousure
        Go supports anonymous functions, which can form closures.
    - Defer
        ```go
        package main
        
        import "fmt"

        func main() {
            defer fmt.Println("世界")
            fmt.Println('Hello')
        }
        ```
        Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.
    - Panic
        ```go
        package main

        import "fmt"

        func test() {
            defer func() {
                if err := recover(); err != nil {
                    fmt.Println(err.(string))
                }
            }()
            panic("panic errors")
        }

        func main() {
            test()
        }
        ```
    - Errors
- Pointers,  Structs,  Methods, Interface
```go
// _Interfaces_ are named collections of method
// signatures.

package main

import "fmt"
import "math"

// Here's a basic interface for geometric shapes.
type geometry interface {
    area() float64
    perim() float64
}

// For our example we'll implement this interface on
// `rect` and `circle` types.
type rect struct {
    width, height float64
}
type circle struct {
    radius float64
}

// To implement an interface in Go, we just need to
// implement all the methods in the interface. Here we
// implement `geometry` on `rect`s.
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}

// The implementation for `circle`s.
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
    return 2 * math.Pi * c.radius
}

// If a variable has an interface type, then we can call
// methods that are in the named interface. Here's a
// generic `measure` function taking advantage of this
// to work on any `geometry`.
func measure(g geometry) {
    fmt.Println(g)
    fmt.Println(g.area())
    fmt.Println(g.perim())
}

func main() {
    r := rect{width: 3, height: 4}
    c := circle{radius: 5}

    // The `circle` and `rect` struct types both
    // implement the `geometry` interface so we can use
    // instances of
    // these structs as arguments to `measure`.
    measure(r)
    measure(c)
}
```
- Reflect
###多线程处理
- Goroutines
  A goroutine is a lightweight thread of execution.
  ```go
  
  package main
  import "fmt"

  func f(from string) {
        for i := 0; i < 3; i++ {
            fmt.Println(from, ":", i)
  } 
  func main() {
      go f("args")
      go func(msg string) {
          fmt.Println(msg)
      }("going")
    var input string
    fmt.Scanln(&input)
    fmt.Println("done")
  }
  ```
- Channels

    Channels are the pipes that connect concurrent goroutines. You can send values into channels from one goroutine and receive those values into another goroutine.
    ```go
package main
import "fmt"
func main() {
    messages := make(chan string)
    go func() { messages <- "ping" }()
    msg := <-messages
    fmt.Println(msg)
}
    ```

    - Channel Buffering
    ` messages := make(chan string, 2)`
    - Channel Direction
    `func pong(pings <-chan string, pongs chan<- string) {}`
    - Closing Channel
    `close(channel)`
    Closing channel means there is no more values to be sent , it is possible to close a non-empty channel
    - Range over channels
        Range can not only provide iteration over basic data structure, but also iterate over values received from a channel.
        
        ```go
        queue := make(chan string, 2)
        queue <- "one"
        queue <- "two"
        close(queue)
        for elem := range queue {
            fmt.Println(elem)
        }
        ```
- Select
```go
// Go's _select_ lets you wait on multiple channel
// operations. Combining goroutines and channels with
// select is a powerful feature of Go.

package main

import "time"
import "fmt"

func main() {

    // For our example we'll select across two channels.
    c1 := make(chan string)
    c2 := make(chan string)

    // Each channel will receive a value after some amount
    // of time, to simulate e.g. blocking RPC operations
    // executing in concurrent goroutines.
    go func() {
        time.Sleep(time.Second * 1)
        c1 <- "one"
    }()
    go func() {
        time.Sleep(time.Second * 2)
        c2 <- "two"
    }()

    // We'll use `select` to await both of these values
    // simultaneously, printing each one as it arrives.
    for i := 0; i < 2; i++ {
        select {
        case msg1 := <-c1:
            fmt.Println("received", msg1)
        case msg2 := <-c2:
            fmt.Println("received", msg2)
        }
    }
}
```
###包管理
- Go 语言中 `import` 语句使用绝对路径的方式引入安装到本地的包。
- 使用 `go get` 命令安装远程仓库中托管的包
- Go 语言还提供了一个 Workspace 的机制。通过设定 GOPATH环境变量，指定除了GOROOT所指定的目录之外，Go 代码所在的位置 (也就是 Workspace 的位置)。 一般来说，GOPATH目录下会包含pkg、src和bin三个子目录，这三个目录各有用处。
    -   **bin** 目录用来放置编译好的可执行文件，为了使得这里的可执行文件可以方便的运行， 在 shell 中设置PATH变量。
    -   **pkg** 目录用来放置代码源文件，在进行import时，是使用这个位置作为根目录的。自己编写的代码也应该放在这下面。
    -   **src** 用来放置安装的包的链接对象 (Object) 的。这个概念有点类似于链接库，Go 会将编译出的可连接库放在这里， 方便编译时链接。不同的系统和处理器架构的对象会在pkg存放在不同的文件夹中。
```shell
├── bin
│   └── hello
├── pkg
│   └── darwin_amd64
│       └── github.com
│           └── user
│               └── stringutil.a
└── src
    └── github.com
        └── user
            ├── hello
            │   ├── hello
            │   └── hello.go
            └── stringutil
                └── reverse.go
```
###进阶
- Memory Allocator
- Garbage Collector
- Goroutine Scheduler
- Channel
#### 参考资料  

- [A Tour of Go](https://tour.golang.org/welcome/1)
- [Go By Example](https://gobyexample.com)
- [How to Write Go Code](http://golang.org/doc/code.html#PackageNames)
- [go 编程基础（视频）](http://www.oschina.net/p/go-fundamental-programming)
- [Go学习笔记 -- 雨痕](https://github.com/nullne/book/blob/master/Go%20%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%20%E7%AC%AC%E5%9B%9B%E7%89%88.pdf)
- [Go 语言的包依赖管理](http://io-meter.com/2014/07/30/go's-package-management/)

