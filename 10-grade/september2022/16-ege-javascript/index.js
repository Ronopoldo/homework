const fs = require('fs')
let origin = fs.readFileSync('./27-B_1.txt').toString()
let a = 0
let b = 0
let doubleArray = []
let index = 0
let summ = 0
let array1 = origin.split('\r\n')
array1.forEach(element =>
  {
    a = Number(element.split(' ')[0])
    b = Number(element.split(' ')[1])

      if (a>b)
      {
        doubleArray[index] = [a,b]
        summ = summ + a
      }else
      {
        doubleArray[index] = [b,a]
        summ = summ + b
      }
    // console.log(a + ' ' + b + ' ' + index)
    index++
  })
index = 0
let biggerArray = []
doubleArray.forEach(element =>
  {
    biggerArray[index] = element[0]
    index++
  })
index = 0
let smallerArray = []
doubleArray.forEach(element =>
  {
    smallerArray[index] = element[1]
    index++
  })


// let smallest = 9000
// let indexSmallest = 0
// index = 0
// while (summ % 5 !== 0)
//   {
//     biggerArray.forEach(element =>
//       {
//         if (element < smallest)
//         {
//           smallest = element
//           indexSmallest = index
//         }
//         index++
//       })
//   }
biggerArray.sort((a, b) => a - b);

console.log(summ)

console.log(biggerArray)
