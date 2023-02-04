let num = 12 //185311
let amount = 0
let answer = []
let delits = []
let  i = 1
while (num <= 14)
  {
    // console.log(delits)
    if (num % i == 0)
    {
      amount = amount + 1
      delits[delits.length] = i
    }

    if (amount == 4 && num+1 == i)
    {
      console.log(i + ' ' + delits)
      i = 0
      num++
      delits = []
    }

    if (amount!=4 && num+1 == i)
    {
      i = 0
      num++
      delits = []
    }

    i++

  }

console.log('ended')