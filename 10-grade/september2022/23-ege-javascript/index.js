let s = Number(prompt('Введите S'))
let i = 0
while (s<43)
  {
    i++
    if (i % 2 == 0)
    {
      console.log("Ходит Ваня:")
    }else
    {
      console.log("Ходит Петя:")
    }
    let hod = Number(prompt())
    if (hod == 1)
    {
      s++
    }
        if (hod == 2)
    {
      s = s * 2
    }
        if (hod == 3)
    {
      s = s * 3
    }
    console.log("Камней: " + s)
  }

if (s < 72)
{
    if (i % 2 == 0)
    {
      console.log("Победил Ваня")
    }else
    {
      console.log("Победил Петя")
    }
}else
{
  if (i % 2 == 0)
      {
      console.log("Победил Петя")
    }else
    {
      console.log("Победил Ваня")
    }
}


//! 41
//! 2
//! 4 и 12